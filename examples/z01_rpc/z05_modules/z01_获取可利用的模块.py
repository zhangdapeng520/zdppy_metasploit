from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.exploits"))
msf.log.info(msf.call(module.exploits))
