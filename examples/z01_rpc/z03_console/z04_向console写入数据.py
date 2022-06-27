from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)
msf.log.debug(msf.get_console_list())

msf.log.info(msf.call("console.write", ["4", "ls -lah"]))
msf.log.info(msf.write_console(4, "ls -lah"))
