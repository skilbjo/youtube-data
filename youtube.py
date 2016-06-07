#!/usr/bin/env python3

import json
from pprint import pprint
from os import listdir
from os.path import isfile, join

data = {
	'dir': './data/',
	'metadata': 'json_metadata/',
	'day1': 'json_performance_day1/',
	'day2': 'json_performance_day2/'		
}

def extract(files):
	for file in files:
		return read_file(file)['items']

def files_in_dir(dirpath):
	return [join(dirpath,f) for f in listdir(dirpath) if isfile(join(dirpath,f))]

def read_file(filename):
	with open(filename,'r') as f:
		return json.load(f)

def transform(data,dataset):
	result = []
	for record in data:
		result.append({
			'dataset': dataset,
			'video_id': record['id'],
			'comments': record['statistics']['commentCount'],
			'favorites': record['statistics']['favoriteCount'],
			'likes': record['statistics']['likeCount'],
			'dislikes': record['statistics']['dislikeCount'],				
			'views': record['statistics']['viewCount'],
			'publishedAt': record['snippet']['publishedAt'],
			'channelId': record['snippet']['channelId'],
			'title': record['snippet']['title']
		})
	return result

def transform_metadata(data,dataset):
	result = []
	for record in data:
		# result.append(record)
		result.append({
			'video_id': record['id']['videoId'],
			'title': record['snippet']['title'],
			'publishedAt': record['snippet']['publishedAt'],
			'channelId': record['snippet']['description'],
			'channelTitle': record['snippet']['channelTitle']
			})
	return result	

def load(data):
	import psycopg2
	# conn = psycopg2.connect()
	# conn.autocommit = True
	# insert data
	# conn.close

def main():
	metadata_files = files_in_dir(data['dir']+data['metadata'])
	day1_files = files_in_dir(data['dir']+data['day1'])	
	day2_files = files_in_dir(data['dir']+data['day2'])
	
	day1 = extract(day1_files)
	day2 = extract(day2_files)
	metadata = extract(metadata_files)

	day1 = transform(day1,'day1')
	day1 = transform(day2,'day2')
	metadata = transform_metadata(metadata,'metadata')

	## Use this to test {develop}; delete this line when you`re finished
	pprint(metadata)

	## After happy with how the transform looks, pass day1, day2, and metadata variables 
	## to your load() function that will handle the postgres inserts. 
	## load(day1)
	## load(day2)
	## load(metadata)

	pprint('Import process finished. Now switching to SQL for data analysis...')

if __name__ == '__main__':
	main()





