class Console:
    @property
    def create(self):
        return "console.create"

    @property
    def destroy(self):
        return "console.destroy"

    @property
    def list(self):
        return "console.list"

    @property
    def write(self):
        return "console.write"

    @property
    def read(self):
        return "console.read"

    @property
    def session_detach(self):
        return "console.session_detach"

    @property
    def session_kill(self):
        return "console.session_kill"

    @property
    def tabs(self):
        return "console.tabs"


console = Console()
