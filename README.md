Python code for Twinleaf VMR sensor
======================================

Who should use this?
---------------------
For Windows users where Python libraries provided by Twinleaf do not work properly.
Connection to the VMR is obtained over serial interface in ascii mode that ***permits 100 Hz data flow***.

Python tools
--------------------
We use `pyqtgraph` to present data to a user. It is much faster than `matplotlib`.

GUI is designed with `PyQt5`.
With `QThreadPool` and `QtWorker` serial data parsing is performed in separate thread.

Features
--------------

- read data from the sensor
- display last 10 s of the data
- save data chunk show on the display

### To do
- save data continuously
- report lost data batches 
- bugfix
- better error reporting
