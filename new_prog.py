import time
import zmq

ctx = zmq.Context()
socket = ctx.socket(zmq.REP)
socket.bind("ipc://sample.soc")

while True:
    for i in range(100):
        time.sleep(1)
        print(i)