class Plugin:
    @property
    def load(self):
        return "plugin.load"

    @property
    def unload(self):
        return "plugin.unload"

    @property
    def loaded(self):
        return "plugin.loaded"


plugin = Plugin()
