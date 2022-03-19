from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.architectures"))
msf.log.info(msf.call(module.architectures))
