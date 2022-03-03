import random
from flask import Flask, request
from flask import render_template
import zmq

ctx = zmq.Context()
pub_socket = ctx.socket(zmq.PUB)
pub_socket.connect("ipc://sample.soc")
app = Flask(__name__)


@app.route("/")
def hello_world():
    pub_socket.send_string(":::".join([request.remote_addr, str(random.randint(0, 100000))]))
    return render_template("index.html")
