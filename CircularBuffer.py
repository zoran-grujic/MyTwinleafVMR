from collections import deque
from collections import Counter
import numpy as np


class CircularBuffer(deque):
    def __init__(self, size=0):
        super(CircularBuffer, self).__init__(maxlen=size)

    # @property
    def average(self):  # TODO: Make type check for integer or floats
        try:
            return np.average(list(self))

        except Exception as e:
            print("CB:average error" + str(e))
            return 1

    def std(self):
        # print(self)
        return np.std(list(self))
