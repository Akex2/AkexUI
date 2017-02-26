#! /usr/bin/env python
import json
import pycurl
class Printer:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.x = 0
        self.y = 0
    
    def _post_data(self, endpoint, data):
        endpoint_url = "%s/%s" % (self.url, endpoint)
        c = pycurl.Curl()
        c.setopt(pycurl.URL, endpoint_url)
        c.setopt(pycurl.HTTPHEADER, ["Content-Type: application/json", "X-Api-Key: %s" % self.key])
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, data)
        print("Posting data %s to %s" % (data, endpoint_url))
        c.perform()
        
 
    def cmd(self, cmd):
        data = json.dumps(dict({"command": cmd}))
        self._post_data('api/printer/command', data)

    def cmd2(self, cmd):
        data = json.dumps(dict({"command": cmd}))
        self._post_data('api/job', data)

    def cmd3(self, cmd):
        data = json.dumps(dict({"command": "pause", "action": cmd}))
        self._post_data('api/job', data)

    def selectP(self, gcodeselect):
        data = json.dumps(dict({"command": "select", "print": "true"}))
        self._post_data('api/files/local/%s' % (gcodeselect), data)

    def select(self, gcodeselect):
        data = json.dumps(dict({"command": "select", "print": "false"}))
        self._post_data('api/files/local/%s' % (gcodeselect), data)

    def connect(self):
        data = json.dumps(dict({"command": "connect", "autoconnect": "true"}))
        self._post_data('/api/connection', data)

    def disconnect(self):
        data = json.dumps(dict({"command": "disconnect"}))
        self._post_data('/api/connection', data)

    def timelaps(self, typeT, postRoll, fps, zhop):
        if typeT == "zchange":  
            data = json.dumps(dict({"type": "%s"%typeT, "postRoll": "%i"%postRoll, "fps": "%i"%fps,  "retractionZHop": "%i"%zhop}))
        if typeT == "timed": 
            data = json.dumps(dict({"type": "%s"%typeT, "postRoll": "%i"%postRoll, "fps": "%i"%fps,  "interval": "%i"%zhop}))
        if typeT == "off": 
            data = json.dumps(dict({"type": "%s"%typeT}))

        self._post_data('/api/timelapse', data)