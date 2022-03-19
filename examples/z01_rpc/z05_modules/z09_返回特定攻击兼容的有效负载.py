from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.compatible_payloads", 'windows/smb/ms08_067_netapi'))
msf.log.info(msf.call(module.compatible_payloads, 'windows/smb/ms08_067_netapi'))

msf.log.info(msf.call("module.compatible_exploit_payloads", 'windows/smb/ms08_067_netapi'))
msf.log.info(msf.call(module.compatible_exploit_payloads, 'windows/smb/ms08_067_netapi'))

msf.log.info(msf.call("module.target_compatible_payloads", ['windows/smb/ms08_067_netapi', 1]))
msf.log.info(msf.call(module.target_compatible_payloads, ['windows/smb/ms08_067_netapi', 1]))
