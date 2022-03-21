from zdppy_metasploit import *

msf = new_metasploit()

options = [1, "ls\n"]
msf.log.info(msf.call("session.shell_write", options))
msf.log.info(msf.call(session.shell_write, options))
