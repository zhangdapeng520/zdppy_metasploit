from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 查看token
msf.log.debug("token列表", msf.get_token_list().to_dict())

# 删除token
msf.log.debug(msf.call("auth.token_remove", ["aaa"]))

# 使用方法删除
msf.log.debug(msf.delete_token("3eb631-c820-4606-ab4c-453bdd64a415").to_dict())
