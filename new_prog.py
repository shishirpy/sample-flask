import time
import zmq

ctx = zmq.Context()
rep_socket = ctx.socket(zmq.REP)
rep_socket.bind("ipc://sample.soc")

req_socket = ctx.socket(zmq.REQ)
req_socket.connect("ipc://sample.soc")

count = 0
while True:
    req_socket.send_string(f"hi-{count}")

    msg = rep_socket.recv_string()
    print(f">>>: {msg}")
    time.sleep(1)

    rep_socket.send_string(f"bye-{count}")
    msg_req = req_socket.recv_string()
    print(f"***: {msg_req}")
    count += 1
