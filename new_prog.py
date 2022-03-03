import time
import zmq

ctx = zmq.Context()
sub_socket = ctx.socket(zmq.SUB)
sub_socket.bind("ipc://sample.soc")
sub_socket.setsockopt_string(zmq.SUBSCRIBE, "")


count = 0
while True:
    msg = sub_socket.recv_string()
    print(f"{msg}")
    count += 1
