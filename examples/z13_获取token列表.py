from zdppy_metasploit import *

msf = new_metasploit()

print(msf.call("auth.token_list"))
print(msf.call(auth.token_list))
