from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 增加
msf.log.debug(msf.add_console())

# 销毁
msf.log.debug(msf.call("console.destroy", 1))
msf.log.debug(msf.delete_console(5))
