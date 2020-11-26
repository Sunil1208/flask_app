# Import the Flask class from the flask module
from config import get_config
from flask import Flask
from utils import DBManager

config = get_config("live")

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, World!"

# dynamic rout
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

# Flask converters

# 1.Integers
@app.route("/integer/<int:value>")
def int_type(value):
    print(value+1)
    return f"Value is {value+1}"

# 2. Float
@app.route("/float/<float:value>")
def float_type(value):
    print(value+1)
    return f"Value is, {value}"

# 3. dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return f"{value}"

# Response object
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return f"Hello, {name}! How are you?", 200
    else:
        return "Not Found", 404

if __name__ == "__main__":
    app.run()
