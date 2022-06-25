from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 停止服务
msf.log.debug(msf.stop())
