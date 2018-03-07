import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))
    
    res = makeResponse(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def makeResponse(req):
    
    result = req.get("result")
    action = result.get("action")
    parameters = result.get("parameters")
    if action != "Wetterabfrage":
        return {}
    city = parameters.get("geo-city")
    date = parameters.get("date")
    
    r = requests.get("http://samples.openweathermap.org/data/2.5/forecast?q="+city+"&appid=ecd11b887d65ca7a4464cf11f3a90528")
    json_object = r.json()
    weather = json_object["list"]
    #for i in range(0,30):
        #if date in weather[i]["dt_text"]:
            #condition = weather[i]["weather"][i][0]["description"]
    condition = weather[1]["weather"][0]["description"]
    
    speech = "Das Wetter in " + city + " am " + date + " ist " + condition
    return {
        "speech": speech,
        "displayText": speech,
        "source": "apiai-weather-webhook-sample"}
    


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')