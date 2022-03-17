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

# 利用模块
exploit = msf.client.modules.use("exploit", "unix/ftp/vsftpd_234_backdoor")

# 查看目标
print(exploit.target)
print(exploit.targets)
print(exploit.default_target)
