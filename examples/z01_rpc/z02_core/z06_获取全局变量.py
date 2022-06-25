from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 设置全局变量
msf.log.debug(msf.set("username", "zhangdapeng333"))

# 获取全局变量
msf.log.debug(msf.call("core.getg", ["username"]))
msf.log.debug(msf.call("core.getg", ["username1111"]))

# 使用封装的方法获取全局变量
msf.log.debug(msf.get("username"))
msf.log.debug(msf.get("username1111"))
