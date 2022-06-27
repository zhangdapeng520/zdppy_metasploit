from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

msf.log.info(msf.call("console.list"))

# 获取tabs
msf.log.info(msf.call("console.session_detach", 7))
msf.log.info(msf.call("console.tabs", [7, "use exploit/windows/smb/ms08_067_"]))
