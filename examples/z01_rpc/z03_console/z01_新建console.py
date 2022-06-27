from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

msf.log.debug(msf.call("console.create"))
msf.log.debug(msf.add_console())
