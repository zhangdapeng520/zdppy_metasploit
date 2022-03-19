from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("console.list"))
msf.log.info(msf.call(console.list))

# 读写数据
msf.log.info(msf.call("console.session_detach", ["5"]))
msf.log.info(msf.call("console.session_detach", 5))
