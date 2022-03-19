from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.evasion"))
msf.log.info(msf.call(module.evasion))
