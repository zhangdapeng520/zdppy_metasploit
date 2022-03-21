from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("console.list"))
msf.log.info(msf.call(console.list))

# 关闭会话
msf.log.info(msf.call("console.session_kill", ["0"]))
msf.log.info(msf.call(console.session_kill, 0))

# 注意：关闭会话不等于关闭console终端
msf.log.info(msf.call(console.list))
