"""Cloud Foundry Application"""

from flask import Flask

import os

app = Flask(__name__)

port = int(os.getenv("VCAP_APP_PORT"))

@app.route('/')
def hola_world():
	return 'Hello Python'

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=port)
