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
