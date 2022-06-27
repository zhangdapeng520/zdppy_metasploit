from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

msf.log.info(msf.call("module.compatible_payloads", 'windows/smb/ms08_067_netapi'))

msf.log.info(msf.call("module.compatible_exploit_payloads", 'windows/smb/ms08_067_netapi'))

msf.log.info(msf.call("module.target_compatible_payloads", ['windows/smb/ms08_067_netapi', 1]))
