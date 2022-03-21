class Session:
    @property
    def list(self):
        return "session.list"

    @property
    def stop(self):
        return "session.stop"

    @property
    def shell_read(self):
        return "session.shell_read"

    @property
    def shell_write(self):
        return "session.shell_write"

    @property
    def shell_upgrade(self):
        return "session.shell_upgrade"

    @property
    def meterpreter_read(self):
        return "session.meterpreter_read"

    @property
    def ring_put(self):
        return "session.ring_put"

    @property
    def ring_last(self):
        return "session.ring_last"

    @property
    def ring_clear(self):
        return "session.ring_clear"

    @property
    def meterpreter_write(self):
        return "session.meterpreter_write"

    @property
    def meterpreter_session_kill(self):
        return "session.meterpreter_session_kill"

    @property
    def meterpreter_tabs(self):
        return "session.meterpreter_tabs"

    @property
    def meterpreter_run_single(self):
        return "session.meterpreter_run_single"

    @property
    def meterpreter_directory_separator(self):
        return "session.meterpreter_directory_separator"

    @property
    def compatible_modules(self):
        return "session.compatible_modules"


session = Session()
