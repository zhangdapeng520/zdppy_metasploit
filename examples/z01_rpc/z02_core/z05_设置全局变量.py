from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 使用call方法设置全局变量
msf.log.debug(msf.call("core.setg", ["username", "zhangdapeng"]))

# 使用封装方法设置全局变量
msf.log.debug(msf.set("a", 1))
