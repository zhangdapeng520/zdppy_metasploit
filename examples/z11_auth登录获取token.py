from zdppy_metasploit import *

msf = new_metasploit()

# 第一种调用方式
print(msf.call("auth.login", ["msf", "zhangdapeng"], is_raw=False))
print(msf.call("auth.login", ["msf", "zhangdapeng1"], is_raw=False))

# 第二种调用方式
print(msf.call(auth.login, ["msf", "zhangdapeng"]))
print(msf.call(auth.login, ["msf", "zhangdapeng1"]))
