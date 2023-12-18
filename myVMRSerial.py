import serial
from CircularBuffer import CircularBuffer
# import threading
import time


class myVMRSerial:
    port = ''
    ser = False
    B = []
    G = []
    A = []
    P = []
    T = []
    bufferSize = 1000
    cbB = CircularBuffer(bufferSize)
    cbG = CircularBuffer(bufferSize)
    cbA = CircularBuffer(bufferSize)
    cbP = CircularBuffer(bufferSize)
    cbT = CircularBuffer(bufferSize)

    def __init__(self, port="COM4"):
        try:
            self.ser = serial.Serial(port, 115200, timeout=.5)  # open serial port
            print(self.ser.name)
            time.sleep(.2)
            """
            self.readThread = threading.Thread(target=self.readData)
            self.readThread.setDaemon(True)
            self.ser.reset_input_buffer()
            self.readThread.start()
            """

        except Exception as e:
            print(e)
            quit(1)

    def readLine(self):
        line = self.ser.readline().decode("utf-8")[:-2]
        return line

    def getData(self):
        try:
            line = self.readLine()
            data = [float(d) for d in (line.split(" "))]
            n = int(data[0])
            dLen = len(data)
            if dLen not in [4, 10, 12]:
                print("Line = ", line)
                print("Line data length = ", dLen)
                return
            #if len(data) >= 4:
            self.setB(data[1:4])  # self.B = data[1:4]
            # print("B = ", self.B)
            if dLen == 10:
                self.setA(data[4:7])
                self.setG(data[7:11])
                # print("G = ", self.G)
                # print("A = ", self.A)
            if dLen == 12:
                self.setP(data[10])
                self.setT(data[11])
                # print("Atm. pressure: ", self.P, " mbar")
                # print("Sensor temperature ", data[11], " C")
            return self.B, self.A, self.G
        except Exception as e:
            pass

    def readData(self, progress_callback):
        while True:
            self.getData()

    def setB(self, x):
        self.B = x
        self.cbB.append(x)

    def setA(self, x):
        self.A = x
        self.cbA.append(x)

    def setG(self, x):
        self.G = x
        self.cbG.append(x)

    def setP(self, x):
        self.P = x
        self.cbP.append(x)

    def setT(self, x):
        self.T = x
        self.cbT.append(x)
