from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("console.create"))
msf.log.info(msf.call(console.create))
