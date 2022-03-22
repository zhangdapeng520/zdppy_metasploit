from zdppy_metasploit import *

msf = new_metasploit()


def base_use():
    """
    基本使用
    :return:
    """
    msf.log.info(msf.call(console.create))

    msf.log.info(msf.call("console.list"))
    msf.log.info(msf.call(console.list))

    # 读写数据
    msf.log.info(msf.call("console.write", ["1", "pwd\n"]))
    msf.log.info(msf.call("console.read", 1))

    msf.log.info(msf.call(console.write, ["1", "pwd\n"]))
    msf.log.info(msf.call(console.read, 1))


def demo2():
    """
    一次完整的执行流程
    :return:
    """
    # 创建console
    result = msf.call(console.create)
    msf.log.info(result)

    console_id = result["id"]
    msf.log.info(msf.call(console.read, console_id))

    # 写入命令：执行命令
    cmd = "pwd"
    result = msf.call(console.write, [console_id, f"{cmd}\n"])
    msf.log.info(result)

    # 获取命令结果
    result = msf.call(console.read, console_id)
    msf.log.info(result)
    msf.log.info(result["data"])

    # 关闭会话
    msf.log.info(msf.call(console.session_kill, console_id))


def demo3():
    """
    一次完整的执行流程，简化版
    :return:
    """
    # 执行cmd命令
    result = msf.run_cmd("pwd")
    msf.log.info(f"命令输出结果：{result}")

    result = msf.run_cmd("whoami")
    msf.log.info(f"命令输出结果：{result}")

    result = msf.run_cmd("ls -lah /")
    msf.log.info(f"命令输出结果：{result}")


def demo4():
    console_id = 32
    result = msf.call(console.read, console_id)
    msf.log.info(f"命令输出结果：{result}")


if __name__ == '__main__':
    # base_use()
    # demo2()
    # demo3()
    # demo4()
    # msf.log.info(msf.run_cmd("show exploits"))
    # msf.log.info(msf.run_cmd("search samba"))

    cmds = [
        "use payload/windows/shell_bind_tcp",
        "generate -b '\x00' -e x86/shikata_ga_nai"
    ]
    msf.log.info(msf.run_cmd(cmds))
