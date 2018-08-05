from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Set the directory path name as a local variable
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def main():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html_file = open(_get_html_template("main.html"), 'r')
    html = html_file.read()
    
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

def _get_html_template(filename):
    return os.path.join(ROOT_PATH, 'frontend', filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)