from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

options = None
msf.log.info(msf.call("health.check", options))
msf.log.debug(msf.health())
