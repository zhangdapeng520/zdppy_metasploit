from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 获取版本信息
msf.log.debug(msf.call("core.version"))
msf.log.debug(msf.version())
