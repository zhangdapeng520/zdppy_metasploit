class Auth:
    @property
    def login(self):
        return "auth.login"

    @property
    def token_generate(self):
        return "auth.token_generate"

    @property
    def token_list(self):
        return "auth.token_list"

    @property
    def token_add(self):
        return "auth.token_add"

    @property
    def token_remove(self):
        return "auth.token_remove"


auth = Auth()
