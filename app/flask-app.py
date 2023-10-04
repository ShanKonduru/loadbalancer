from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def  home():
    # Get the hostname
    hostname = socket.gethostname()

    # Define the HTML template
    html_page = f"""
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
    return html_page;

if __name__ == "__main__":
    app.run(debug=True)
