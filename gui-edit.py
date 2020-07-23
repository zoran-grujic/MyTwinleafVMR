"""
Start Qt Designer to edit gui.ui file
Then run gui-compile.py to convert ui file into py
"""

import os
path_to_qtdesigner = "C:\\Users\\Zoran\\Anaconda3\\Library\\bin\\designer.exe"
cmd = "START " + path_to_qtdesigner + " gui.ui"
os.system(cmd)
