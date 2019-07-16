import pymongo as pym
import dns
import redditKeys as rkey
import csv

subreddits = []

def getData():
	global subreddits
	with open('Data/reddit_flair_data.csv', 'r') as data_file:
		data_reader = csv.reader(data_file, delimiter=',')
		line_count = 0
		tag1=''
		tag2=''
		tag3=''
		tag4=''
		tag5=''
		tag6=''
		tag7=''
		tag8=''
		tag9=''
		tag10=''
		for row in data_reader:
			if line_count == 0:
				tag1 = row[0]
				tag2 = row[1]
				tag3 = row[2]
				tag4 = row[3]
				tag5 = row[4]
				tag6 = row[5]
				tag7 = row[7]				
				tag8 = row[8]				
				tag9 = row[9]				
				tag10 = row[10]				
				line_count += 1
			else:
				tempDict = {tag1:row[0], tag2:row[1], tag3:row[2], tag4:row[3], tag5:row[4], tag6:row[5], tag7:row[7], tag8:row[8], tag9:row[9], tag10:row[10]}
				subreddits.append(tempDict)
				line_count += 1

def setupDB():
	global subreddits

	getData()
	url = 'mongodb+srv://' + rkey.mongoDB_Username + ':' + rkey.mongoDB_pass + '@redditflaircluster-jakts.mongodb.net/test?retryWrites=true&w=majority'
	myClient = pym.MongoClient(url)
	redditDB = myClient["redditflair"]
	subredditDB = redditDB["subreddits"]

	for i in range(len(subreddits)):
		print("Inserting Data: " + str(i))
		subredditDB.insert_one(subreddits[i])

if __name__=='__main__':
	setupDB()