from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("core.reload_modules"))
msf.log.info(msf.call(core.reload_modules))
