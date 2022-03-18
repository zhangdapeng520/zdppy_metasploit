from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("core.save"))
msf.log.info(msf.call(core.save))
