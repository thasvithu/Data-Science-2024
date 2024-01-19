#Jinja2 Template engine
""" 
{%...%} statements, for loops
{{   }} expression to print output
{#...#} this is for comments
"""

from flask import Flask, redirect, url_for, render_template, request


app6 = Flask(__name__) 

@app6.route("/")
def welcome():
    return render_template("index.html") 

#Result checker submit HTML page
@app6.route("/submit", methods = ["POST", "GET"])
def sumbit():
    total_score = 0
    if request.method == "POST":
        science = int(request.form["science"]) #give the name value in your hrml
        maths = int(request.form["maths"])
        c = int(request.form["c"])
        dataScience = int(request.form["datascience"])
        
        avg_score = (science + maths + c + dataScience) / 4

    return render_template("resultApp6.html", result = avg_score)


if __name__ == "__main__":
    app6.run(debug = True)