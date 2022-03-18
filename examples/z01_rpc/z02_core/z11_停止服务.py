from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("core.stop"))
msf.log.info(msf.call(core.stop))
