from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.compatible_evasion_payloads", 'windows/windows_defender_exe'))
msf.log.info(msf.call(module.compatible_evasion_payloads, 'windows/windows_defender_exe'))
