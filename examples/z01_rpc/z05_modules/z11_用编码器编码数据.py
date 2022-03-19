from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.encode", ['AAAA', 'x86/shikata_ga_nai', {'format': 'c'}]))
msf.log.info(msf.call(module.encode, ['AAAA', 'x86/shikata_ga_nai', {'format': 'c'}]))
