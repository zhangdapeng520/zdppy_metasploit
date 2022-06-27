from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

options = 2
msf.log.info(msf.call("session.meterpreter_session_kill", options))

options = 3
msf.log.info(msf.call("session.meterpreter_session_kill", options))
