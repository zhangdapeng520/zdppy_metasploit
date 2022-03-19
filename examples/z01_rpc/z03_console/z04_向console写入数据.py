from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("console.list"))
msf.log.info(msf.call(console.list))

msf.log.info(msf.call("console.write", ["0", "ls -lah"]))
msf.log.info(msf.call(console.write, ["0", "ls -lah"]))
