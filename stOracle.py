import ctypes
import subprocess
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    subprocess.run('net start OracleServiceORCL', shell=True)
    subprocess.run('net start OracleOraDB12Home1MTSRecoveryService', shell=True)
    subprocess.run('net start OracleOraDB12Home1TNSListener', shell=True)
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:  # in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
