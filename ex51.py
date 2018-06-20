from flask import Flask
from flask import render_template

myapp = Flask(__name__)

@myapp.route("/")
def index():
     greeting = "Hello World"
     return render_template("index.html",greeting = greeting)

if __name__ == "__main__":
    myapp.run()
