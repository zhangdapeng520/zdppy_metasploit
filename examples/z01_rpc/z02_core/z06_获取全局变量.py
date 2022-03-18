from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("core.setg", ["username", "zhangdapeng"]))
msf.log.info(msf.call(core.setg, ["password", "zhangdapeng"]))
msf.log.info(msf.call(core.set, ["age", "33"]))  # 快捷方式

msf.log.info(msf.call("core.getg", ["username"]))
msf.log.info(msf.call(core.getg, ["password"]))
msf.log.info(msf.call(core.get, ["age"]))
