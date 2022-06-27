from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

msf.log.info(msf.call("module.info_html", ['exploit', 'windows/smb/ms08_067_netapi']))
