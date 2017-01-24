#!/usr/bin/python3
import caly_caldav_ical
import json 
"""
with open('key.json') as json_data:
    d = json.load(json_data)
    userId = d['naver']['id']
    userPw = d['naver']['pw']
"""

userId="-"
userPw="-"

client = caly_caldav_ical.CaldavClient(
	"iCal",
    userId,
    userPw
)

client.getPrincipal()
client.getTopCalendarID()
client.getAllCalendarID()