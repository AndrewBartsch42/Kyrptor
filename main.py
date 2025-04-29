from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<form action=\"/action_page.php\"><input type=\"text\" id=\"fname\" name=\"fname\"></form>"
