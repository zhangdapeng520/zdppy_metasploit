from zdppy_metasploit import *

msf = new_metasploit()

options = 3
msf.log.info(msf.call("session.compatible_modules", options))
msf.log.info(msf.call(session.compatible_modules, options))
