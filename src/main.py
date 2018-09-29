#flask imports
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

from helpers.configurations import configurations
from modules.healthmodule import healthmodule

app = FlaskAPI(__name__)

configs = configurations()

@app.route(configs.getHealthUrl() + '/check', methods=['GET'])
def heartbeat():
    try:
        #TODO: refien result logic
        res = healthmodule().getVersion()
        if res is not None:
            return res, 200
        return {"message":"Error Processing Request"}, 500
    except:
        print('An error occured processing this request')

if __name__ == "__main__":
    app.run(debug=True)