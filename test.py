from flask import Flask
from markupsafe import escape
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

@app.route('/<input>')
def res(input):
    return {
        "res" : input,
    }
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)