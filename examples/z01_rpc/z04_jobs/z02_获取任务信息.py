from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("job.info", 0))
msf.log.info(msf.call(job.info, 0))
