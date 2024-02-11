from flask import Flask, render_template, Response
import cv2

app8 = Flask(__name__)


camera = cv2.VideoCapture('http://192.168.8.188:8080/')

@app8.route("/")
def index():
    return render_template("indexApp8.html")

def generate_frames():
    while True:
        success, frame = camera.read()
        
        if not success:
            break
        else:
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app8.route("/video")
def video():
    return Response(generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app8.run(debug=True)
