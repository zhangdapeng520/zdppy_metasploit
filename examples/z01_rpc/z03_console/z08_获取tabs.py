from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("console.list"))
msf.log.info(msf.call(console.list))

# 关闭会话
msf.log.info(msf.call("console.tabs", [0, "use exploit/windows/smb/ms08_067_"]))
msf.log.info(msf.call(console.tabs, [0, "use exploit/windows/smb/ms08_067_"]))
