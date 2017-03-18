#! /usr/bin/env python
import urllib2
import json

class lista:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.x = 0
        self.y = 0

    def liste(self, endpoint):
		endpoint_url = "%s/%s" % (self.url, endpoint)
		#print endpoint_url
		#xapikey = '054E508852624649B8B250B341CFF639'
		les_headers = {'Content-Type': 'text/html', 'X-Api-Key': self.key }
		#les_headers = {'Content-Type': 'text/html', xapikey}
		req = urllib2.Request(endpoint_url,headers=les_headers)
		#url='http://127.0.0.1:5000/api/printer'
		#req = urllib2.Request(url,headers={"Content-Type": "text/html",xapikey})
		#contents = urllib2.urlopen(req).read()
		res = urllib2.urlopen(req)
		resultat = json.load(res)
		#print contents
		return resultat