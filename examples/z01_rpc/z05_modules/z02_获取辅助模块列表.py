from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.auxiliary"))
msf.log.info(msf.call(module.auxiliary))
