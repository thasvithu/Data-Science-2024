# A Sample Flask Application--Inprogress

from flask import Flask

# WSGI Application
app2 = Flask(__name__)

@app2.route("/")
def welcome():
    return "Hi... vithu how are you!"

@app2.route("/mgs")
def message():
    return "Happy Learning FLASK:)"



if __name__ == "__main__":
    app2.run(debug = True)