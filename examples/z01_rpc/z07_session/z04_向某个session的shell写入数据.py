from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

options = [1, "ls\n"]
msf.log.info(msf.call("session.shell_write", options))
