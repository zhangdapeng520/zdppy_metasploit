from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

msf.log.debug(msf.get_thread_list())

# 杀死进程
msf.log.debug(msf.call("core.thread_kill", 2))
msf.log.debug(msf.delete_thread(2))

msf.log.debug(msf.get_thread_list())
