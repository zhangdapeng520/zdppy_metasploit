from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 使用call方法
msf.log.debug(msf.call("core.save"))

# 使用封装方法
msf.log.debug(msf.save())
