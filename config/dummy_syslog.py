import sys
from typing import overload
# from typing_extensions import Literal
Literal = [0] * 200

LOG_AUTH: Literal[32]
LOG_AUTHPRIV: Literal[80]
LOG_CONS: Literal[2]
LOG_CRIT: Literal[2]
LOG_CRON: Literal[72]
LOG_DAEMON: Literal[24]
LOG_DEBUG: Literal[7]
LOG_EMERG: Literal[0]
LOG_ERR: Literal[3]
LOG_INFO = Literal[6]
LOG_KERN: Literal[0]
LOG_LOCAL0: Literal[128]
LOG_LOCAL1: Literal[136]
LOG_LOCAL2: Literal[144]
LOG_LOCAL3: Literal[152]
LOG_LOCAL4: Literal[160]
LOG_LOCAL5: Literal[168]
LOG_LOCAL6: Literal[176]
LOG_LOCAL7: Literal[184]
LOG_LPR: Literal[48]
LOG_MAIL: Literal[16]
LOG_NDELAY: Literal[8]
LOG_NEWS: Literal[56]
LOG_NOTICE: Literal[5]
LOG_NOWAIT: Literal[16]
LOG_ODELAY: Literal[4]
LOG_PERROR: Literal[32]
LOG_PID: Literal[1]
LOG_SYSLOG: Literal[40]
LOG_USER: Literal[8]
LOG_UUCP: Literal[64]
LOG_WARNING: Literal[4]
def LOG_MASK(a: int) -> int: ...
def LOG_UPTO(a: int) -> int: ...
def closelog() -> None: ...
def openlog(ident: str = ..., logoption: int = ..., facility: int = ...) -> None: ...
def setlogmask(x: int) -> int: ...
@overload
def syslog(priority: int, message: str) -> None: ...
@overload
def syslog(message: str) -> None: ...
