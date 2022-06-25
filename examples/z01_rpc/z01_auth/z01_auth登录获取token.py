from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 第一种调用方式
result = msf.call("auth.login", ["msf", "zhangdapeng"], is_raw=False)
msf.log.debug(f"获取token成功", result=result)

# 第二种方式，直接调用login
result = msf.login()
msf.log.debug(f"获取token成功", result=result.to_dict())
