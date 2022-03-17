from zdppy_metasploit import Metasploit

msf = Metasploit(
    username="msf",
    password="zhangdapeng",
    host="192.168.160.129",
    port=55552,
    path="/api/",
    is_ssl=False,
    token=None,
    encoding="utf-8",
    headers={"Content-type": "binary/message-pack"},
)

# 获取可利用模块的列表
print(msf.client.modules.exploits)
