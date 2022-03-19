from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("plugin.load", 'nexpose'))
msf.log.info(msf.call(plugin.load, 'nexpose'))
