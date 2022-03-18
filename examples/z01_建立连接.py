from zdppy_metasploit import Metasploit

# 建立连接方式1
msf = Metasploit(
    username="msf",
    password="zhangdapeng",
    host="192.168.160.128",
    port=55553,
    path="/api/",
    is_ssl=False,
    token=None,
    encoding="utf-8",
    headers={"Content-type": "binary/message-pack"},
)

print(msf.client)

# 建立连接方式2
from zdppy_yaml import Yaml

y = Yaml()
print(y.config)
msf2 = Metasploit(**y.config)
print(msf2.client)

# 建立连接的方式3
from zdppy_metasploit import new_metasploit

msf3 = new_metasploit(config="config/config.yaml", config_secret="config/secret/.config.yaml")
print(msf3.client)

# 建立连接的方式4
from zdppy_metasploit import new_metasploit

msf4 = new_metasploit()
print(msf4.client)
