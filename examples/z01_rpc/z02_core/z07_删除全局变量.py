from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("core.setg", ["username", "zhangdapeng"]))
msf.log.info(msf.call(core.setg, ["password", "zhangdapeng"]))
msf.log.info(msf.call(core.set, ["age", "22"]))

msf.log.info(msf.call("core.getg", ["username"]))
msf.log.info(msf.call(core.getg, ["password"]))
msf.log.info(msf.call(core.get, ["age"]))

msf.log.info(msf.call("core.unsetg", ["username"]))
msf.log.info(msf.call(core.unsetg, ["password"]))
msf.log.info(msf.call(core.delete, ["age"]))

msf.log.info(msf.call("core.getg", ["username"]))
msf.log.info(msf.call(core.getg, ["password"]))
msf.log.info(msf.call(core.get, ["age"]))
