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
msf.log.info(exploit.target)
msf.log.info(exploit.targets)
msf.log.info(exploit.default_target)

# 找到目标的有效载荷
msf.log.info(exploit.targetpayloads())

# 查看和设置模块选项
msf.log.info(exploit.options)
