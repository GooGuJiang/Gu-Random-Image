from flask import Flask, jsonify,redirect
import os
import requests
import json
import time

def fileTime(file):
    return [
        time.ctime(os.path.getatime(file)),
        time.ctime(os.path.getmtime(file)),
        time.ctime(os.path.getctime(file))
    ]

def main_json():
    if os.path.isfile('./github.json') == False:
        jsonfile = open('./github.json','w')
        jsonfile.close()
    else:
        print(fileTime('./github.json'))


app = Flask(__name__)


@app.route('/')
def index():
    main_json()
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/json')
def imgjson():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
