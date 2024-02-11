#Building URL dynamically
#Flask Variables Rules and URL Building

from flask import Flask, redirect, url_for

app4 = Flask(__name__)

@app4.route("/")
def welcome():
    return "Hi this is vithu"

@app4.route("/success/<int:score>")
def success(score):
    return "The person has passed, and the marks are " + str(score)

@app4.route("/fail/<int:score>")
def fail(score):
    return "The person has failed, and the marks are " + str(score)

# Result checker
@app4.route("/results/<int:marks>")
def results(marks):
    if marks < 50:
        return redirect(url_for('fail', score=marks))
    else:
        return redirect(url_for('success', score=marks))

#HTML result
@app4.route("/html")
def html():
    return "<html><body><h1><b>Hi Vithu from HTML</b></h1></body></html>"


if __name__ == "__main__":
    app4.run(debug=True)
