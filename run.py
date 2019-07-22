from flask import Flask, render_template, request
import pymongo as pym
from Scripts.testLink import fetch_data

app = Flask(__name__)

@app.route("/", methods=['POST'])
def results():
	if request.method == 'POST':
		if 'submit_button' in request.form:
			return render_template('index.html')
		subredditurl = request.form['subredditurl']
		post_data = fetch_data(subredditurl)
		return render_template('results.html', data = post_data)

@app.route("/")
def home():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True, threaded=True)