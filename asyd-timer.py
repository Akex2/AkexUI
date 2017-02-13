#!/usr/bin/env python
# encoding: utf-8:

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *
import random
import time
from PyQt4 import QtWebKit
from PyQt4 import QtGui, QtCore
import json
import command
import prototest
import trav
import alist
import numpy as np
import pyqtgraph as pg


class GetTemp(QObject):
    message = pyqtSignal(dict)

    def __init__(self):
        QObject.__init__(self)
        # self.message = pyqtSignal(str)

    def get_values(self):
        data = alist.liste('http://127.0.0.1:5000/api/printer','054E508852624649B8B250B341CFF639')
        #data = {'bed': str(random.randint(50, 60)),
        #        'tool0': str(random.randint(180, 220))}
        self.message.emit(data)

    def get_values2(self):
        data = alist.liste('http://127.0.0.1:5000/api/job','054E508852624649B8B250B341CFF639')
        #data = {'bed': str(random.randint(50, 60)),
        #        'tool0': str(random.randint(180, 220))}
        self.message.emit(data)


#class App(QMainWindow): #(QtGui.QTabWidget, prototest.Ui_TabWidget):
class MainDialog(QtGui.QTabWidget, prototest.Ui_TabWidget):
    def __init__(self):
        #super(MainDialog,self).__init__(parent)
        QtGui.QTabWidget.__init__(self)
        # Charge de la définition de l'UI depuis le fichier produit par le designer
        #self.ui = loadUi("example.ui")
        #self.ui.show()

        # Création d'une instance de GetTemp
        self.get_status = GetTemp()
        # On connecte le message émis par GetTemp à la méthode update_temp
        self.get_status.message.connect(self.update_temp)

        # Créatiion d'un QTimer
        self.timer = QTimer()
        # Choix de l'intervalle
        self.timer.setInterval(2000)
        # On appelle la méthode get_values de l'instance de GetStatus quand le timer arrive à expiration
        self.timer.timeout.connect(self.get_status.get_values)
        # Démarrage du timer
        self.timer.start()


        self.get_status2 = GetTemp()
        # On connecte le message émis par GetTemp à la méthode update_temp
        self.get_status2.message.connect(self.update_temp2)

        # Créatiion d'un QTimer
        self.timer2 = QTimer()
        # Choix de l'intervalle
        self.timer2.setInterval(5000)
        # On appelle la méthode get_values de l'instance de GetStatus quand le timer arrive à expiration
        self.timer2.timeout.connect(self.get_status2.get_values2)
        # Démarrage du timer
        self.timer2.start()



        import command
        import trav
        pg.setConfigOption('background', 'w') #before loading widget
        #plt=self.plot
        #curve = plt.plot()
        
        #win = pyqtgraph.GraphicsWindow(title="Basic plotting examples")
        #p1 = self.graphicsView.addPlot()
        #curve1 = p1.plot()
        #p1 = win.addPlot(title="Basic array plotting", y=np.random.normal(size=100))


        #super(MainDialog,self).__init__(parent)
        self.setupUi(self)
        self.BConnect.clicked.connect(self.BConnectClicked)
        self.BDisconect.clicked.connect(self.BDisconectClicked)
        self.BZZU.clicked.connect(self.BzzuClicked)
        self.BZU.clicked.connect(self.BZUClicked)
        self.BU.clicked.connect(self.BUClicked)
        self.BD.clicked.connect(self.BDClicked)
        self.BC.clicked.connect(self.BCClicked)
        self.BX.clicked.connect(self.BXClicked)
        self.BY.clicked.connect(self.BYClicked)
        self.BZ.clicked.connect(self.BZClicked)
        self.BHX.clicked.connect(self.BHXClicked)
        self.BHY.clicked.connect(self.BHYClicked)
        self.BHZ.clicked.connect(self.BHZClicked)
        self.BLoadPrint.clicked.connect(self.BLoadClicked)
        self.BPrint.clicked.connect(self.BPrintClicked)
        self.BFOFF.clicked.connect(self.BFOffClicked)
        self.BFan.clicked.connect(self.BFanClicked)
        self.BMotor.clicked.connect(self.BMotorOffClicked)
        self.BExtru.clicked.connect(self.BExtruClicked)
        self.BRetra.clicked.connect(self.BRetraClicked)
        self.BSetExtru.clicked.connect(self.BSetExtruClicked)
        self.BSetBed.clicked.connect(self.BSetBedClicked)
        self.BRafCam.clicked.connect(self.BRafCamClicked)
        #self.BEC.clicked.connect(self.BECClicked)
        #self.BED.clicked.connect(self.BEDClicked)
        #self.BEC_2.clicked.connect(self.BEC_2Clicked)
        self.BTerminal.clicked.connect(self.BTerminalClicked)
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


        self.myprinter = command.Printer("http://127.0.0.1:5000", "054E508852624649B8B250B341CFF639")
        self.travx=trav.travel()
        fin = time.time()
        self.travx.set_temps(fin)
        content2 = alist.liste('http://127.0.0.1:5000/api/files','054E508852624649B8B250B341CFF639')
        i = 0
        j = 0
        gcodelist=[]
        portlist=[]
        while i < len(content2['files']):
            fichier = content2['files'][i]['name']
            #print fichier
            gcodelist.append(fichier)
            self.LWGcode.addItem(fichier)
            #self.oports.addItem(fichier)
            i = i + 1
        content3 = alist.liste('http://127.0.0.1:5000/api/connection','054E508852624649B8B250B341CFF639')
        while j < len(content3['options']):
            #print content3
            fichier = content3['options']['ports'][0]
            #fichier = content3['options'][j]['ports'][0] 
            #content2['files'][j]['name']  
            #fichier = content3[0]['ports'][0]
            #print fichier
            portlist.append(fichier)
            self.CBport.addItem(fichier) 
            j = j + 1


    def BConnectClicked(self):
        port=self.CBport.currentText() #.text()
        print port
        self.myprinter.connect()

    def BDisconectClicked(self):
        port=self.CBport.currentText() #.text()
        print port
        self.myprinter.disconnect()

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
        self.myprinter.cmd("G1 F5000 X-%s" % (travo))
        self.myprinter.cmd("G90")
        #print "G1 F5000 X%s" % (travo)
        #print travo #travo.aficher()

    def BYClicked(self):
        travo = self.travx.get_distance()
        self.myprinter.cmd("G91")
        self.myprinter.cmd("G1 F5000 Y%s" % (travo))
        self.myprinter.cmd("G90")

    def BZClicked(self):
        travo = self.travx.get_distance()
        self.myprinter.cmd("G91")
        self.myprinter.cmd("G1 F5000 Z%s" % (travo))
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

    def BFOffClicked(self):
        self.myprinter.cmd("M107")

    def BFanClicked(self):
        vitessefan=self.SFan.value()
        print vitessefan
        vitessefan = vitessefan*2.55
        print vitessefan
        self.myprinter.cmd("M106 S%s" %(vitessefan))
        #self.myprinter.cmd("M107")

    def BFanClicked(self):
        vitessefan=self.SVitesse.value()
        print vitessefan
        vitesse = vitessefan*2.55
        print vitessefan
        self.myprinter.cmd("M106 S%s" %(vitesse))

    def BFanClicked(self):
        flux=self.SliderFlux.value()
        self.myprinter.cmd("M106 S%s" %(flux))

    def BExtruClicked(self):
        travo = self.travx.get_distance()
        self.myprinter.cmd("G91")
        self.myprinter.cmd("G1 F120 E%s" % (travo))
        self.myprinter.cmd("G90")

    def BRetraClicked(self):
        travo = self.travx.get_distance()
        self.myprinter.cmd("G91")
        self.myprinter.cmd("G1 F120 E-%s" % (travo))
        self.myprinter.cmd("G90")

    def BLoadClicked(self):
        #command.cmd('{"command": "select", "print": false}','X-Api-Key: 054E508852624649B8B250B341CFF639', 'http://127.0.0.1:5000/api/files/local/Vts.gcode')
        gcodeselect=self.LWGcode.currentItem().text()
        print gcodeselect
        #data = json.dumps(dict({"select", "print"":" false}))
        self.myprinter.select(gcodeselect)

    def BPrintClicked(self):
        #command.cmd('{"command": "select", "print": false}','X-Api-Key: 054E508852624649B8B250B341CFF639', 'http://127.0.0.1:5000/api/files/local/Vts.gcode')
        gcodeselect=self.LWGcode.currentItem().text()
        print gcodeselect
        #data = json.dumps(dict({"select", "print"":" false}))
        self.myprinter.selectP(gcodeselect)

    def BSetExtruClicked(self):
        test = self.LETemExt.text()
        print test
        self.LTemExC.setText("Cible :  %s" %(test)) 
        #self.myprinter.cmd("M104 S%s" %(flux)) A decomente pour active

    def BSetBedClicked(self):
        test = self.LETembed.text()
        print test
        self.LTemBedC.setText("Cible :  %s" %(test)) 
        #self.myprinter.cmd("M140 S%s" %(flux))  A decomente pour active

    def BRafCamClicked(self):
        self.webView.reload()
        print "reload"

    def BTerminalClicked(self):
        test = self.LETerminal.text()
        print test
        self.LWTerminal.addItem(test)#("Cible :  %s" %(test))

    def rand(n):
        data = np.random.random(n)
        data[int(n*0.1):int(n*0.13)] += .5
        data[int(n*0.18)] += 2
        data[int(n*0.1):int(n*0.13)] *= 5
        data[int(n*0.18)] *= 20
        data *= 1e-12
        return data, np.arange(n, n+len(data)) / float(n)
    fin = 0
    def update_temp(self, data):
        debut = time.time()
        #print data
        fichier = data['temperature']['bed']['actual']
        self.LTemBed.setText("Actuel :  %3.1f" %(fichier))
        #print "Bed : %s" %fichier
        fichier2 = data['temperature']['tool0']['actual']
        self.LTemEx.setText("Actuel :  %3.1f" %(fichier2))
        #print "Extru1 : %s" %fichier2
        fin = self.travx.get_temps()
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
        self.travx.set_listtemps(Y)
        self.travx.set_listtemperatureE(fichier2)
        self.travx.set_listtemperatureB(fichier)
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
        #temps.reverse()
        #print a
        #print c
        #plt.clearPlots()
        p1.setData(x=temps, y=extru1)
        p2.setData(x=temps, y=bed)
        #plt.addLegend()
        #plt.clear()


        #curvePen = pg.mkPen(color=(255, 15, 10), style=QtCore.Qt.DotLine)

        # plot the curve
        
        #curve = pg.PlotCurveItem(y.shape, x.shape,pen=curvePen,stepMode=True)
        #plt.addItem(curve)
        #fin = self.travx.set_temps(debut)

    def update_temp2(self, data):
        #print data
        pass


if __name__ == '__main__':
    #app=QtGui.QApplication(sys.argv) #app = QApplication(sys.argv)
    #win = App()
    #app.exec_()
    app=QtGui.QApplication(sys.argv) 
    form=MainDialog()
    form.show()
    app.exec_()