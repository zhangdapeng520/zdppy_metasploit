from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.target_compatible_evasion_payloads", ['windows/windows_defender_exe', 0]))
msf.log.info(msf.call(module.target_compatible_evasion_payloads, ['windows/windows_defender_exe', 0]))
