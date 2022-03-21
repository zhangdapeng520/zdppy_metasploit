from zdppy_metasploit import *

msf = new_metasploit()

options = 2
msf.log.info(msf.call("session.ring_clear", options))
msf.log.info(msf.call(session.ring_clear, options))
