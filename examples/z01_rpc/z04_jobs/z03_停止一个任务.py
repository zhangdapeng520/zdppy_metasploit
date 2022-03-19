from zdppy_metasploit import *

msf = new_metasploit()

msf.log.info(msf.call("job.stop", 0))
msf.log.info(msf.call(job.stop, 0))
