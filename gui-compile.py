"""
Convert ui into py file
"""

import os
path_to_pyuic5 = "C:\\Users\\Zoran\\Anaconda3\\Library\\bin\\pyuic5"
cmd = path_to_pyuic5 + " gui.ui -o gui.py"
os.system(cmd)
