from zdppy_metasploit import *

msf = new_metasploit(host="192.168.213.131", port=55553)


def demo1():
    options = 4
    msf.log.info(msf.call("session.stop", options))
    # msf.log.info(msf.call(session.stop, options))


def demo2():
    options = [4, 5, 6]
    msf.log.info(msf.call("session.stop_list", options))


if __name__ == '__main__':
    # demo1()
    demo2()
