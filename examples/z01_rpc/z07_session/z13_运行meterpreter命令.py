from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

options = [3, 'pwd\n']
msf.log.info(msf.call("session.meterpreter_run_single", options))
