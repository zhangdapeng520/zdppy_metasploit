from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.encode_formats"))
msf.log.info(msf.call(module.encode_formats))
