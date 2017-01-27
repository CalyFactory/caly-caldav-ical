#!/usr/bin/python3
import caly_client
import json 

def tmp_login():
	with open('key.json') as json_data:
	    d = json.load(json_data)
	    userId = d['iCal']['id']
	    userPw = d['iCal']['pw']

	client = caly_client.CaldavClient(
		"iCal",
	    userId,
	    userPw
	)
	client.getAllCalendarEvent()
	#client.
	return client.getCalSet()

tmp_login()