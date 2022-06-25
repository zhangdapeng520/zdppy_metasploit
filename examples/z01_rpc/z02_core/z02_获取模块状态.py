from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 使用call方法获取
msf.log.debug(msf.call("core.module_stats"))

# 使用封装方法获取
msf.log.debug(msf.get_module_status().to_dict())
