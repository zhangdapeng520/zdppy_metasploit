from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 添加
msf.log.debug(msf.set("age", 33))

# 获取
msf.log.debug(msf.get("age"))

# 删除
msf.log.debug(msf.call("core.unsetg", ["username"]))
msf.log.debug(msf.delete("age"))
msf.log.debug(msf.delete("age1"))
