from flask import Flask

app3 = Flask(__name__)

@app3.route("/")
def test():
    print("Sucess!")
    return "Hello Flask :)"

if __name__ == "__main__":
    app3.run(debug = True)