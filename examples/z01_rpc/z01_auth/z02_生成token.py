from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)

# 获取响应
response = msf.call("auth.login", ["msf", "zhangdapeng"], is_raw=False)

# 获取token
token = None
if response is not None:
    token = response.get("token")

if token is None:
    print("获取token失败")
    exit(0)

# 生成token
print("获取token成功：", token)

# 这个方法不用传参，官方文档没有更新
print(msf.call("auth.token_generate", [], is_raw=False))
print(msf.call(auth.token_generate, [], is_raw=False))
