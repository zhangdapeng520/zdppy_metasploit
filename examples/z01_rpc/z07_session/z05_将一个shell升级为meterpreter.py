from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)


def demo1():
    """
    普通方法
    :return:
    """
    options = [1, "0.0.0.0", 8888]
    msf.log.info(msf.call("session.shell_upgrade", options))


def demo2():
    """
    使用封装的方法
    :return:
    """
    msf.log.info(msf.create_meterpreter())


if __name__ == '__main__':
    # demo1()
    demo2()
