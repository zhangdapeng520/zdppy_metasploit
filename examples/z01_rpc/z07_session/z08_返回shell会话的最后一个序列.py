from zdppy_metasploit import *

msf = new_metasploit()

options = 2
msf.log.info(msf.call("session.ring_last", options))
msf.log.info(msf.call(session.ring_last, options))
