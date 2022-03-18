from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("core.setg", ["username", "zhangdapeng"]))
msf.log.info(msf.call(core.setg, ["password", "zhangdapeng"]))
msf.log.info(msf.call(core.set, ["age", "22"]))
