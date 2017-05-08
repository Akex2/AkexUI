#!/usr/bin/env python
# encoding: utf-8:

import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *
import random
import uuid
import time
from PyQt4 import QtWebKit
from PyQt4 import QtGui, QtCore
import json
import command
import rempPrototest
import trav
import alist
import numpy as np
import pyqtgraph as pg
import server2
import socket
import threading
import websocket
import yaml



class GetTemp(QObject):
    message = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)
        # self.message = pyqtSignal(str)

    def get_value_printer(self):
        #data = self.datalist.liste('api/printer')
        #data = {'bed': str(random.randint(50, 60)),
        #        'tool0': str(random.randint(180, 220))}
        self.message.emit()

    def get_value_job(self):
        #data = {'bed': str(random.randint(50, 60)),
        #        'tool0': str(random.randint(180, 220))}
        self.message.emit()

    def get_value_connect(self):       
        #data = {'bed': str(random.randint(50, 60)),
        #        'tool0': str(random.randint(180, 220))}
        self.message.emit()


class Example(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QMessageBox.__init__(self)

        msgBox = QtGui.QMessageBox()
        msgBox.resize(500, 300)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText('Etes vous sûr?')
        msgBox.addButton(QtGui.QPushButton('Oui'), QtGui.QMessageBox.YesRole)
        msgBox.addButton(QtGui.QPushButton('Non'), QtGui.QMessageBox.NoRole)
        ret = msgBox.exec_()
        msgBox.resize(500, 300)
        msgBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        return ret

class myWorker(QtCore.QThread):
    mySignal = QtCore.pyqtSignal(QtCore.QString)
    #def __init__(self, parent=None):
    #    alex = MainDialog()

    # Register the signal as a class variable first
    #alex = MainDialog()
    # init and other stuff...
    def someFunction(self, msg):
        #print type(msg)
        #print msg
        #print "boucle somefuction in asyd file"
        #time.sleep(0.1)
        #alex = MainDialog()
        #self.alex.retourterminal(msg)
        #....
        # emit the signal with the parameter
        self.mySignal.emit(msg)


#class App(QMainWindow): #(QtGui.QTabWidget, prototest.Ui_TabWidget):
class MainDialog(QtGui.QFrame, rempPrototest.Ui_Frame):
    def __init__(self,parent=None):
        super(MainDialog,self).__init__(parent)
        QtGui.QTabWidget.__init__(self)
        # Charge de la définition de l'UI depuis le fichier produit par le designer
        #self.ui = loadUi("example.ui")
        #self.ui.show()

        #self.lazy = lazyworker()
        #self.lazy.message.connect(self.updateUI)

        # Création d'une instance de GetTemp
        self.get_printer = GetTemp()
        # On connecte le message émis par GetTemp à la méthode update_temp
        self.get_printer.message.connect(self.update_temp)

        # Créatiion d'un QTimer
        self.timer = QTimer()
        # Choix de l'intervalle
        self.timer.setInterval(2000)
        # On appelle la méthode get_value_printer de l'instance de GetStatus quand le timer arrive à expiration
        self.timer.timeout.connect(self.get_printer.get_value_printer)
        # Démarrage du timer
        self.timer.start()


        self.get_job = GetTemp()
        # On connecte le message émis par GetTemp à la méthode update_temp
        self.get_job.message.connect(self.update_job)

        # Créatiion d'un QTimer
        self.timer2 = QTimer()
        # Choix de l'intervalle
        self.timer2.setInterval(5000)
        # On appelle la méthode get_value_printer de l'instance de GetStatus quand le timer arrive à expiration
        self.timer2.timeout.connect(self.get_job.get_value_job)
        # Démarrage du timer
        self.timer2.start()

        self.get_etat = GetTemp()
        # On connecte le message émis par GetTemp à la méthode update_temp
        self.get_etat.message.connect(self.update_etat)

        self.timer3 = QTimer()
        # Choix de l'intervalle
        self.timer3.setInterval(5000)
        # On appelle la méthode get_value_printer de l'instance de GetStatus quand le timer arrive à expiration
        self.timer3.timeout.connect(self.get_etat.get_value_connect)
        # Démarrage du timer
        self.timer3.start()

        ##########TEST PYQTSIGNAL
        
        #self.akex = server2.Pot()
        #self.wsc= server2.wsc()
        #self.connect(self.akex, (SIGNAL("clicked()")), self.retourterminal)
        #self.akex.eventterminal.connect(self.retourterminal)
        #self.lazy = lazyworker()
        #self.lazy.message.connect(self.updateUI)
        #self.connect(lazyworker.doWork, SIGNAL("alex()"),self.updateUI)
        #tl = lazyworker()
        #self.connect(tl, SIGNAL("update(int)"), self.updateUI)
        #tl.doWork()

        with open('/usr/src/AkexUI/akexUI.yaml', 'r') as f:
            doc = yaml.load(f)
        url = doc["Octoprint"]["url"]
        apikey = doc["Octoprint"]["apikey"]
        self.speed = doc ["Printer"]["speed"]

        #import command
        #import trav
        #pg.setConfigOption('background', 'w') #before loading widget
        #plt=self.plot
        #curve = plt.plot()
        
        #win = pyqtgraph.GraphicsWindow(title="Basic plotting examples")
        #p1 = self.graphicsView.addPlot()
        #curve1 = p1.plot()
        #p1 = win.addPlot(title="Basic array plotting", y=np.random.normal(size=100))


        #super(MainDialog,self).__init__(parent)
        self.setupUi(self)

        #self.pb.clicked.connect(self.pbClicked)
        #self.pb2.clicked.connect(self.pb2Clicked)

        ####Onglet connexion
        self.BConnect.clicked.connect(self.BConnectClicked)
        self.BDisconect.clicked.connect(self.BDisconectClicked) #BConectRafr
        self.BConectRafr.clicked.connect(self.BConectRafrClicked) #BConectRafr

        self.PBReboot.clicked.connect(self.PBRebootClicked)
        self.PBArret.clicked.connect(self.PBArretClicked)

        ####Onglet Print
        self.BLoadPrint.clicked.connect(self.BLoadClicked)
        self.BPrint.clicked.connect(self.BPrintClicked)

        self.BRafrGcode.clicked.connect(self.BRafrGcodeClicked)
        #icon2 = QtGui.QIcon()
        #icon2.addPixmap(QtGui.QPixmap("glyphicons_082.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.BRafrGcode.setIcon(icon2);
        self.BPlay.clicked.connect(self.BPlayClicked)
        self.BPause.clicked.connect(self.BPauseClicked)
        self.BStop.clicked.connect(self.BStopClicked)

        ###Onglet Temperature
        self.BSetExtru.clicked.connect(self.BSetExtruClicked)
        self.BSetBed.clicked.connect(self.BSetBedClicked) #PBExtruOff

        self.PBExtruOff.clicked.connect(self.PBExtruOffClicked) #PBExtruOff
        self.PBBedOff.clicked.connect(self.PBBedOffClicked)

        #Gaph
        plt=self.plot
        plt.setYRange(15, 250)
        plt.setXRange(5, 0.6)
        plt.setLabel('bottom', "Time", "min")
        plt.setLabel('left', "Temp", "°")
        plt.addLegend()
        p1 = plt.plot(name='Extru1')
        p1.setPen(color=(0,0,255), width=5.0)
        #p1.set_title("EX0")
        p2 = plt.plot(name='Bed')
        p2.setPen(color=(255,0,0), width=5.0)
        #style = pg.PlotDataItem(pen='y')
        #plt.addItem(l, "maximum value")
        #plt.setXLimits(50)
        #plt.plot(int(10),int(20))
        #X = 100
        #Y =50
        #x = np.arange(1000)
        #y = np.random.normal(size=1000)
        #plt.plot(x, y)

        ###Onglet Controle
        #increment mouvement
        self.BZZU.clicked.connect(self.BzzuClicked)
        self.BZU.clicked.connect(self.BZUClicked)
        self.BU.clicked.connect(self.BUClicked)
        self.BD.clicked.connect(self.BDClicked)
        self.BC.clicked.connect(self.BCClicked)
        #Axes + -
        self.BX.clicked.connect(self.BXClicked)
        self.BY.clicked.connect(self.BYClicked)
        self.BZ.clicked.connect(self.BZClicked)

        self.BX_2.clicked.connect(self.BXMClicked)
        self.BY_2.clicked.connect(self.BYMClicked)
        self.BZ_2.clicked.connect(self.BZMClicked)

        #Home Axes
        self.BHX.clicked.connect(self.BHXClicked)
        self.BHY.clicked.connect(self.BHYClicked)
        self.BHZ.clicked.connect(self.BHZClicked)

        self.BMotor.clicked.connect(self.BMotorOffClicked)
        self.BFOFF.clicked.connect(self.BFOffClicked)
        #Slider fan vitesse flux
        self.BFan.clicked.connect(self.BFanClicked)
        self.BVitesse.clicked.connect(self.BVitesseClicked)
        self.BFlux.clicked.connect(self.BFluxClicked)

        #Extruder mouvement
        self.BExtru.clicked.connect(self.BExtruClicked)
        self.BRetra.clicked.connect(self.BRetraClicked)

        self.BEC.clicked.connect(self.BECClicked)
        self.BED.clicked.connect(self.BEDClicked)
        self.BECent.clicked.connect(self.BECentClicked)

        #ALIM
        self.PBAlimOn.clicked.connect(self.PBAlimOnClicked)
        self.PBAlimOff.clicked.connect(self.PBAlimOffClicked)

        #Slider
        self.SFan.valueChanged.connect(self.SFanChange)
        self.SVitesse.valueChanged.connect(self.SvitesseChange)
        self.SliderFlux.valueChanged.connect(self.SFluxChange)

        ###Onglet Cam
        self.BRafCam.clicked.connect(self.BRafCamClicked)
        self.CBTime.addItem("off")
        self.CBTime.addItem("zchange")
        self.CBTime.addItem("timed")

        self.BSaveTime.clicked.connect(self.BSaveTimeClicked)
        self.CBTime.currentIndexChanged.connect(self.CBTimeChanged)
        ##################################################################BOUTON SAUVER

        ###Onglet Terminale
        self.BTerminal.clicked.connect(self.BTerminalClicked)
        ###Connection event clavier QlineEdit
        self.LETerminal.clicked.connect(lambda: self.printText("LETerminal"))
        self.LETembed.clicked.connect(lambda: self.printText("LETembed"))
        self.LETemExt.clicked.connect(lambda: self.printText("LETemExt"))
        self.LEFps.clicked.connect(lambda: self.printText("LEFps"))
        self.LEDerImg.clicked.connect(lambda: self.printText("LEDerImg"))
        self.LEExtru.clicked.connect(lambda: self.printText("LEExtru")) #LEExtru
        self.LEZhop.clicked.connect(lambda: self.printText("LEZhop")) #LEExtru
        ###Clavier
        self.PBCG.clicked.connect(self.PBCGCliked)
        self.PBCM.clicked.connect(self.PBCMCliked)
        self.PBCX.clicked.connect(self.PBCXCliked)
        self.PBCY.clicked.connect(self.PBCYCliked)
        self.PBCZ.clicked.connect(self.PBCZCliked)
        self.PBCE.clicked.connect(self.PBCECliked)
        self.PBCS.clicked.connect(self.PBCSCliked)
        self.PBCF.clicked.connect(self.PBCFCliked)
        self.PBCP.clicked.connect(self.PBCPCliked)
        self.PBCI.clicked.connect(self.PBCICliked)
        self.PBCD.clicked.connect(self.PBCDCliked)
        self.PBCC.clicked.connect(self.PBCCCliked)
        self.PBCH.clicked.connect(self.PBCHCliked)
        self.PBCT.clicked.connect(self.PBCTCliked)
        
        self.PBCEspace.clicked.connect(self.PBCEspaceCliked)        
        self.PBC7.clicked.connect(self.PBC7Cliked)
        self.PBC8.clicked.connect(self.PBC8Cliked)
        self.PBC9.clicked.connect(self.PBC9Cliked)
        self.PBC4.clicked.connect(self.PBC4Cliked)
        self.PBC5.clicked.connect(self.PBC5Cliked)
        self.PBC6.clicked.connect(self.PBC6Cliked)
        self.PBC1.clicked.connect(self.PBC1Cliked)
        self.PBC2.clicked.connect(self.PBC2Cliked)
        self.PBC3.clicked.connect(self.PBC3Cliked)
        self.PBC0.clicked.connect(self.PBC0Cliked)

        self.PBCSuppr.clicked.connect(self.PBCSupprCliked)
        self.PBCDel.clicked.connect(self.PBCDelCliked)
        self.PBCEntrer.clicked.connect(self.PBCEntrerCliked)
        ###Cache clavier
        self.clavier.hide()

        ###Instanciation de myprinter au module command et a la class Printer
        self.myprinter = command.Printer(url,apikey)

        self.datalist = alist.lista(url,apikey)

        ###Instanciation de travx au module trav et a la class travel
        self.travx=trav.travel()
        self.travx1=trav.travel()
        ###Marque le depart pour le graph
        fin = time.time()
        self.travx.set_temps(fin)
        ###Remplissage de l onglet connexion etat/port list/et profile
        
        self.update_etat()
        self.RafrPorts()
        ###Remplissage de l onglet print fichier temps filament etc
        
        self.update_job()
        self.RafrFile()
        #import testlib
        #tl = lazyworker()
        #self.connect(tl, SIGNAL("update(int)"), self.updateUI)
        #tl.doWork()
        #tl.RegisterSignal(self.updateUI)
        #self.test = tl.doWork()

        self.worker = myWorker()
        # register signal to a slot
        self.worker.mySignal.connect(self.updateUI)
        #self.wsc= server2.wsc()
        self.wsc = server2.wsc(self.worker)
        #self.wsc= wsc()

    
        
        
    def InPrint(self):
        self.groupBox.setEnabled(0)
        self.TConnect.setEnabled(0)
        self.BSaveTime.setEnabled(0)
        self.BLoadPrint.setEnabled(0)
        self.BPrint.setEnabled(0)
        self.PBExtruOff.setEnabled(0)
        self.PBBedOff.setEnabled(0)

    def OutPrint(self):
        self.groupBox.setEnabled(1)
        self.TConnect.setEnabled(1)
        self.BSaveTime.setEnabled(1)
        self.BLoadPrint.setEnabled(1)
        self.BPrint.setEnabled(1)
        self.PBExtruOff.setEnabled(1)
        self.PBBedOff.setEnabled(1)

    #onglet connection
    def BConnectClicked(self):
        #self.CBport.currentText() #.text()
        #print port
        self.myprinter.connect()

    def BDisconectClicked(self): 
        port=self.CBport.currentText() #.text()
        print port
        self.myprinter.disconnect()

    def BConectRafrClicked(self):
        self.RafrPorts()
        
    def PBRebootClicked(self):
        if self.RBOcto.isChecked() == 1: 
            os.system('systemectl octoprint restart')
        if self.RBRedeem.isChecked() == 1:
            os.system('systemectl redeem restart')
        if self.RBSysteme.isChecked() == 1:
            os.system('shutdown -r now')
        else : 
            pass

    def PBArretClicked(self):
        if self.RBOcto.isChecked() == 1: 
            os.system('systemectl octoprint stop')
        if self.RBRedeem.isChecked() == 1:
            os.system('systemectl redeem stop')
        if self.RBSysteme.isChecked() == 1:
            os.system('shutdown -h now')
        else : 
            pass

    def RafrPorts(self):
        self.update_job()
        data = self.datalist.liste('api/connection')
        j = 0
        self.CBport.clear()
        while j < len(data['options']["ports"]):
            #print data
            fichier = data['options']['ports'][0]
            #fichier = data['options'][j]['ports'][0] 
            #content2['files'][j]['name']  
            #fichier = data[0]['ports'][0]
            #print fichier
            #portlist.append(fichier)
            self.CBport.addItem(fichier) 
            j = j + 1

    #Onglet Print
    def BLoadClicked(self):
        #command.cmd('{"command": "select", "print": false}','X-Api-Key: 054E508852624649B8B250B341CFF639', 'http://127.0.0.1:5000/api/files/local/Vts.gcode')
        gcodeselect=self.LWGcode.currentItem().text()
        #print gcodeselect
        self.myprinter.select(gcodeselect)
        time.sleep(0.5)
        data = self.datalist.liste('api/job')
        self.update_job(data)
        #data = json.dumps(dict({"select", "print"":" false}))    

    def BPrintClicked(self):
        #command.cmd('{"command": "select", "print": false}','X-Api-Key: 054E508852624649B8B250B341CFF639', 'http://127.0.0.1:5000/api/files/local/Vts.gcode')
        gcodeselect=self.LWGcode.currentItem().text()
        print gcodeselect
        #data = json.dumps(dict({"select", "print"":" false}))
        self.myprinter.selectP(gcodeselect)

    def BRafrGcodeClicked(self): 
        self.RafrFile()

    def BPlayClicked(self):
        self.myprinter.cmd2("start")

    def BPauseClicked(self):
        onPause = self.ONPAUSE
        #data = alist.liste('http://127.0.0.1:5000/api/printer','054E508852624649B8B250B341CFF639')
        #onPause = data['state']['flags']['pause']
        if onPause == 1 :
            print "resume"
            self.myprinter.cmd3("resume")
        else :
            print "pause"
            self.myprinter.cmd3("pause")


    def BStopClicked(self):
        self.myprinter.cmd2("cancel")

    def RafrFile(self):
        content2 = self.datalist.liste('api/files')
        self.LWGcode.clear()
        i = 0
        j = 0
        liste_fichiers = []
        while i < len(content2['files']):
            fichier = content2['files'][i]['name']
            
            #print a
            #liste_fichiers = [ {'filename': 'toto', 'ctime': '42'}, {'filename': 'tutu', 'ctime': '43'}] par exemple
            date = content2['files'][i]['date']
            #liste_fichiers = []
            liste_fichiers.append({'filename': fichier, 'ctime': date})
            
            
            #self.oports.addItem(fichier)
            i = i + 1
            a = sorted(liste_fichiers, key=lambda x: x['ctime'],reverse=True)
            #print a
        #a = sorted(liste_fichiers, key=lambda x: 0)
        print len(a)
        while j < len(a):
            #print "fichier"
            fichier = a[j]['filename']
            self.LWGcode.addItem(fichier)
            j = j + 1
        #a = sorted(liste_fichiers, key=lambda x: x['ctime'],reverse=True)
        #print a

    #Oglet temperature
    def BSetExtruClicked(self):
        test = self.LETemExt.text()
        print test
        #self.LTemExC.setText(test) 
        self.myprinter.cmd("M104 S%s" %(test)) #A decomente pour active

    def PBExtruOffClicked(self):
        #self.LTemExC.setText("Cible :  %s" %(test)) 
        self.myprinter.cmd("M104 S0") #A decomente pour active

    def BSetBedClicked(self):
        test = self.LETembed.text()
        print test
        #self.LTemBedC.setText(test) 
        self.myprinter.cmd("M140 S%s" %(test))  #A decomente pour active

    def PBBedOffClicked(self):
        #self.LTemExC.setText("Cible :  %s" %(test)) 
        self.myprinter.cmd("M140 S0") #A decomente pour active

    

    #Onglet Control
    def BzzuClicked(self):
        self.travx.set_distance('0.01')
        #print "ok" #self.label.setText("Bonjour"+self.Edit.text())

        #command.cmd('{"command": "M107"}','X-Api-Key: 054E508852624649B8B250B341CFF639', 'http://127.0.0.1:5000/api/printer/command')

    def BZUClicked(self):
        self.travx.set_distance('0.1')
        #print "ok" #self.label.setText("Bonjour"+self.Edit.text())
        #command.cmd('{"command": "M107"}','X-Api-Key: 054E508852624649B8B250B341CFF639')

    def BUClicked(self):
        self.travx.set_distance('1')
        #print "ok" #self.label.setText("Bonjour"+self.Edit.text())
        #command.cmd('{"command": "M107"}','X-Api-Key: 054E508852624649B8B250B341CFF639')

    def BDClicked(self):
        self.travx.set_distance('10')
        #print "ok" #self.label.setText("Bonjour"+self.Edit.text())
        #command.cmd('{"command": "M107"}','X-Api-Key: 054E508852624649B8B250B341CFF639')

    def BCClicked(self):
        self.travx.set_distance('100')
        #print "ok" #self.label.setText("Bonjour"+self.Edit.text())
        #command.cmd('{"command": "M107"}','X-Api-Key: 054E508852624649B8B250B341CFF639')

    def BXClicked(self):
        travo = self.travx.get_distance()       
        self.myprinter.cmd("G91")
        self.myprinter.cmd("G1 F%s X%s" % (self.speed, travo))
        self.myprinter.cmd("G90")
        #print "G1 F%s X%s" % (self.speed, travo)
        #print self.speed, travo #self.speed, travo.aficher()

    def BXMClicked(self):
        travo = self.travx.get_distance()       
        self.myprinter.cmd("G91")
        self.myprinter.cmd("G1 F%s X-%s" % (self.speed, travo))
        self.myprinter.cmd("G90")
        #print "G1 F%s X%s" % (self.speed, travo)
        #print self.speed, travo #self.speed, travo.aficher()

    def BYClicked(self):
        travo = self.travx.get_distance()
        self.myprinter.cmd("G91")
        self.myprinter.cmd("G1 F%s Y%s" % (self.speed, travo))
        self.myprinter.cmd("G90")

    def BYMClicked(self):
        travo = self.travx.get_distance()
        self.myprinter.cmd("G91")
        self.myprinter.cmd("G1 F%s Y-%s" % (self.speed, travo))
        self.myprinter.cmd("G90")

    def BZClicked(self):
        travo = self.travx.get_distance()
        self.myprinter.cmd("G91")
        self.myprinter.cmd("G1 F%s Z%s" % (self.speed, travo))
        self.myprinter.cmd("G90")

    def BZMClicked(self):
        travo = self.travx.get_distance()
        self.myprinter.cmd("G91")
        self.myprinter.cmd("G1 F%s Z-%s" % (self.speed, travo))
        print ("G1 F%s Z-%s" % (self.speed, travo))
        self.myprinter.cmd("G90")

    def BHXClicked(self):
        print "ok" #self.label.setText("Bonjour"+self.Edit.text())
        self.myprinter.cmd("G28 X")

    def BHYClicked(self):
        self.myprinter.cmd("G28 Y")
        print "ok1" #self.label.setText("Bonjour"+self.Edit.text())

    def BHZClicked(self):
        self.myprinter.cmd("G28 X")
        print "ok2" #self.label.setText("Bonjour"+self.Edit.text())

    def BMotorOffClicked(self):
        self.myprinter.cmd("M18")

    def BExtruClicked(self):
        travo = self.LEExtru.text()
        self.myprinter.cmd("G91")
        self.myprinter.cmd("G1 F120 E%s" % (travo))
        self.myprinter.cmd("G90")

    def BRetraClicked(self):
        travo = self.LEExtru.text()
        self.myprinter.cmd("G91")
        self.myprinter.cmd("G1 F120 E-%s" % (travo))
        self.myprinter.cmd("G90")

    def BECClicked(self): 
        self.LEExtru.setText("5")

    def BEDClicked(self): 
        self.LEExtru.setText("10")

    def BECentClicked(self): 
        self.LEExtru.setText("100")

    def BFOffClicked(self):
        self.myprinter.cmd("M107")

    def BFanClicked(self):
        vitessefan=self.SFan.value()
        print vitessefan
        vitessefan = vitessefan*2.55
        print vitessefan
        self.myprinter.cmd("M106 S255")
        time.sleep(0.1)
        self.myprinter.cmd("M106 S%s" %int((vitessefan)))
        #self.myprinter.cmd("M107")

    def BVitesseClicked(self):
        vitesse=self.SVitesse.value()
        self.myprinter.cmd("M220 S%s" %(vitesse))

    def BFluxClicked(self):
        flux=self.SliderFlux.value()
        self.myprinter.cmd("M221 S%s" %(flux))

    def SFanChange(self):
        vitessefan=self.SFan.value()
        self.LTFan.setNum(int(vitessefan))

    def SvitesseChange(self):
        vitesse=self.SVitesse.value()
        self.LTVitesse.setNum(int(vitesse))

    def SFluxChange(self):
        flux= self.SliderFlux.value()
        self.LTFlux.setNum(int(flux))


    def PBAlimOnClicked(self): 
        self.myprinter.cmd("M80")

    def PBAlimOffClicked(self): 
        ex = Example()
        ex.resize(500, 300)
        ex.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        data = ex.show()
        print data
        #self.myprinter.cmd("M80")

    
    #Onglet Cam
    def BRafCamClicked(self):
        self.webView.reload()
        print "reload"

    def BSaveTimeClicked(self): 
        typeT=self.CBTime.currentText()
        fps = self.LEFps.text()
        derImg = self.LEDerImg.text()
        zhop = self.LEZhop.text()
        print typeT
        print fps
        print derImg
        self.myprinter.timelaps(typeT, int(derImg), int(fps), int(zhop))

    def CBTimeChanged(self): 
        if self.CBTime.currentText() == "zchange" : 
            self.LTime_2.setText("RetractZHop")

        if self.CBTime.currentText() == "timed" : 
            self.LTime_2.setText("Intervale")


    #Onglet Terminal
    def BTerminalClicked(self):
        test = self.LETerminal.text()
        print "entrer"
        #self.worker.someFunction("event interne")
        #self.LWTerminal.addItem(test)#("Cible :  %s" %(test))
        self.myprinter.cmd(str(test))
        self.LWTerminal.scrollToBottom()

    def updateUI(self, prog):
        print "event success"
        self.LWTerminal.addItem(prog)
        self.LWTerminal.scrollToBottom()

    def retourterminal(self, data):
        self.LWTerminal.addItem(data)
        #print "retour temrinal"
        #print data

    

    fin = 0

    #Update des temperature et du graph
    def update_temp(self):
        data = self.datalist.liste('api/printer')
        debut = time.time()
        #print data
        onPrint = data['state']['flags']['printing']
        onPause = data['state']['flags']['paused']
        self.ONPAUSE = onPause
        enabled = self.TConnect.isEnabled()
        if onPrint == 0 and self.timer2.isActive()  == 1 :
            #print "boucle if ok"
            self.timer2.stop()
        if onPrint == 1 and self.timer2.isActive() == 0 :
            #print "boucle if ok2"
            self.timer2.start()
        if onPrint == 1 and enabled == 1 and onPause == 0 :
            self.InPrint()
            #print "in print"
        if (onPrint == 0 or onPause == 1) and enabled == 0:
            self.OutPrint()
            #print "out print"
        fichier = data['temperature']['bed']['actual']
        self.LTemBed.setText("%3.1f" %(fichier))
        #print "Bed : %s" %fichier
        fichier2 = data['temperature']['tool0']['actual']
        self.LTemEx.setText("%3.1f" %(fichier2))
        #print "Extru1 : %s" %fichier2
        fin = self.travx.get_temps()
        fichier3 = data['temperature']['bed']['target']
        fichier4 = data['temperature']['tool0']['target']
        self.LTemExC.setText("Cible : %3.0f" %(fichier4))
        self.LTemBedC.setText("Cible : %3.0f" %(fichier3))
        #x,y = (int(fichier2),(int(fichier)
        #plt.plot(x,y)
        #self.ui.bedTemperature.setText(data['bed'])
        #self.ui.tool0.setText(data['tool0'])
        plt=self.plot
        plt.clear()
        plt.enableAutoRange(False, False)
        #plt.plot(int(10),int(20))
        X = 100
        Y =debut+ 5 - fin
        if Y > 100000:
            Y=0
        #print Y
        Y = Y/60
        #print fichier
        fichier2 = fichier2
        fichier = fichier
        #print Y
        #self.travx.set_listtemps(Y)
        self.travx.set_listtemperatureE(fichier2)
        self.travx.set_listtemperatureB(fichier)
        #self.travx1=trav.travel()
        self.travx1.set_listtemperatureB(fichier3)
        self.travx1.set_listtemperatureE(fichier4)
        #print Y
        #y = np.arange(fichier2)
        #x = np.arange(Y)
        #print y
        #curvePen = plt.mkPen(color=(255, 15, 10))
        #plt.clear()
        p1 = plt.plot()
        p1.setPen(color=(0,0,255), width=4.0)
        #p1.set_title("EX0")
        p2 = plt.plot()
        p2.setPen(color=(255,0,0), width=4.0)
        #cible= 50
        p3 = plt.plot()
        #p3.setPen(color=(255,143,143), width=4.0)
        p3.setPen(color=(255,0,0,120), width=4.0)
        p4 = plt.plot()
        p4.setPen(color=(0,0,255,120), width=4.0)
        #plt.plot(int(50))
        #plt.addLegend()
        #plt.plot(Y, fichier2,pen='y')
        #yd, xd = rand(10000)
        #print x
        #templist = []
        #templist.append(Y)
        #print templist
        #temperaturelist = []
        #temperaturelist.append(fichier2)
        #print temperaturelist
        #y = arr[1:-1]['y']
        #x = arr[1:-1]['x']
        #p1.setData(y=y, x=x) #arr[1:-1]['y'] = y
        #p1.setData(y=yd, x=xd)
        #yd, xd = rand(10000)
        #
        #a=np.array([1, 2, 3, 4, 5])
        #c=np.array([1, 2, 3, 4, 5])
        temps=self.travx.get_listtemps()
        extru1=self.travx.get_listtemperatureE()
        bed=self.travx.get_listtemperatureB()
        bedtarget=self.travx1.get_listtemperatureB()
        extru1target=self.travx1.get_listtemperatureE()
        #print bedtarget
        #print bed
        #temps.reverse()
        #print a
        #print c
        #plt.clearPlots()
        p1.setData(x=temps, y=extru1)
        p2.setData(x=temps, y=bed)
        p3.setData(x=temps, y=bedtarget)
        p4.setData(x=temps, y=extru1target)
        #plt.addLegend()
        #plt.clear()


        #curvePen = pg.mkPen(color=(255, 15, 10), style=QtCore.Qt.DotLine)

        # plot the curve
        
        #curve = pg.PlotCurveItem(y.shape, x.shape,pen=curvePen,stepMode=True)
        #plt.addItem(curve)
        #fin = self.travx.set_temps(debut)

    #Update etat du job
    def update_job(self):
        data = self.datalist.liste('/api/job')
        #print data
        try:

            averagePrintTime = data['job']['averagePrintTime']
        #print averagePrintTime
            if averagePrintTime > 0 :
                a = self.secTohms(int(averagePrintTime))
                self.LTEFichier.setText(a)
        except:
            pass
        try :
            length = data['job']['filament']['tool0']['length']
            length = (length/1000)
            self.LFilamentFichier.setText("%3.2f Metres"%length)
        except:
            pass

        try: 
            nameFile = data['job']['file']['name']
            self.LNomFichier.setText(nameFile)
        except:
            pass

        try:
            completion = data['progress']['completion'] #printTime
            self.progressBar.setValue(int(completion))
        except:
            pass

        try :
            printTime = data['progress']['printTime'] #printTimeLeft
            #_print printTime
            if printTime > 0 :
                #print "entrer"
                a = self.secTohms(int(printTime))
                self.LTPFichier.setText(a)
        except:
            pass
        
        try: 
            printTimeLeft = data['progress']['printTimeLeft'] #printTimeLeft
            if printTimeLeft > 0 :
                a = self.secTohms(int(printTimeLeft))
                self.LTRFichier.setText(a)
        except:
            pass

    #Conversion Sec to Heures
    def secTohms(self, nb_sec):
        q,s=divmod(nb_sec,60)
        h,m=divmod(q,60)
        return "%dh%dm%ds" %(h,m,s)

    #Update de la connection
    def update_etat(self):
        data = self.datalist.liste('/api/connection')
        etatprinteuse = data['current']['state']
        if etatprinteuse == "Closed" and self.timer.isActive() == 1 :
            #print "closed"
            self.timer.stop()
            self.timer2.stop()

        if etatprinteuse == "Closed" and self.timer2.isActive() == 1 :
            #print "closed"
            self.timer.stop()
            self.timer2.stop()

        if etatprinteuse == "Operational" and self.timer.isActive() == 0 :
            #print "operational"
            self.timer.start()
            self.timer2.start()
        #print etatprinteuse
        self.LEtatPrinteuse.setText(etatprinteuse)
        profile = data['options']['printerProfiles'][0]['name']
        #print profile
        self.LProfilePrinteuse.setText(profile)

    

    
    #Event d un touch sur un QLineEdit
    def printText(self,data):
        #print data
        self.travx.set_cible(data)
        #b = (print "alex")
        #b
        self.LEClavier.clear()
        #self.LEClavier.setText(a)
        #self.tabWidget.hide()
        self.clavier.show()
        self.clavier.raise_()

    #Clavier
    def PBCGCliked(self):
        self.LEClavier.insert("G")

    def PBCMCliked(self):
        self.LEClavier.insert("M")

    def PBCXCliked(self):
        self.LEClavier.insert("X")

    def PBCYCliked(self):
        self.LEClavier.insert("Y")

    def PBCZCliked(self):
        self.LEClavier.insert("Z")

    def PBCECliked(self):
        self.LEClavier.insert("E")

    def PBCSCliked(self):
        self.LEClavier.insert("S")

    def PBCFCliked(self):
        self.LEClavier.insert("F")

    def PBCPCliked(self):
        self.LEClavier.insert("P")

    def PBCICliked(self):
        self.LEClavier.insert("I")

    def PBCDCliked(self):
        self.LEClavier.insert("D")

    def PBCCCliked(self):
        self.LEClavier.insert("C")

    def PBCHCliked(self):
        self.LEClavier.insert("H")

    def PBCTCliked(self):
        self.LEClavier.insert("T")





    def PBCEspaceCliked(self):
        self.LEClavier.insert(" ")

    def PBC7Cliked(self):
        self.LEClavier.insert("7")

    def PBC8Cliked(self):
        self.LEClavier.insert("8")

    def PBC9Cliked(self):
        self.LEClavier.insert("9")

    def PBC4Cliked(self):
        self.LEClavier.insert("4")

    def PBC5Cliked(self):
        self.LEClavier.insert("5")

    def PBC6Cliked(self):
        self.LEClavier.insert("6")

    def PBC1Cliked(self):
        self.LEClavier.insert("1")

    def PBC2Cliked(self):
        self.LEClavier.insert("2")

    def PBC3Cliked(self):
        self.LEClavier.insert("3")

    def PBC0Cliked(self):
        self.LEClavier.insert("0")

    def PBCSupprCliked(self):
        self.LEClavier.clear()

    def PBCDelCliked(self):
        self.LEClavier.backspace()






    def PBCEntrerCliked(self):
        b = self.travx.get_cible()
        #print b
        a=self.LEClavier.text()
        self.entrerClavier(a,b)
        #self.LETerminal.setText(a)
        self.clavier.hide()
        #self.tabWidget.show()
    #Fonction pour envoyer la string au bon QLineEdit
    def entrerClavier(self, data, cible):
        if cible == "LETerminal" :
            self.LETerminal.setText(data)
            self.wsc.setcmd(data) ### a décomenté pour enable l envoie de cmd au parseur du terminale
            #self.test
            #print "ok"
        if cible == "LETemExt" :
            self.LETemExt.setText(data)
            #print "ok"
        if cible == "LETembed" :
            self.LETembed.setText(data)
            #print "ok"
        if cible == "LEFps" :
            self.LEFps.setText(data)
            #print "ok"
        if cible == "LEDerImg" :
            self.LEDerImg.setText(data)
            #print "ok"
        if cible == "LEExtru" :
            self.LEExtru.setText(data)
            #print "ok"
        if cible == "LEZhop" :
            self.LEZhop.setText(data)
            #print "ok"
        else:
            #print"not ok"
            pass
        


if __name__ == '__main__':
    #app=QtGui.QApplication(sys.argv) #app = QApplication(sys.argv)
    #win = App()
    #app.exec_()
    app=QtGui.QApplication(sys.argv) 
    form=MainDialog()
    form.show()
    app.exec_()
