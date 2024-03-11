from flask import Flask
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello_world():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"<h1>It is backend!</h1><p>Current time: {current_time}</p>"
    
@app.route("/current_time")
def current_time():
    now = datetime.now()
    return {
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
    }
    
if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
