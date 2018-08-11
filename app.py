from flask import Flask, url_for, render_template
import os
import socket

# Set the directory path name as a local variable
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

@app.route("/")
def main():
    first_image = "/static/images/Virginia.png"
    second_image = "/static/images/Gonzaga.png"

    return render_template('main.html', first_image=first_image, second_image=second_image)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
