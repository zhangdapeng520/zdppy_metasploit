from zdppy_metasploit import *

msf = new_metasploit()

options = 3
msf.log.info(msf.call("session.meterpreter_directory_separator", options))
msf.log.info(msf.call(session.meterpreter_directory_separator, options))
