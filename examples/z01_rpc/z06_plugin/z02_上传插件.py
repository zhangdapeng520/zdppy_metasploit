from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("plugin.unload", 'nexpose'))
msf.log.info(msf.call(plugin.unload, 'nexpose'))
