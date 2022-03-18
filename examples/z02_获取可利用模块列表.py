from zdppy_metasploit import new_metasploit

msf = new_metasploit()

# 获取可利用模块的列表
print(msf.client.modules.exploits)
