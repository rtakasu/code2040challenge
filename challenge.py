# Rafael Takasu
# Code 2040 API Challenge
# 11/12/15

import requests
import json
import ast
import datetime
import time

#Part 0 - get token

data = {'email': 'rgt2108@columbia.edu', 'github': 'https://github.com/rtakasu/code2040challenge.git'}

r = requests.post('http://challenge.code2040.org/api/register', json.dumps(data))

result = json.loads(r.text)

token = result["result"]

print token

#Part 1

data = {'token': token}

r = requests.post('http://challenge.code2040.org/api/getstring', json.dumps(data))

result = json.loads(r.text)

input_string = result["result"]

reversed_string = input_string[::-1]

data = {'token': token, 'string': reversed_string}

r = requests.post('http://challenge.code2040.org/api/validatestring', json.dumps(data))

print r.text

#Part 2

data = {'token': token}

r = requests.post('http://challenge.code2040.org/api/haystack', json.dumps(data))

result = json.loads(r.text)

needle = result["result"]["needle"]
haystack = result["result"]["haystack"]

for i in range(len(haystack)):
	if haystack[i] == needle:
		index = i

data = {'token': token, 'needle': index}

r = requests.post('http://challenge.code2040.org/api/validateneedle', json.dumps(data))

print r.text

#Part 3

data = {'token': token}

r = requests.post('http://challenge.code2040.org/api/prefix', json.dumps(data))

print r.text

result = json.loads(r.text)

prefix = result["result"]["prefix"]
array = result["result"]["array"]

length_of_prefix = len(prefix)

for string in array:
	if string[0:length_of_prefix] == prefix:
		array.remove(string)

data = {'token': token, 'array':array}

r = requests.post('http://challenge.code2040.org/api/validateprefix', json.dumps(data))

print r.text

#Part 4

data = {'token': token}

r = requests.post('http://challenge.code2040.org/api/time', json.dumps(data))

result = json.loads(r.text)

# get inputs
input_time = result["result"]["datestamp"]
input_interval = result["result"]["interval"]

# make date object and convert it to seconds
date_object = datetime.datetime.strptime(input_time, "%Y-%m-%dT%H:%M:%S.%fZ")
input_time_seconds = time.mktime(date_object.timetuple())

# add interval to input time
input_time_seconds += input_interval

# transform the date back into ISO 8601
date_object = datetime.datetime.fromtimestamp(input_time_seconds)
datestamp = datetime.datetime.strptime(str(date_object), "%Y-%m-%d %H:%M:%S")
iso_output_time = datestamp.isoformat()
iso_output_time = iso_output_time + ".000Z"

data = {'token': token, 'datestamp': iso_output_time}

r = requests.post('http://challenge.code2040.org/api/validatetime', json.dumps(data))

print r.text




