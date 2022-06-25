from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 这个方法不用传参，官方文档没有更新
msf.log.debug(msf.call("auth.token_generate", [], is_raw=False))

# 直接调用方法生成token
msf.log.debug(msf.generate_token().to_dict())
