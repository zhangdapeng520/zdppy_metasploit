from .libs.pymetasploit3.msfrpc import MsfRpcClient
from zdppy_log import Log


class Metasploit:
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

        # 日志对象
        self.log = Log(log_file_path=log_file_path, debug=debug)

        # 创建rpc客户端
        self.client = MsfRpcClient(
            password,
            uri=path,
            port=port,
            server=host,
            ssl=is_ssl,
            token=token,
            encoding=encoding,
            headers=headers,
            username=username,
            log=self.log
        )
