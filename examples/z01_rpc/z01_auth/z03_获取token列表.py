from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 调用call方法
msf.log.debug("获取token列表", msf.call("auth.token_list"))

# 调用get_token_list方法
msf.log.debug("获取token列表", msf.get_token_list().to_dict())
