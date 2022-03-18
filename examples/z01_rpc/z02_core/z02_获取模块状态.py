from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("core.module_stats"))
msf.log.info(msf.call(core.module_stats))
