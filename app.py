from flask import Flask, request
from flask import render_template
import zmq

ctx = zmq.Context()
pub_socket = ctx.socket(zmq.PUB)
pub_socket.connect("ipc://sample.soc")
app = Flask(__name__)


@app.route("/")
def hello_world():
    # pub_socket.send_string(request.remote_addr)
    print(request)
    for key in dir(request):
        print(key, getattr(request, key))
        pub_socket.send_string(str(getattr(request, key)))
    return render_template("index.html")
