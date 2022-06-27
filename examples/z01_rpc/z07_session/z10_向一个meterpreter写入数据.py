from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

options = [2, "sysinfo"]
msf.log.info(msf.call("session.meterpreter_write", options))
