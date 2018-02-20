from wit import Wit
import requests
from flask import Flask, request, redirect, render_template, make_response, abort, jsonify
import json
import os

access_token = os.environ["ACCESS_TOKEN"]

client = Wit(access_token = access_token)

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def index():
	
	message_text = request.form['input']

	response = client.message(message_text)
	respList = []
		
	for key, val in response['entities'].items():
		if len(val)>0:
			respList.append({'entityType':key,'entityValue': val[0]['value']})
		
	return json.dumps(respList)


if __name__ == "__main__":
	app.run()
