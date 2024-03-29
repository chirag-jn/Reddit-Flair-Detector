from flask import Flask, render_template, request
import pymongo as pym
from Scripts.testLink import fetch_data
from Scripts.predictFlair import predictflair
from trainModels import train
import nltk
app = Flask(__name__)

@app.route("/", methods=['POST'])
def results():
	# Here we are getting the URL which was submitted by the user and predicting the results for the same. 
	if request.method == 'POST':
		if 'submit_button' in request.form:
			return render_template('index.html')
		subredditurl = request.form['subredditurl']
		post_data = fetch_data(subredditurl)
		post_data['flair'] = predictflair(post_data)
		return render_template('results.html', data = post_data)

@app.route("/")
def home():
	return render_template('index.html')

if __name__ == "__main__":
	# train()
	# nltk.download('punkt')
	# nltk.download('stopwords')
	app.run(debug=True, threaded=True)