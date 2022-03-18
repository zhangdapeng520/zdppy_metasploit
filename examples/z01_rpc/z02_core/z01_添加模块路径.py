from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("core.add_module_path", ["/tmp/modules/"]))
msf.log.info(msf.call(core.add_module_path, ["/tmp/modules/"]))
