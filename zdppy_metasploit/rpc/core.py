class Core:
    @property
    def version(self):
        return "core.version"

    @property
    def add_module_path(self):
        return "core.add_module_path"

    @property
    def module_stats(self):
        return "core.module_stats"

    @property
    def reload_modules(self):
        return "core.reload_modules"

    @property
    def save(self):
        return "core.save"

    @property
    def setg(self):
        return "core.setg"

    @property
    def set(self):
        return "core.setg"

    @property
    def getg(self):
        return "core.getg"

    @property
    def get(self):
        return "core.getg"

    @property
    def unsetg(self):
        return "core.unsetg"

    @property
    def delete(self):
        return "core.unsetg"

    @property
    def thread_list(self):
        return "core.thread_list"

    @property
    def thread_kill(self):
        return "core.thread_kill"

    @property
    def stop(self):
        return "core.stop"


core = Core()
