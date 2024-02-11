from flask import Flask, redirect, url_for, render_template, request

app5 = Flask(__name__)

@app5.route("/")
def welcome():
    return render_template("indexApp7.html") 

if __name__ == "__main__":
    app5.run(debug = True)