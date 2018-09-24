#routes
from router import Routes

#flask imports
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

rtes = Routes()

@app.route(rtes.returnDiagnosticsUrl() + '/check', methods=['GET'])
def heartbeat():
    try:
        #TODO: refien result logic
        res = rtes.getVers()
        if res is not None:
            return res, 200
        return {"message":"Error Processing Request"}, 500
    except:
        print('An error occured processing this request')

if __name__ == "__main__":
    app.run(debug=True)