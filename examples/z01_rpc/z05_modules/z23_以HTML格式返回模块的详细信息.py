from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("module.info_html", ['exploit', 'windows/smb/ms08_067_netapi']))
msf.log.info(msf.call(module.info_html, ['exploit', 'windows/smb/ms08_067_netapi']))
