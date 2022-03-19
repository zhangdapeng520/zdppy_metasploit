from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("job.list"))
msf.log.info(msf.call(job.list))
