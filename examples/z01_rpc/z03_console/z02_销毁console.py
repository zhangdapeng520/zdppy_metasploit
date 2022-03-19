from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("console.create"))
msf.log.info(msf.call(console.create))

# 销毁
msf.log.info(msf.call("console.destroy", 1))
msf.log.info(msf.call(console.destroy, 2))
