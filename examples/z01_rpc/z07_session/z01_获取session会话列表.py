from zdppy_metasploit import *

msf = new_metasploit()

options = None
msf.log.info(msf.call("session.list", options))

result = msf.call(session.list, options)
msf.log.info(list(result.keys()))
