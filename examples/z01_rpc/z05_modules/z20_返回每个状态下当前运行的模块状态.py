from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.running_stats"))
msf.log.info(msf.call(module.running_stats))
