from flask import Flask, url_for, render_template
import os
import socket

from server import get_random_image_set

# Set the directory path name as a local variable
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

def _get_static_url(path):
    # return os.path.relpath(path)
    return path

@app.route("/")
def main():
    first_image, second_image = get_random_image_set(2, [])
    first_image = _get_static_url(first_image)
    second_image = _get_static_url(second_image)
    return render_template('main.html', first_image=first_image, second_image=second_image)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
