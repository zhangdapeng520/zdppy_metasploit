from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

msf.log.info(msf.call("console.list"))

# 读写数据
msf.log.info(msf.call("console.session_detach", ["5"]))
msf.log.info(msf.call("console.session_detach", 5))
