from zdppy_metasploit import *

msf = new_metasploit()

options = 2
msf.log.info(msf.call("session.meterpreter_session_kill", options))
msf.log.info(msf.call(session.meterpreter_session_kill, options))
