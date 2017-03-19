#!/usr/bin/env python

import socket
import threading
import websocket
from websocket import create_connection
import thread
import time
import uuid
import random
import json
import re
from PyQt4 import QtCore
from PyQt4.QtCore import QObject, pyqtSignal, SIGNAL
from PyQt4.uic import *
import asydtimer

class wsc(QObject):
    """
    A single connection (client) of the program
    """
    
    def __init__(self,worker):
        #threading.Thread.__init__(self)
        self.Qtsignal = worker
        #self.worker = asydtimer.myWorker()
        url = "ws://127.0.0.1:5000/sockjs/{:0>3d}/{}/websocket".format(random.randrange(0, stop=999), uuid.uuid4() )
        websocket.enableTrace(True)
        #self.ws = create_connection(url)
        ws = websocket.WebSocketApp(url,on_message = self.on_message)
        self.inc=0
        self.cmd ="josef"
        #ws = websocket.WebSocketApp("ws://echo.websocket.org/", on_message = on_message, on_close = on_close)
        wst = threading.Thread(target=ws.run_forever)
        wst.daemon = True
        wst.start()
        

    def on_message(self,ws, message):
        message_body = message[1:]
    #print message_body
    #nmessage = message_body["current"]
        #time.sleep(0.1)
        self.retour(message)
    #print nmessage

    def setcmd(self, ncmd): 
        #thread.start_new_thread(run, ())
        self.cmd = ncmd
        print ncmd

    
    #print message_body
    def retour(self, retour):
        a = retour[1:]
        cmd = self.cmd
        #data = json.loads(retour)
        #time.sleep(0.1)

        try:
            data = json.loads(a)
            b = data[0]['current']['logs'][0]
            #c = data[0]['current']
        #print c
        #c = b[0:10]
        #c = data[0]['current']['logs']['Recv']
        #if not b == "M105":
            #print c
    #nmessage = demjson.decode(a, strict=False)
        #nmessage = message[2]
    #print data
        #print c

            re1='(Send)'    # Word 1
            re2='(:)'   # Any Single Character 1
            re3='( )'   # Any Single Character 2
            re4='(M)'   # Any Single Character 3
            re5='(1)'   # Any Single Character 4
            re6='(0)'   # Any Single Character 5
            re7='(5)'   # Any Single Character 6
            re17='(%s)'%cmd
            re8='(Recv)'    # Word 1
            re9='(:)'   # Any Single Character 1
            re10='( )'  # Any Single Character 2
            re11='(o)'  # Any Single Character 3
            re12='(k)'  # Any Single Character 4
            re13='( )'  # Any Single Character 5
            re14='(T)'  # Any Single Character 6
            re15='$'
            re16='(  )'
            #rg = re.compile(re1+re2+re3+re4+re5+re6+re7,re.IGNORECASE|re.DOTALL)
            rg = re.compile(re1+re2+re3+re17,re.IGNORECASE|re.DOTALL)#m = rg.search(b)
            m = rg.match(b)
            #rg2 = re.compile(re8+re9+re10+re11+re12+re13+re14,re.IGNORECASE|re.DOTALL)
            #m2 = rg2.match(b)
            #rg3 = re.compile(re8+re9+re16+re11+re12+re13+re14,re.IGNORECASE|re.DOTALL)
           # m3 = rg3.match(b)
            #print m2
            #if (m3 is not None) or (m2 is not None) or (m is not None) :
            #    pass
            if (m is not None) or (self.inc) == 1 :
                if self.inc == 1 :
                    print b
                    self.inc=0
                    print "deuxieme boucle"
                    #print (type(b))
                    #b= "alex"
                    self.Qtsignal.someFunction(str(b))
                    #time.sleep(0.2)
                    
                if (self.inc == 0) and (m is not None) :                   
                    print b
                    self.inc = 1
                    print "premiere boucle"
                    self.akex.someFunction(str(b))
                    
                else :
                    pass

            else :
                pass
        except:
            pass
            
