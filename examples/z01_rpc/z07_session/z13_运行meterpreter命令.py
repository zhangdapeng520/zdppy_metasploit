from zdppy_metasploit import *

msf = new_metasploit()

options = [3, 'sysin']
msf.log.info(msf.call("session.meterpreter_run_single", options))
msf.log.info(msf.call(session.meterpreter_run_single, options))
