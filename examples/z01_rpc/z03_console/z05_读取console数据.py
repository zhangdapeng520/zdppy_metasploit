from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("console.list"))
msf.log.info(msf.call(console.list))

# 读写数据
msf.log.info(msf.call("console.write", ["0", "version\n"]))
msf.log.info(msf.call("console.read", 0))

msf.log.info(msf.call(console.write, ["0", "version\n"]))
msf.log.info(msf.call(console.read, 0))
