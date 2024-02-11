#Integrate HTML with Flask
#HTTP verb GET and POST

from flask import Flask, redirect, url_for, render_template, request

app5 = Flask(__name__)

@app5.route("/")
def welcome():
    return render_template("index.html") 

#Result checker submit HTML page
@app5.route("/submit", methods = ["POST", "GET"])
def sumbit():
    total_score = 0
    if request.method == "POST":
        science = int(request.form["science"]) #give the name value in your hrml
        maths = int(request.form["maths"])
        c = int(request.form["c"])
        dataScience = int(request.form["datascience"])
        
        total_score = (science + maths + c + dataScience) / 4

    res = ""
    
    if total_score >= 50:
        res = "PASS"
    else:
       res = "FAIL"
       
       
    return render_template("result.html", result = res)


if __name__ == "__main__":
    app5.run(debug = True)