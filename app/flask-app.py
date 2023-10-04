from flask import Flask
import socket

html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Application</title>
</head>
<body>
    <h1>Hello, this is my Flask application.</h1>
    <p>Serving you from: <strong>{hostname}</strong></p>
</body>
</html>
"""

app = Flask(__name__)

@app.route("/")
def  home():
    # Replace {hostname} with the actual hostname
    html_page = html_page.format(hostname=socket.gethostname())
    return html_page;

if __name__ == "__main__":
    app.run(debug=True)
