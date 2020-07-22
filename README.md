Python code for Twinleaf VMR sensor
======================================

Serial connection in ascii mode permits only 100 Hz data stream.

We use `pyqtgraph` to plot data as fast as possible.

With `QThreadPool` and `QtWorker` serial data parsing is performed in separate thread. 