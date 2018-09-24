#system imports
import json

#flask imports
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

base = '/api/'
diagnosticBaseUrl = base + 'health/'

@app.route(diagnosticBaseUrl + 'check', methods=['GET'])
def heartbeat():
    try:
        return {"Name":"py-seed-service", "Version":"1.0.0"}
    except:
        print('An error occured processing this request')

if __name__ == "__main__":
    app.run(debug=True)