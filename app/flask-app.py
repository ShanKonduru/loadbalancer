from flask import Flask, render_template, render_template_string
import socket

app = Flask(__name__)

@app.route("/")
def home():
    try:
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
        return render_template_string(html_page)
    except Exception as e:
        # Handle exceptions and display an error page
        error_message = "My apologies, currently the servers are down. Please try again after some time."
        return render_template("error.html", error_message=error_message), 502

if __name__ == "__main__":
    app.run(debug=True)
