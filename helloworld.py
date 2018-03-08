
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    #port = 5000

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
