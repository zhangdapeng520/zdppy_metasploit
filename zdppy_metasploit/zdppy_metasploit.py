import json
from typing import List, Tuple, Union, Dict, Any
from .pymetasploit3.msfrpc import MsfRpcClient
from zdppy_log import Log
from .exceptions import NotfoundError, ParamError, InternalError


class Result:
    """
    响应结果
    """

    def __init__(self,
                 status: bool = True,
                 result: str = "success",
                 token: str = "",
                 token_list: List[str] = None,
                 error_message: str = "",
                 data: Dict = None
                 ):
        self.status: bool = status
        self.result: str = result
        self.token: str = token
        self.token_list: List[str] = token_list
        self.error_message = error_message
        self.data = data

    def to_dict(self):
        r = {
            "status": self.status,
            "result": self.result or "success"
        }
        if self.token:
            r["token"] = self.token
        if self.token_list:
            r["token_list"] = self.token_list
        if self.error_message:
            r["error_message"] = self.error_message
        if self.data:
            r["data"] = self.data
        return r

    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return self.to_json()


def get_fail_result(error_message: str = "") -> Result:
    """
    获取失败的结果
    """
    fail_result = Result(status=False, result="failure", error_message=error_message)
    return fail_result


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
                 log_file_path: str = "log.log",
                 console_pool_size: int = 3,  # console池子对象个数
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
        self.sessions = None  # 存储所有的session会话

    def __init_consoles(self):
        """
        初始化console字典
        :return:
        """
        result = self.call("console.list")
        consoles = result.get('consoles', None)

        # 合并已有的console
        if consoles:
            temp_consoles = [i["id"] for i in consoles if not i["busy"]]
            self.consoles.extend(temp_consoles)

        # 创建一个新的可用的console
        else:
            for _ in range(self.console_pool_size):
                # 创建console
                result = self.call("console.create")

                # 获取控制台输出
                console_id = result.get('id')
                result = self.call("console.read", console_id)

                # 添加到console池子
                if console_id is not None:
                    self.consoles.append(console_id)
                else:
                    raise NotfoundError("找不到可用的console")

    def get_module_exploits(self) -> Result:
        """
        获取可利用的模块
        """
        return Result(data=self.call("module.exploits"))

    def health(self) -> Result:
        """
        健康检查
        """
        data = self.call("health.check", None)
        if data.get("status") == "UP":
            return Result()
        return get_fail_result()

    def login(self) -> Result:
        """
        登录并获取token
        """
        result = self.call("auth.login", [self.username, self.password], is_raw=False)
        r = Result(result=result.get("result"), token=result.get("token"))
        return r

    def version(self) -> Result:
        """
        获取版本信息
        """
        return Result(data=dict(self.call("core.version")))

    def stop(self) -> Result:
        """
        停止服务
        """
        try:
            self.call("core.stop")
        finally:
            pass
        return Result()

    def generate_token(self) -> Result:
        """
        生成token
        """
        result = self.call("auth.token_generate", [], is_raw=False)
        r = Result(result=result.get("result"), token=result.get("token"))
        return r

    def get_token_list(self) -> Result:
        """
        获取token列表
        """
        result = self.call("auth.token_list")
        r = Result(token_list=result.get("tokens"))
        return r

    def add_token(self, *tokens: str) -> Result:
        """
        添加token，可以同时添加多个
        """
        if len(tokens) == 0:
            self.log.error("要添加的token不能少于1个", tokens=tokens)
            return Result(result="fail", status=False)

        # 添加token
        result = self.call("auth.token_add", tokens)

        # 获取token列表
        r = self.get_token_list()

        # token为刚添加的第一个token
        r.token = tokens[0]

        # 添加结果
        r.result = result.get("result")

        # 返回
        return r

    def delete_token(self, *tokens: str) -> Result:
        """
        删除token，支持批量删除
        """
        if len(tokens) == 0:
            self.log.error("要删除的token不能少于1个")
            return Result(status=False, result="fail")

        # 删除
        result = self.call("auth.token_remove", tokens)

        # 获取token列表
        r = self.get_token_list()
        r.result = result.get("result")
        r.token = tokens[0]

        # 返回
        return r

    def add_module_path(self, *paths: str) -> Result:
        """
        添加模块路径
        """
        if len(paths) == 0:
            self.log.error("添加模块路径失败，要添加的模块路径个数不能少于1", paths=paths)
            return get_fail_result(error_message="要添加的模块路径个数不能少于1")

        # 添加模块路径
        result = self.call("core.add_module_path", paths)
        if result.get("error"):
            return get_fail_result(result.get("error_message"))

        # 添加成功
        r = Result(result=result.get("result") or "success")
        r.data = dict(result)
        return r

    def get_module_status(self) -> Result:
        """
        获取模块状态
        """
        result = self.call("core.module_stats")
        return Result(data=dict(result))

    def reload_modules(self) -> Result:
        """
        重新加载模块
        """
        result = self.call("core.reload_modules")
        return Result(data=dict(result))

    def save(self) -> Result:
        """
        保存配置
        """
        result = self.call("core.save")
        if result.get("result") == "success":
            return Result()
        return get_fail_result(result.get("error_message"))

    def set(self, key: str, value: Any) -> Result:
        """
        设置全局变量
        """
        # 调用方法
        result = self.call("core.setg", [key, value])

        # 判断结果并返回
        if result.get("result") == "success":
            return Result()
        return get_fail_result(error_message=result.get("error_message"))

    def get(self, key: str) -> Result:
        """
        根据键获取值
        """
        result = self.call("core.getg", [key])
        if result.get(key):
            return Result(data=dict(result))
        return get_fail_result("找不到该key对应的value")

    def delete(self, key: str) -> Result:
        """
        删除全局变量
        """
        # 这个请求始终返回的是success，不存在删除失败的情况
        self.call("core.unsetg", [key])
        return Result()

    def get_thread_list(self) -> Result:
        """
        获取进程列表
        """
        return Result(data=dict(self.call("core.thread_list")))

    def write_console(self, console_id: int, command: str) -> Result:
        """
        向控制台写入命令
        """
        data = self.call("console.write", [str(console_id), f"{command}\n"])
        return Result(data=data)

    def get_console_list(self) -> Result:
        """
        获取console列表
        """
        return Result(data=self.call("console.list"))

    def delete_console_session(self, console_id: int) -> Result:
        """
        关闭console会话，但是不会销毁console
        """
        data = self.call("console.session_kill", [console_id])
        if data.get("result") == "success":
            return Result()
        return get_fail_result()

    def delete_thread(self, thread_id: int) -> Result:
        """
        杀死进程，删除进程
        """
        # 杀死进程
        result = self.call("core.thread_kill", thread_id)

        # 判断结果
        if result.get("error"):
            return get_fail_result(error_message=result.get("error_message"))
        return Result()

    def add_console(self) -> Result:
        """
        添加console
        """
        result = self.call("console.create")
        return Result(data=dict(result))

    def read_console(self, console_id: int):
        """
        读取console数据
        """
        data = self.call("console.read", console_id)
        return Result(data=data)

    def delete_console(self, console_id: int) -> Result:
        """
        删除console
        """
        result = self.call("console.destroy", console_id)
        if result.get("result") == "success":
            return Result()
        return get_fail_result("删除console失败")

    def run_cmd(self, cmd: Union[str, List, Tuple], only_data=True):
        """
        执行CMD命令
        :param cmd 要执行的cmd命令
        :param only_data 只获取data数据
        :return:
        """
        # 需要初始化console池子
        if len(self.consoles) == 0:
            self.__init_consoles()
        if len(self.consoles) == 0:
            raise NotfoundError("找不到可用的console")

        # 负载均衡：随机的取一个console
        console_id = self.consoles.pop()

        # 执行命令
        result = None
        if isinstance(cmd, str):
            self.call("console.write", [console_id, f"{cmd}\n"])
            result = self.call("console.read", console_id)
        elif isinstance(cmd, list) or isinstance(cmd, tuple):
            for c in cmd:
                self.call("console.write", [console_id, f"{c}\n"])
                result = self.call("console.read", console_id)
        else:
            raise ParamError("cmd参数格式错误")

        # 将console归还到池子
        self.consoles.append(console_id)

        # 校验结果
        if result is None:
            raise InternalError("服务器内部错误")

        # 返回命令输出结果
        if only_data:
            return result.get("data")
        return result

    def upload(self,
               id: int,
               origin: str,
               src: str,
               ):
        """
        上传文件到受控主机
        :param id: meterprter的ID，是一个session id
        :param origin: 部署msf服务的服务器上文件的路径，暂时不支持传本地文件
        :param src: 受控主机上的文件路径
        :return:
        """
        # 更新sessions
        if self.sessions is None:
            self.sessions = self.call("session.list")
        if self.sessions is None:
            raise NotfoundError("未发现可用的session")

        # 判断类型
        meterpreter = self.sessions.get(id, None)
        if meterpreter is None:
            raise NotfoundError("该meterpreter不存在")
        if meterpreter.get('type') != "meterpreter":
            raise ParamError("该session不是一个meterpreter")

        # 使用该meterpreter上传文件
        options = [id, f"upload {origin} {src}"]
        self.log.debug(self.call("session.meterpreter_write", options))
        result = self.call("session.meterpreter_read", id)
        self.log.debug(result)

        # 返回结果
        return result

    def use(self,
            module_type: str = "exploit",
            module_name: str = "unix/ftp/vsftpd_234_backdoor",
            rhosts: str = None,
            payload: str = "cmd/unix/interact",
            **kwargs,
            ):
        """
        使用一个模块
        :return:
        """
        # 准备参数
        opts = {}
        if rhosts:
            opts["RHOSTS"] = rhosts
        if payload:
            opts["payload"] = payload
        if len(kwargs):
            opts.extend(kwargs)
        params = [module_type, module_name, opts]

        # 执行模块
        result = self.call("module.execute", params)
        if not (result.get("job_id") and result.get("uuid")):
            raise InternalError(f"执行模块失败：{result}")

        return result

    def create_meterpreter(self,
                           session_id: int = None,
                           lhosts: str = "0.0.0.0",
                           lport: int = 18888,
                           ):
        """
        创建一个meterpreter
        :return:
        """
        # 没有传session id，默认取sessions中id最大的那个（最新创建的）
        if session_id is None:
            # 获取sessions
            self.sessions = self.call("session.list")
            if not self.sessions:
                raise NotfoundError("没有可用的session")
            max_session_id = max(list(self.sessions.keys()))

            # 获取session
            session = self.sessions.get(max_session_id)
            if not session:
                raise NotfoundError("该session不可用")

            session_id = max_session_id

        # session升级为meterpreter
        options = [session_id, lhosts, lport]
        result = self.call("session.shell_upgrade", options)
        self.log.debug(f"session升级为meterpreter：{result}")

        # 返回结果
        return result
