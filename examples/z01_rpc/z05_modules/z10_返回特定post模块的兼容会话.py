from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.compatible_sessions", 'windows/wlan/wlan_profile'))
msf.log.info(msf.call(module.compatible_sessions, 'windows/wlan/wlan_profile'))
