from zdppy_metasploit import *

msf = new_metasploit()

options = [1, "0.0.0.0", 8888]
msf.log.info(msf.call("session.shell_upgrade", options))
msf.log.info(msf.call(session.shell_upgrade, options))
