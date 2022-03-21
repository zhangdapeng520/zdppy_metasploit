from zdppy_metasploit import *

msf = new_metasploit()

opts = {'RHOSTS': '192.168.160.130'}
result = msf.call(module.execute, ['auxiliary', 'scanner/portscan/syn', opts])
msf.log.info(result)

job_id = result["job_id"]
result = msf.call(job.info, job_id)
msf.log.info(result)

options = None
msf.log.info(msf.call(session.list, options))
