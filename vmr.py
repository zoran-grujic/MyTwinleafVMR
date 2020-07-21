from myVMRSerial import myVMRSerial
import time

vmr = myVMRSerial()

while True:
    print(list(vmr.cbB))
    time.sleep(.009)



