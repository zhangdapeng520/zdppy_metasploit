from zdppy_metasploit import *

msf = new_metasploit()

options = [2, "sysinfo"]
msf.log.info(msf.call("session.meterpreter_write", options))
msf.log.info(msf.call(session.meterpreter_write, options))
