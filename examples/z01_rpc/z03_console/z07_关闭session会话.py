from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

msf.log.info(msf.get_console_list())

# 关闭会话
msf.log.info(msf.call("console.session_kill", ["0"]))
msf.log.info(msf.delete_console_session(0))
