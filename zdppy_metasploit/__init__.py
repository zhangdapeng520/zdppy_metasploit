from .zdppy_metasploit import Metasploit
from .factory import new_metasploit

# z01_rpc 支持的方法
from .rpc.core import core
from .rpc.auth import auth
from .rpc.console import console
from .rpc.job import job
from .rpc.module import module
from .rpc.plugin import plugin
from .rpc.session import session
from .rpc.health import health
