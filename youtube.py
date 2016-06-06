#!/usr/bin/env python3

import json
import petl
from pprint import pprint
from os import listdir
from os.path import isfile, join

data = {
	'dir': './data/',
	'metadata': 'json_metadata/',
	'day1': 'json_performance_day1/',
	'day2': 'json_performance_day2/'		
}

def files_in_dir(dirpath):
	return [join(dirpath,f) for f in listdir(dirpath) if isfile(join(dirpath,f))]

def read_file(filename):
	with open(filename,'r') as f:
		return json.load(f)

def load(data):
	import psycopg2
	# conn = psycopg2.connect()
	# conn.autocommit = True
	# insert data
	# conn.close

def main():
	metadata_files = files_in_dir(data['dir']+data['metadata'])
	day1 = files_in_dir(data['dir']+data['day1'])	
	day2 = files_in_dir(data['dir']+data['day2'])
	
	pprint(read_file(day1[4]))


if __name__ == '__main__':
	main()


