from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

msf.log.debug(msf.get_console_list())

# 读写数据
msf.log.debug(msf.write_console(4, "ls -lah"))
msf.log.debug(msf.call("console.read", 4))
msf.log.debug(msf.read_console(4))
