from zdppy_yaml import Yaml
from .zdppy_metasploit import Metasploit

msf = None


def new_metasploit(
        config: str = "config/config.yaml",
        config_secret: str = "config/secret/.config.yaml",
        force_new: bool = False
):
    """
    根据配置信息创建Metasploit对象
    :param config: 公开的配置信息
    :param config_secret: 私密的配置信息
    :param force_new 是否强制新增，当想要使用不同的配置文件创建新的MSF客户端的时候开启
    :return:
    """
    # 返回唯一一个msf
    global msf
    if not force_new and msf is not None:
        return msf

    # 新建一个msf
    y = Yaml(config=config, config_secret=config_secret)
    msf = Metasploit(**y.config)
    return msf
