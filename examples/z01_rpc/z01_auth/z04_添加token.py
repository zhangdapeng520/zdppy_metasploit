from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 添加token
msf.log.debug("添加token", msf.call("auth.token_add", ["aaa"]))

# 使用方法添加token
result = msf.add_token("aaa")
msf.log.debug("使用方法添加token", result=result.to_dict())
