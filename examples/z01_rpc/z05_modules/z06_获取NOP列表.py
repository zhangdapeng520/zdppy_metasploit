from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.nops"))
msf.log.info(msf.call(module.nops))
