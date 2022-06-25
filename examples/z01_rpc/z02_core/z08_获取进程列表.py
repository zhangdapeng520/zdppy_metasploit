from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 获取进程列表
msf.log.debug(msf.call("core.thread_list"))
msf.log.debug(msf.get_thread_list())
