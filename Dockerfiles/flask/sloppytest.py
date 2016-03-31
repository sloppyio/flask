from flask import Flask
from flask import render_template
from flask import request

import os

app = Flask(__name__)

@app.route('/')
def hello_world():  
		try:
			return render_template('sloppy.html',message=os.environ['MESSAGE'],backend=os.environ['URIBACKEND'],header=request.headers)

		except KeyError as e:
			return 'You have to set two environment variables: MESSAGE and URIBACKEND' 

if __name__ == '__main__':
		app.run(host='0.0.0.0',debug=True)
