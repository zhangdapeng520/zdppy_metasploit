from zdppy_metasploit import *

msf = new_metasploit()

options = [3, 'pwd\n']
msf.log.info(msf.call("session.meterpreter_run_single", options))
msf.log.info(msf.call(session.meterpreter_run_single, options))

# 读取命令并获取命令输出
msf.log.info(msf.call(session.meterpreter_run_single, [3, 'search -f README.txt\n']))
msf.log.info(msf.call(session.meterpreter_read, 3))
