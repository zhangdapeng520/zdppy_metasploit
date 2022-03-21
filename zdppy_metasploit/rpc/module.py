class Module:
    @property
    def exploits(self):
        return "module.exploits"

    @property
    def auxiliary(self):
        return "module.auxiliary"

    @property
    def post(self):
        return "module.post"

    @property
    def payloads(self):
        return "module.payloads"

    @property
    def encoders(self):
        return "module.encoders"

    @property
    def nops(self):
        return "module.nops"

    @property
    def info(self):
        return "module.info"

    @property
    def options(self):
        return "module.options"

    @property
    def compatible_payloads(self):
        return "module.compatible_payloads"

    @property
    def compatible_exploit_payloads(self):
        return "module.compatible_exploit_payloads"

    @property
    def target_compatible_payloads(self):
        return "module.target_compatible_payloads"

    @property
    def compatible_sessions(self):
        return "module.compatible_sessions"

    @property
    def encode(self):
        return "module.encode"

    @property
    def execute(self):
        """
        支持的类型：exploit、auxiliary、post、payload、evasion
        :return:
        """
        return "module.execute"

    @property
    def executable_formats(self):
        return "module.executable_formats"

    @property
    def transform_formats(self):
        return "module.transform_formats"

    @property
    def encryption_formats(self):
        return "module.encryption_formats"

    @property
    def platforms(self):
        return "module.platforms"

    @property
    def architectures(self):
        return "module.architectures"

    @property
    def encode_formats(self):
        return "module.encode_formats"

    @property
    def running_stats(self):
        return "module.running_stats"

    @property
    def target_compatible_evasion_payloads(self):
        return "module.target_compatible_evasion_payloads"

    @property
    def compatible_evasion_payloads(self):
        return "module.compatible_evasion_payloads"

    @property
    def info_html(self):
        return "module.info_html"

    @property
    def evasion(self):
        return "module.evasion"


module = Module()
