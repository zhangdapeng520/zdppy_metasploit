from .zdppy_metasploit import Metasploit

msf = None


def new_metasploit(
        username: str = "msf",
        password: str = "zhangdapeng",
        port: int = 55552,
        host: str = "127.0.0.1",
        path: str = "/api/",
        is_ssl: bool = False,
        token: str = None,
):
    """
    根据配置信息创建Metasploit对象
    :return:
    """
    # 新建一个msf
    msf = Metasploit(username=username,
                     password=password,
                     port=port,
                     host=host,
                     path=path,
                     is_ssl=is_ssl,
                     token=token, )
    return msf
