from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.executable_formats"))
msf.log.info(msf.call(module.executable_formats))
