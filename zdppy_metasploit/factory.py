from zdppy_yaml import Yaml
from .zdppy_metasploit import Metasploit


def new_metasploit(
        config: str = "config/config.yaml",
        config_secret: str = "config/secret/.config.yaml"
):
    """
    根据配置信息创建Metasploit对象
    :param config: 公开的配置信息
    :param config_secret: 私密的配置信息
    :return:
    """
    y = Yaml(config=config, config_secret=config_secret)
    msf = Metasploit(**y.config)
    return msf
