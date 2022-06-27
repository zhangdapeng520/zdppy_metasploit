from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

options = [1, "pwd"]
msf.log.info(msf.call("session.ring_put", options))
