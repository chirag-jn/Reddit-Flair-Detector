import csv
from preProcessClass import preProcessText

subreddits = {}

processColumns = ['title', 'body', 'comments']

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
				subreddits[tag1] = []
				subreddits[tag2] = []
				subreddits[tag3] = []
				subreddits[tag4] = []
				subreddits[tag5] = []
				subreddits[tag6] = []
				subreddits[tag7] = []
				subreddits[tag8] = []
				subreddits[tag9] = []
				subreddits[tag10] = []
			else:
				subreddits[tag1].append(row[0])
				subreddits[tag2].append(row[1])
				subreddits[tag3].append(row[2])
				subreddits[tag4].append(row[3])
				subreddits[tag5].append(row[4])
				subreddits[tag6].append(row[5])
				subreddits[tag7].append(row[7])
				subreddits[tag8].append(row[8])
				subreddits[tag9].append(row[9])
				subreddits[tag10].append(row[10])
				line_count += 1

def processText():
	getData()
	# textProcessor = preProcessText()
	# for i in processColumns:
	# 	subreddits[i] = textProcessor.processTextList(subreddits[i])
		
if __name__ == '__main__':
	processText()