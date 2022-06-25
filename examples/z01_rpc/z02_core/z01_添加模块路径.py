from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 使用call添加
msf.log.debug(msf.call("core.add_module_path", ["/tmp"]))

# 使用方法添加
msf.log.debug(msf.add_module_path("/zdpruby").to_dict())
