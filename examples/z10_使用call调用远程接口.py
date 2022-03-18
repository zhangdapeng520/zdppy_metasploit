from zdppy_metasploit import *

msf = new_metasploit()

# 查看msf的版本号
print(msf.call("core.version"))

# 第二种调用方式
print(msf.call(core.version))
