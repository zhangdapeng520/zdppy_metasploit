from zdppy_metasploit import *

msf = new_metasploit()


def demo1():
    """
    普通的上传方法
    :return:
    """
    options = [2, "upload Rakefile /tmp/Rakefile"]
    msf.log.info(msf.call(session.meterpreter_write, options))
    msf.log.info(msf.call(session.meterpreter_read, 2))


def demo2():
    """
    封装的上传方法
    :return:
    """
    msf.log.info(msf.upload(
        id=2,
        origin="msfvenom",
        src="/tmp/msfvenom"
    ))


if __name__ == '__main__':
    # demo1()
    demo2()
