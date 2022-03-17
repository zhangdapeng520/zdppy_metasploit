from zdppy_metasploit import Metasploit

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