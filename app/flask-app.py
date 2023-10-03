from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def  home():
    return "Hello, this is my flask application.\r\nServing you from " + socket.gethostname()

if __name__ == "__main__":
    app.run(debug=True)
