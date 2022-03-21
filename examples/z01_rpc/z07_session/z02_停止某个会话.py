from zdppy_metasploit import *

msf = new_metasploit()

options = 1
msf.log.info(msf.call("session.stop", options))
msf.log.info(msf.call(session.stop, options))
