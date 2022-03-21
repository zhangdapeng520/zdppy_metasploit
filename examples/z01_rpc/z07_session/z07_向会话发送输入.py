from zdppy_metasploit import *

msf = new_metasploit()

options = [1, "pwd"]
msf.log.info(msf.call("session.ring_put", options))
msf.log.info(msf.call(session.ring_put, options))
