import random
from typing import Dict, List

import item as item

from .libs.pymetasploit3.msfrpc import MsfRpcClient
from zdppy_log import Log
from .rpc.console import console
from .exceptions import NotfoundError


class Metasploit:
    # 全局缓存对象
    cache_dict = dict()

    def __init__(self,
                 username: str = "msf",
                 password: str = "zhangdapeng",
                 port: int = 55552,
                 host: str = "127.0.0.1",
                 path: str = "/api/",
                 is_ssl: bool = False,
                 token: str = None,
                 encoding: str = "utf8",
                 headers: dict = {"Content-type": "binary/message-pack"},
                 debug: bool = True,
                 log_file_path: str = "logs/zdppy/zdppy_metasploit.log",
                 console_pool_size: int = 33,  # console池子对象个数
                 ):
        """
        创建MSF核心对象
        :param username: 用户名
        :param password: 密码
        :param port: 端口
        :param host: 主机ip
        :param path: 请求路径
        :param is_ssl: 是否为ssl
        :param token: 校验token
        :param encoding: 编码
        :param headers: 请求头
        :param debug: 是否为开发模式
        :param log_file_path: 日志路径
        """
        # rpc操作核心对象
        self.username = username
        self.password = password
        self.port = port
        self.host = host
        self.path = path
        self.is_ssl = is_ssl
        self.token = token
        self.encoding = encoding
        self.headers = headers
        self.debug = debug
        self.__log_file_path = log_file_path
        self.console_pool_size = console_pool_size

        # 日志对象
        self.log = Log(log_file_path=log_file_path, debug=debug)
        self.log.debug("创建日志对象成功")

        # 创建rpc客户端
        self.client = MsfRpcClient(
            password,
            self.log,
            uri=path,
            port=port,
            server=host,
            ssl=is_ssl,
            token=token,
            encoding=encoding,
            headers=headers,
            username=username
        )

        # 方法区
        self.call = self.client.call

        # console id列表
        self.consoles: List[str] = []

    def __init_consoles(self):
        """
        初始化console字典
        :return:
        """
        self.log.debug("初始化控制台列表")
        result = self.call(console.list)
        self.log.debug(f"获取控制台列表：{result}")
        consoles = result.get('consoles')

        # 合并已有的console
        if consoles is not None:
            temp_consoles = [i["id"] for i in consoles if not i["busy"]]
            self.consoles.extend(temp_consoles)
            self.log.debug(f"合并已有的console成功：{self.consoles}")

        # 创建一个新的可用的console
        else:
            for _ in range(self.console_pool_size):
                # 创建console
                result = self.call(console.create)
                self.log.debug(f"创建console：{result}")

                # 获取控制台输出
                console_id = result.get('id')
                result = self.call(console.read, console_id)
                self.log.debug(f"创建console控制台输出：{result}")

                # 添加到console池子
                if console_id is not None:
                    self.consoles.append(console_id)
                else:
                    raise NotfoundError("找不到可用的console")

    def run_cmd(self, cmd: str, only_data=True):
        """
        执行CMD命令
        :param cmd 要执行的cmd命令
        :param only_data 只获取data数据
        :return:
        """
        # 需要初始化console池子
        if len(self.consoles) == 0:
            self.__init_consoles()

        # 负载均衡：随机的取一个console
        console_id = self.consoles.pop()
        self.log.debug(f"获取随机的console成功：{console_id} {self.consoles}")

        # 执行命令
        self.log.debug(f"执行命令：{cmd}")
        self.call(console.write, [console_id, f"{cmd}\n"])
        result = self.call(console.read, console_id)
        self.log.debug(f"控制台输出：{result}")

        # 将console归还到池子
        self.consoles.append(console_id)

        # 返回命令输出结果
        if only_data:
            return result.get("data")
        return result
