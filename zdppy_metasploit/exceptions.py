class MetasploitException(Exception):
    """
    Metasploit的根异常
    """

    def __init__(self, *args):
        super(MetasploitException, self).__init__(*args)


class NotfoundError(MetasploitException):
    """
    未发现异常
    """

    def __init__(self, *args):
        super(NotfoundError, self).__init__(*args)


class ParamError(MetasploitException):
    """
    参数错误
    """

    def __init__(self, *args):
        super(ParamError, self).__init__(*args)


class InternalError(MetasploitException):
    """
    服务器错误
    """

    def __init__(self, *args):
        super(InternalError, self).__init__(*args)
