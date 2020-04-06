#python获取windows管理员权限
#会弹出uac界面
from __future__ import print_function
import ctypes, sys
import subprocess
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    # 将要运行的代码加到这里
    a = subprocess.call('net start mysql',shell=True)
    print(a)
else:
    if sys.version_info[0] == 3:
    	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)