#! /usr/bin/env python
import urllib2
import json
def liste(url, xapikey):
	xapikey = '054E508852624649B8B250B341CFF639'
	les_headers = {'Content-Type': 'text/html', 'X-Api-Key': xapikey }
	#les_headers = {'Content-Type': 'text/html', xapikey}
	req = urllib2.Request(url,headers=les_headers)
	#url='http://127.0.0.1:5000/api/printer'
	#req = urllib2.Request(url,headers={"Content-Type": "text/html",xapikey})
	#contents = urllib2.urlopen(req).read()
	res = urllib2.urlopen(req)
	resultat = json.load(res)
	#print contents
	return resultat
