from zdppy_metasploit import *

msf = new_metasploit()

# 查看token
print(msf.call(auth.token_list))

# 添加token
print(msf.call("auth.token_add", ["aaa"]))
print(msf.call(auth.token_add, ["bbb"]))

# 查看token
print(msf.call(auth.token_list))

# 删除token
print(msf.call("auth.token_remove", ["aaa"]))
print(msf.call(auth.token_remove, ["bbb"]))

# 查看token
print(msf.call(auth.token_list))
