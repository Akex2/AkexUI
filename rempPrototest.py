# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rempPrototest.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(1024, 600)
        Frame.setMinimumSize(QtCore.QSize(1024, 600))
        Frame.setMaximumSize(QtCore.QSize(1024, 600))
        Frame.setStyleSheet(_fromUtf8("QScrollBar:vertical {\n"
"\n"
"  border-color: rgb(227, 227, 227);\n"
"  border-width: 1px;\n"
"  border: 2px solid grey;\n"
"   border-radius: 10px;\n"
"  background-color: rgba(255, 255, 255,0);\n"
"  width: 25px;\n"
"  margin: 0px 0 0px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.5, y2:0, stop:0 rgba(255, 95, 0, 255), stop:0.55 rgba(235, 148, 61, 255), stop:1 rgba(208, 156, 69, 255));/* rgba(255, 95, 0, 255);/* rgba(208, 156, 69, 255);/* qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(255, 95, 0, 255), stop:0.55 rgba(235, 148, 61, 255), stop:1 rgba(208, 156, 69, 255));*/\n"
"\n"
"  \n"
"  min-height: 25px;\n"
"  border-radius: 10px;\n"
"\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"    border: 0px solid grey;\n"
"  background-color: rgba(255,255, 255,0);\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background-color: rgba(255,255, 255,0);\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"  }\n"
"QFrame {\n"
"    alternate-background-color: rgb(8, 12, 255);\n"
"    selection-color: white;\n"
"    selection-background-color: rgb(8, 20, 255);\n"
"    /*background-color: qradialgradient(cx: 0.50, cy: 0.5,fx: 0.5, fy: 0.5,radius: 1.0, stop: 0 #212121, stop: 1 #07031c);*/\n"
"    background-color:qlineargradient(x1:1, y1:0, x2:1, y2:1, stop: 0 #545454, stop: 1 #07031c);\n"
"    color: white;\n"
"    margin: 0px;\n"
"    border: 0px;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"    margin: 0px;\n"
"    border-width: 0px;\n"
"    \n"
"}\n"
"QTabWidget {\n"
"    margin: 0px;\n"
"    border-width: 0px;\n"
"}\n"
"\n"
" QTabBar::tab {\n"
"     background-color:qlineargradient(x1:1, y1:1, x2:1, y2:1, stop: 0 #212121, stop: 1 #07031c);\n"
"    /*border: 2px solid #C4C4C3;\n"
"    /*border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    color: white;\n"
"      padding: 10px;\n"
"    margin: 0px;\n"
"    border-width: 0px;\n"
" }"))
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.tabWidget1 = QtGui.QTabWidget(Frame)
        self.tabWidget1.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.tabWidget1.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.tabWidget1.setFont(font)
        self.tabWidget1.setStyleSheet(_fromUtf8("\n"
"QGroupBox{\n"
"    border-color: rgba(255, 255, 255, 0);\n"
"    margin: 0;\n"
"    border: 0px;\n"
"    border-width: 0px;\n"
"\n"
"\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(0, 95, 255, 255), stop:0.55 rgba(61, 148, 235, 255), stop:1 rgba(69, 156, 208, 255));\n"
"/*background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,stop: 0 #66e, stop: 1 #0c0cdc);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,stop: 0 #0c0cdc, stop: 1 #55f);*/\n"
"\n"
"\n"
"border: 1px solid #777;\n"
"height: 15px;\n"
"border-radius: 10px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.4, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.479904 rgba(0, 0, 0, 255), stop:0.522685 rgba(117, 117, 117, 255), stop:1 rgba(163, 163, 163, 255));\n"
"    /*background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);*/\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 40px;\n"
"    margin: -13px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 20px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 15px;  /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    /*background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #B1B1B1, stop:1 #2bff00);*/\n"
"    /*background-color: black;*/\n"
"    margin: 2px 0;\n"
"    border: 1px solid #777;\n"
"    border-radius: 8px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #38e000;\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"\n"
"}\n"
"QProgressBar {\n"
"    color: rgb(166, 166, 166);\n"
"    background-color: rgba(255,255,255,0);\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    text-align: center;\n"
"    border-radius: 8px;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.529, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 127, 0, 255), stop:0.55 rgba(235, 148, 61, 255), stop:1 rgba(80, 80, 80, 255));*/\n"
"    alignment: center;\n"
"    margin: 0px;\n"
"    border:0px;\n"
"    padding : 0px\n"
"    \n"
"}\n"
"QTabWidget {\n"
"    margin: 0px;\n"
"    border-width: 0px;\n"
"}\n"
"\n"
" QTabBar::tab {\n"
"    background-color: rgba(255,255, 255,0);\n"
"     /*background-color:qlineargradient(x1:1, y1:1, x2:1, y2:1, stop: 0 #212121, stop: 1 #07031c);*/\n"
"    /*border: 2px solid #C4C4C3;\n"
"    /*border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    color: white;\n"
"      padding: 10px;\n"
"    margin: 0px;\n"
"    border: 0px;\n"
" }\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 95, 255, 255), stop:0.0813397 rgba(0, 113, 255, 255), stop:0.119617 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"\n"
" }\n"
"QPushButton#BHX{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.5, y2:0, stop:0 rgba(0, 95, 255, 255), stop:0.55 rgba(61, 148, 235, 255), stop:1 rgba(69, 156, 208, 255));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    /*background: rgb(10, 14, 255);*/\n"
"/*image: url(glyphicons_082.png);*/\n"
"/*background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(171, 171, 171, 255));*/\n"
"  /*background-color: #8c8c8c;*/\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 20px;\n"
"    border-color: rgba(255,255,255,0);\n"
"    font: bold 20px;\n"
"    padding: 10;\n"
"}    \n"
"QPushButton#BHY{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.5, y2:0, stop:0 rgba(0, 95, 255, 255), stop:0.55 rgba(61, 148, 235, 255), stop:1 rgba(69, 156, 208, 255));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    /*background: rgb(10, 14, 255);*/\n"
"/*image: url(glyphicons_082.png);*/\n"
"/*background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(171, 171, 171, 255));*/\n"
"  /*background-color: #8c8c8c;*/\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 20px;\n"
"    border-color: rgba(255,255,255,0);\n"
"    font: bold 20px;\n"
"    padding: 10;\n"
"}    \n"
"QPushButton#BHZ{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.5, y2:0, stop:0 rgba(0, 95, 255, 255), stop:0.55 rgba(61, 148, 235, 255), stop:1 rgba(69, 156, 208, 255));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    /*background: rgb(10, 14, 255);*/\n"
"/*image: url(glyphicons_082.png);*/\n"
"/*background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(171, 171, 171, 255));*/\n"
"  /*background-color: #8c8c8c;*/\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 20px;\n"
"    border-color: rgba(255,255,255,0);\n"
"    font: bold 20px;\n"
"    padding: 10;\n"
"}    \n"
"QPushButton{\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    /*background-color: #8c8c8c;*/\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 20px;\n"
"    border-color: rgba(255,255,255,0);\n"
"    font: bold 20px;\n"
"    padding: 0;\n"
"}\n"
"QPushButton#BRafrGcode{\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.5, y2:0, stop:0 rgba(0, 95, 255, 255), stop:0.55 rgba(61, 148, 235, 255), stop:1 rgba(69, 156, 208, 255));\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 20px;\n"
"    border-color: rgba(255,255,255,0);\n"
"    font: bold 20px;\n"
"    padding: 10;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:checked {\n"
" border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 15px;\n"
"    border-color: beige;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(56, 56, 56, 255), stop:1 rgba(77, 77, 77, 255));\n"
"    /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);*/\n"
"}\n"
"QPushButton:!enabled{\n"
"    color: rgb(94, 94, 94);\n"
" \n"
"}\n"
"QLabel {\n"
"    background-color:rgba(255,255, 255,0); /*qradialgradient(cx: 0.50, cy: 0.5,fx: 0.5, fy: 0.5,radius: 1.0, stop: 0 #212121, stop: 1 #07031c);*/\n"
"    color: white;\n"
"}\n"
"QLineEdit {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(64, 64, 64);\n"
"    color: white;\n"
"}\n"
"QComboBox{\n"
"    border-radius: 20px;\n"
"    color: white ;\n"
"    selection-background-color:rgb(15, 39, 255);\n"
"    background-color: rgb(89, 89, 89);\n"
"}\n"
"QComboBox::item:selected:active {\n"
"    selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(171, 171, 171, 255));\n"
"    /*selection-background-color: rgb(25, 255, 25);*/\n"
"    /*background-color: rgb(255, 115, 255);*/\n"
"    background: (15, 39, 255);/*qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);*/\n"
"}\n"
"QCombobox:!editable{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color:white;\n"
"}\n"
"/*QComboBox:editable {\n"
"    background: blue;\n"
"    color: pink;\n"
"    \n"
"}*/\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"QComboBox::drop-down {\n"
"    \n"
"    background-color: rgb(139, 139, 139);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 35px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    /*border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 20px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 20px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(171, 171, 171, 255));\n"
"    background-color: #2c2c2c;\n"
"    border-width: 1px;\n"
"    padding: 5px 0px 5px 0px;\n"
"    border-style: solid;\n"
"    border-color: #4d4d4d;\n"
"    color: #cbcbcb;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"QListWidget QAbstractItemView {\n"
"    selection-background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(171, 171, 171, 255));\n"
"    background-color: #2c2c2c;\n"
"    border-width: 1px;\n"
"    padding: 5px 0px 5px 0px;\n"
"    border-style: solid;\n"
"    border-color: #4d4d4d;\n"
"    color: #cbcbcb;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QListWidget {\n"
"    selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(171, 171, 171, 255));\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    /*selection-background-color:rgb(15, 39, 255);*/\n"
"}\n"
"QListWidget::item:selected:active {\n"
"    selection-background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(171, 171, 171, 255));\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(171, 171, 171, 255));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(0, 81, 255, 255));*/\n"
"    /*background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"    /*background: rgb(24, 16, 255);*/\n"
"    /*background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);*/\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    border-radius: 10px;\n"
"}\n"
"QRadioButton::indicator::checked {\n"
"    border-radius: 15px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.479904 rgba(0, 0, 0, 255), stop:0.522685 rgba(117, 117, 117, 255), stop:1 rgba(163, 163, 163, 255));\n"
"   /* image: url(:/images/radiobutton_checked.png);*/\n"
"}\n"
"QRadioButton{\n"
"padding: 1px 0px 1px 3px;\n"
"color: white;\n"
"width: 25px;\n"
"height: 25px;\n"
"}\n"
"QRadioButton::indicator::unchecked {\n"
"   border-radius: 15px;\n"
"    background-color: rgb(255,255,255);\n"
"   /* image: url(:/images/radiobutton_checked.png);*/\n"
"}"))
        self.tabWidget1.setObjectName(_fromUtf8("tabWidget1"))
        self.TConnect = QtGui.QWidget()
        self.TConnect.setObjectName(_fromUtf8("TConnect"))
        self.CBport = QtGui.QComboBox(self.TConnect)
        self.CBport.setGeometry(QtCore.QRect(80, 70, 491, 51))
        self.CBport.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CBport.setFont(font)
        self.CBport.setEditable(False)
        self.CBport.setObjectName(_fromUtf8("CBport"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.TConnect)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(80, 150, 521, 80))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.labeletatprinteuse = QtGui.QLabel(self.gridLayoutWidget_4)
        self.labeletatprinteuse.setMaximumSize(QtCore.QSize(186, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labeletatprinteuse.setFont(font)
        self.labeletatprinteuse.setObjectName(_fromUtf8("labeletatprinteuse"))
        self.gridLayout_4.addWidget(self.labeletatprinteuse, 0, 0, 1, 1)
        self.labelprofileprinteuse = QtGui.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelprofileprinteuse.setFont(font)
        self.labelprofileprinteuse.setObjectName(_fromUtf8("labelprofileprinteuse"))
        self.gridLayout_4.addWidget(self.labelprofileprinteuse, 1, 0, 1, 1)
        self.LEtatPrinteuse = QtGui.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LEtatPrinteuse.setFont(font)
        self.LEtatPrinteuse.setText(_fromUtf8(""))
        self.LEtatPrinteuse.setObjectName(_fromUtf8("LEtatPrinteuse"))
        self.gridLayout_4.addWidget(self.LEtatPrinteuse, 0, 1, 1, 1)
        self.LProfilePrinteuse = QtGui.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LProfilePrinteuse.setFont(font)
        self.LProfilePrinteuse.setText(_fromUtf8(""))
        self.LProfilePrinteuse.setObjectName(_fromUtf8("LProfilePrinteuse"))
        self.gridLayout_4.addWidget(self.LProfilePrinteuse, 1, 1, 1, 1)
        self.gridLayoutWidget_10 = QtGui.QWidget(self.TConnect)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(650, 60, 253, 201))
        self.gridLayoutWidget_10.setObjectName(_fromUtf8("gridLayoutWidget_10"))
        self.gridLayout_10 = QtGui.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.BConnect = QtGui.QPushButton(self.gridLayoutWidget_10)
        self.BConnect.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BConnect.setFont(font)
        self.BConnect.setObjectName(_fromUtf8("BConnect"))
        self.gridLayout_10.addWidget(self.BConnect, 0, 0, 1, 1)
        self.BDisconect = QtGui.QPushButton(self.gridLayoutWidget_10)
        self.BDisconect.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BDisconect.setFont(font)
        self.BDisconect.setObjectName(_fromUtf8("BDisconect"))
        self.gridLayout_10.addWidget(self.BDisconect, 1, 0, 1, 1)
        self.BConectRafr = QtGui.QPushButton(self.gridLayoutWidget_10)
        self.BConectRafr.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BConectRafr.setFont(font)
        self.BConectRafr.setDefault(False)
        self.BConectRafr.setFlat(False)
        self.BConectRafr.setObjectName(_fromUtf8("BConectRafr"))
        self.gridLayout_10.addWidget(self.BConectRafr, 2, 0, 1, 1)
        self.gridLayoutWidget_12 = QtGui.QWidget(self.TConnect)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(80, 280, 451, 201))
        self.gridLayoutWidget_12.setObjectName(_fromUtf8("gridLayoutWidget_12"))
        self.gridLayout_12 = QtGui.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem, 5, 0, 1, 1)
        self.RBSysteme = QtGui.QRadioButton(self.gridLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.RBSysteme.setFont(font)
        self.RBSysteme.setObjectName(_fromUtf8("RBSysteme"))
        self.gridLayout_12.addWidget(self.RBSysteme, 4, 2, 2, 1)
        self.RBRedeem = QtGui.QRadioButton(self.gridLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.RBRedeem.setFont(font)
        self.RBRedeem.setObjectName(_fromUtf8("RBRedeem"))
        self.gridLayout_12.addWidget(self.RBRedeem, 2, 2, 2, 1)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem2, 0, 0, 1, 1)
        self.PBArret = QtGui.QPushButton(self.gridLayoutWidget_12)
        self.PBArret.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBArret.setFont(font)
        self.PBArret.setObjectName(_fromUtf8("PBArret"))
        self.gridLayout_12.addWidget(self.PBArret, 3, 0, 2, 1)
        self.PBReboot = QtGui.QPushButton(self.gridLayoutWidget_12)
        self.PBReboot.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBReboot.setFont(font)
        self.PBReboot.setObjectName(_fromUtf8("PBReboot"))
        self.gridLayout_12.addWidget(self.PBReboot, 1, 0, 2, 1)
        self.RBOcto = QtGui.QRadioButton(self.gridLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.RBOcto.setFont(font)
        self.RBOcto.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.RBOcto.setObjectName(_fromUtf8("RBOcto"))
        self.gridLayout_12.addWidget(self.RBOcto, 0, 2, 2, 1)
        self.tabWidget1.addTab(self.TConnect, _fromUtf8(""))
        self.TPrint = QtGui.QWidget()
        self.TPrint.setObjectName(_fromUtf8("TPrint"))
        self.LWGcode = QtGui.QListWidget(self.TPrint)
        self.LWGcode.setGeometry(QtCore.QRect(10, 10, 551, 411))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LWGcode.setFont(font)
        self.LWGcode.setObjectName(_fromUtf8("LWGcode"))
        self.BPause = QtGui.QPushButton(self.TPrint)
        self.BPause.setGeometry(QtCore.QRect(740, 90, 100, 51))
        self.BPause.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BPause.setFont(font)
        self.BPause.setIconSize(QtCore.QSize(40, 40))
        self.BPause.setObjectName(_fromUtf8("BPause"))
        self.BStop = QtGui.QPushButton(self.TPrint)
        self.BStop.setGeometry(QtCore.QRect(890, 90, 100, 51))
        self.BStop.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BStop.setFont(font)
        self.BStop.setIconSize(QtCore.QSize(40, 40))
        self.BStop.setObjectName(_fromUtf8("BStop"))
        self.BLoadPrint = QtGui.QPushButton(self.TPrint)
        self.BLoadPrint.setEnabled(True)
        self.BLoadPrint.setGeometry(QtCore.QRect(650, 20, 151, 51))
        self.BLoadPrint.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BLoadPrint.setFont(font)
        self.BLoadPrint.setObjectName(_fromUtf8("BLoadPrint"))
        self.BPlay = QtGui.QPushButton(self.TPrint)
        self.BPlay.setGeometry(QtCore.QRect(580, 90, 100, 51))
        self.BPlay.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BPlay.setFont(font)
        self.BPlay.setObjectName(_fromUtf8("BPlay"))
        self.BPrint = QtGui.QPushButton(self.TPrint)
        self.BPrint.setEnabled(True)
        self.BPrint.setGeometry(QtCore.QRect(830, 20, 151, 51))
        self.BPrint.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BPrint.setFont(font)
        self.BPrint.setObjectName(_fromUtf8("BPrint"))
        self.progressBar = QtGui.QProgressBar(self.TPrint)
        self.progressBar.setGeometry(QtCore.QRect(10, 430, 1001, 121))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(_fromUtf8(""))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.BRafrGcode = QtGui.QPushButton(self.TPrint)
        self.BRafrGcode.setGeometry(QtCore.QRect(580, 20, 51, 51))
        self.BRafrGcode.setMinimumSize(QtCore.QSize(0, 51))
        self.BRafrGcode.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/alex/glyphicons_082.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BRafrGcode.setIcon(icon)
        self.BRafrGcode.setIconSize(QtCore.QSize(40, 40))
        self.BRafrGcode.setObjectName(_fromUtf8("BRafrGcode"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.TPrint)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(580, 150, 431, 271))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelfilament = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelfilament.setFont(font)
        self.labelfilament.setObjectName(_fromUtf8("labelfilament"))
        self.gridLayout_2.addWidget(self.labelfilament, 1, 0, 1, 1)
        self.labelnom = QtGui.QLabel(self.gridLayoutWidget_2)
        self.labelnom.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelnom.setFont(font)
        self.labelnom.setObjectName(_fromUtf8("labelnom"))
        self.gridLayout_2.addWidget(self.labelnom, 0, 0, 1, 1)
        self.labeltempasser = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labeltempasser.setFont(font)
        self.labeltempasser.setObjectName(_fromUtf8("labeltempasser"))
        self.gridLayout_2.addWidget(self.labeltempasser, 3, 0, 1, 1)
        self.labeltempsetsitmer = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labeltempsetsitmer.setFont(font)
        self.labeltempsetsitmer.setObjectName(_fromUtf8("labeltempsetsitmer"))
        self.gridLayout_2.addWidget(self.labeltempsetsitmer, 2, 0, 1, 1)
        self.labeltempsrestant = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labeltempsrestant.setFont(font)
        self.labeltempsrestant.setObjectName(_fromUtf8("labeltempsrestant"))
        self.gridLayout_2.addWidget(self.labeltempsrestant, 4, 0, 1, 1)
        self.LNomFichier = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LNomFichier.setFont(font)
        self.LNomFichier.setText(_fromUtf8(""))
        self.LNomFichier.setObjectName(_fromUtf8("LNomFichier"))
        self.gridLayout_2.addWidget(self.LNomFichier, 0, 1, 1, 1)
        self.LFilamentFichier = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LFilamentFichier.setFont(font)
        self.LFilamentFichier.setText(_fromUtf8(""))
        self.LFilamentFichier.setObjectName(_fromUtf8("LFilamentFichier"))
        self.gridLayout_2.addWidget(self.LFilamentFichier, 1, 1, 1, 1)
        self.LTEFichier = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LTEFichier.setFont(font)
        self.LTEFichier.setText(_fromUtf8(""))
        self.LTEFichier.setObjectName(_fromUtf8("LTEFichier"))
        self.gridLayout_2.addWidget(self.LTEFichier, 2, 1, 1, 1)
        self.LTPFichier = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LTPFichier.setFont(font)
        self.LTPFichier.setText(_fromUtf8(""))
        self.LTPFichier.setObjectName(_fromUtf8("LTPFichier"))
        self.gridLayout_2.addWidget(self.LTPFichier, 3, 1, 1, 1)
        self.LTRFichier = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LTRFichier.setFont(font)
        self.LTRFichier.setText(_fromUtf8(""))
        self.LTRFichier.setObjectName(_fromUtf8("LTRFichier"))
        self.gridLayout_2.addWidget(self.LTRFichier, 4, 1, 1, 1)
        self.tabWidget1.addTab(self.TPrint, _fromUtf8(""))
        self.TTemp = QtGui.QWidget()
        self.TTemp.setObjectName(_fromUtf8("TTemp"))
        self.plot = PlotWidget(self.TTemp)
        self.plot.setGeometry(QtCore.QRect(10, 10, 1001, 411))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.plot.setFont(font)
        self.plot.setObjectName(_fromUtf8("plot"))
        self.gridLayoutWidget_5 = QtGui.QWidget(self.TTemp)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 430, 1001, 111))
        self.gridLayoutWidget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 3, 1, 1)
        self.LTemBedC = QtGui.QLabel(self.gridLayoutWidget_5)
        self.LTemBedC.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LTemBedC.setFont(font)
        self.LTemBedC.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LTemBedC.setObjectName(_fromUtf8("LTemBedC"))
        self.gridLayout_5.addWidget(self.LTemBedC, 1, 4, 1, 1)
        self.BSetExtru = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.BSetExtru.setEnabled(True)
        self.BSetExtru.setMinimumSize(QtCore.QSize(130, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BSetExtru.setFont(font)
        self.BSetExtru.setObjectName(_fromUtf8("BSetExtru"))
        self.gridLayout_5.addWidget(self.BSetExtru, 1, 2, 1, 1)
        self.LETemExt = extQLineEdit(self.gridLayoutWidget_5)
        self.LETemExt.setMinimumSize(QtCore.QSize(0, 51))
        self.LETemExt.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LETemExt.setFont(font)
        self.LETemExt.setText(_fromUtf8(""))
        self.LETemExt.setAlignment(QtCore.Qt.AlignCenter)
        self.LETemExt.setObjectName(_fromUtf8("LETemExt"))
        self.gridLayout_5.addWidget(self.LETemExt, 1, 1, 1, 1)
        self.LTemExC = QtGui.QLabel(self.gridLayoutWidget_5)
        self.LTemExC.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LTemExC.setFont(font)
        self.LTemExC.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LTemExC.setObjectName(_fromUtf8("LTemExC"))
        self.gridLayout_5.addWidget(self.LTemExC, 1, 0, 1, 1)
        self.LTemEx_ = QtGui.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LTemEx_.setFont(font)
        self.LTemEx_.setAlignment(QtCore.Qt.AlignCenter)
        self.LTemEx_.setObjectName(_fromUtf8("LTemEx_"))
        self.gridLayout_5.addWidget(self.LTemEx_, 0, 0, 1, 1)
        self.LTemBed_ = QtGui.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LTemBed_.setFont(font)
        self.LTemBed_.setAlignment(QtCore.Qt.AlignCenter)
        self.LTemBed_.setObjectName(_fromUtf8("LTemBed_"))
        self.gridLayout_5.addWidget(self.LTemBed_, 0, 4, 1, 1)
        self.LTemEx = QtGui.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LTemEx.setFont(font)
        self.LTemEx.setText(_fromUtf8(""))
        self.LTemEx.setObjectName(_fromUtf8("LTemEx"))
        self.gridLayout_5.addWidget(self.LTemEx, 0, 1, 1, 1)
        self.LETembed = extQLineEdit(self.gridLayoutWidget_5)
        self.LETembed.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LETembed.setFont(font)
        self.LETembed.setAlignment(QtCore.Qt.AlignCenter)
        self.LETembed.setObjectName(_fromUtf8("LETembed"))
        self.gridLayout_5.addWidget(self.LETembed, 1, 5, 1, 1)
        self.PBExtruOff = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.PBExtruOff.setEnabled(True)
        self.PBExtruOff.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBExtruOff.setFont(font)
        self.PBExtruOff.setObjectName(_fromUtf8("PBExtruOff"))
        self.gridLayout_5.addWidget(self.PBExtruOff, 0, 2, 1, 1)
        self.BSetBed = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.BSetBed.setMinimumSize(QtCore.QSize(130, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BSetBed.setFont(font)
        self.BSetBed.setObjectName(_fromUtf8("BSetBed"))
        self.gridLayout_5.addWidget(self.BSetBed, 1, 6, 1, 1)
        self.PBBedOff = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.PBBedOff.setEnabled(True)
        self.PBBedOff.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBBedOff.setFont(font)
        self.PBBedOff.setObjectName(_fromUtf8("PBBedOff"))
        self.gridLayout_5.addWidget(self.PBBedOff, 0, 6, 1, 1)
        self.LTemBed = QtGui.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LTemBed.setFont(font)
        self.LTemBed.setText(_fromUtf8(""))
        self.LTemBed.setObjectName(_fromUtf8("LTemBed"))
        self.gridLayout_5.addWidget(self.LTemBed, 0, 5, 1, 1)
        self.tabWidget1.addTab(self.TTemp, _fromUtf8(""))
        self.TControl = QtGui.QWidget()
        self.TControl.setObjectName(_fromUtf8("TControl"))
        self.gridLayoutWidget_8 = QtGui.QWidget(self.TControl)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(0, 320, 1021, 231))
        self.gridLayoutWidget_8.setObjectName(_fromUtf8("gridLayoutWidget_8"))
        self.gridLayout_8 = QtGui.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem4, 0, 4, 1, 1)
        self.BFlux = QtGui.QPushButton(self.gridLayoutWidget_8)
        self.BFlux.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BFlux.setFont(font)
        self.BFlux.setObjectName(_fromUtf8("BFlux"))
        self.gridLayout_8.addWidget(self.BFlux, 2, 5, 1, 1)
        self.SliderFlux = QtGui.QSlider(self.gridLayoutWidget_8)
        self.SliderFlux.setMinimumSize(QtCore.QSize(0, 51))
        self.SliderFlux.setMaximum(150)
        self.SliderFlux.setSliderPosition(99)
        self.SliderFlux.setOrientation(QtCore.Qt.Horizontal)
        self.SliderFlux.setObjectName(_fromUtf8("SliderFlux"))
        self.gridLayout_8.addWidget(self.SliderFlux, 2, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem5, 0, 0, 1, 1)
        self.SVitesse = QtGui.QSlider(self.gridLayoutWidget_8)
        self.SVitesse.setMinimumSize(QtCore.QSize(0, 51))
        self.SVitesse.setMaximum(200)
        self.SVitesse.setProperty("value", 100)
        self.SVitesse.setOrientation(QtCore.Qt.Horizontal)
        self.SVitesse.setObjectName(_fromUtf8("SVitesse"))
        self.gridLayout_8.addWidget(self.SVitesse, 1, 3, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem6, 0, 2, 1, 1)
        self.LTFlux = QtGui.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LTFlux.setFont(font)
        self.LTFlux.setAlignment(QtCore.Qt.AlignCenter)
        self.LTFlux.setObjectName(_fromUtf8("LTFlux"))
        self.gridLayout_8.addWidget(self.LTFlux, 2, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem7, 1, 6, 1, 1)
        self.BVitesse = QtGui.QPushButton(self.gridLayoutWidget_8)
        self.BVitesse.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BVitesse.setFont(font)
        self.BVitesse.setObjectName(_fromUtf8("BVitesse"))
        self.gridLayout_8.addWidget(self.BVitesse, 1, 5, 1, 1)
        self.LTVitesse = QtGui.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LTVitesse.setFont(font)
        self.LTVitesse.setAlignment(QtCore.Qt.AlignCenter)
        self.LTVitesse.setObjectName(_fromUtf8("LTVitesse"))
        self.gridLayout_8.addWidget(self.LTVitesse, 1, 1, 1, 1)
        self.BFan = QtGui.QPushButton(self.gridLayoutWidget_8)
        self.BFan.setMinimumSize(QtCore.QSize(161, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BFan.setFont(font)
        self.BFan.setObjectName(_fromUtf8("BFan"))
        self.gridLayout_8.addWidget(self.BFan, 0, 5, 1, 1)
        self.SFan = QtGui.QSlider(self.gridLayoutWidget_8)
        self.SFan.setMinimumSize(QtCore.QSize(0, 51))
        self.SFan.setMaximum(100)
        self.SFan.setOrientation(QtCore.Qt.Horizontal)
        self.SFan.setObjectName(_fromUtf8("SFan"))
        self.gridLayout_8.addWidget(self.SFan, 0, 3, 1, 1)
        self.LTFan = QtGui.QLabel(self.gridLayoutWidget_8)
        self.LTFan.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LTFan.setFont(font)
        self.LTFan.setAlignment(QtCore.Qt.AlignCenter)
        self.LTFan.setObjectName(_fromUtf8("LTFan"))
        self.gridLayout_8.addWidget(self.LTFan, 0, 1, 1, 1)
        self.PBAlimOn = QtGui.QPushButton(self.gridLayoutWidget_8)
        self.PBAlimOn.setMinimumSize(QtCore.QSize(80, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBAlimOn.setFont(font)
        self.PBAlimOn.setCheckable(True)
        self.PBAlimOn.setAutoExclusive(True)
        self.PBAlimOn.setObjectName(_fromUtf8("PBAlimOn"))
        self.gridLayout_8.addWidget(self.PBAlimOn, 2, 7, 1, 1)
        self.LAlim = QtGui.QLabel(self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LAlim.setFont(font)
        self.LAlim.setAlignment(QtCore.Qt.AlignCenter)
        self.LAlim.setObjectName(_fromUtf8("LAlim"))
        self.gridLayout_8.addWidget(self.LAlim, 1, 7, 1, 3)
        self.PBAlimOff = QtGui.QPushButton(self.gridLayoutWidget_8)
        self.PBAlimOff.setMinimumSize(QtCore.QSize(80, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBAlimOff.setFont(font)
        self.PBAlimOff.setAutoExclusive(True)
        self.PBAlimOff.setObjectName(_fromUtf8("PBAlimOff"))
        self.gridLayout_8.addWidget(self.PBAlimOff, 2, 9, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem8, 2, 8, 1, 1)
        self.BFOFF = QtGui.QPushButton(self.gridLayoutWidget_8)
        self.BFOFF.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BFOFF.setFont(font)
        self.BFOFF.setObjectName(_fromUtf8("BFOFF"))
        self.gridLayout_8.addWidget(self.BFOFF, 0, 7, 1, 3)
        spacerItem9 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem9, 0, 10, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.TControl)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 1024, 311))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1031, 61))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.BZZU = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.BZZU.setMinimumSize(QtCore.QSize(130, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BZZU.setFont(font)
        self.BZZU.setCheckable(True)
        self.BZZU.setChecked(False)
        self.BZZU.setAutoExclusive(True)
        self.BZZU.setObjectName(_fromUtf8("BZZU"))
        self.horizontalLayout_2.addWidget(self.BZZU)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.BZU = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.BZU.setMinimumSize(QtCore.QSize(130, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BZU.setFont(font)
        self.BZU.setCheckable(True)
        self.BZU.setAutoExclusive(True)
        self.BZU.setObjectName(_fromUtf8("BZU"))
        self.horizontalLayout_2.addWidget(self.BZU)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.BU = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.BU.setMinimumSize(QtCore.QSize(130, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BU.setFont(font)
        self.BU.setCheckable(True)
        self.BU.setChecked(True)
        self.BU.setAutoExclusive(True)
        self.BU.setObjectName(_fromUtf8("BU"))
        self.horizontalLayout_2.addWidget(self.BU)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.BD = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.BD.setMinimumSize(QtCore.QSize(130, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BD.setFont(font)
        self.BD.setCheckable(True)
        self.BD.setAutoExclusive(True)
        self.BD.setObjectName(_fromUtf8("BD"))
        self.horizontalLayout_2.addWidget(self.BD)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.BC = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.BC.setMinimumSize(QtCore.QSize(130, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BC.setFont(font)
        self.BC.setCheckable(True)
        self.BC.setAutoExclusive(True)
        self.BC.setObjectName(_fromUtf8("BC"))
        self.horizontalLayout_2.addWidget(self.BC)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.gridLayoutWidget_9 = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(0, 70, 811, 141))
        self.gridLayoutWidget_9.setObjectName(_fromUtf8("gridLayoutWidget_9"))
        self.gridLayout_9 = QtGui.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.BX = QtGui.QPushButton(self.gridLayoutWidget_9)
        self.BX.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BX.setFont(font)
        self.BX.setAutoExclusive(False)
        self.BX.setObjectName(_fromUtf8("BX"))
        self.gridLayout_9.addWidget(self.BX, 0, 2, 1, 2)
        self.BX_2 = QtGui.QPushButton(self.gridLayoutWidget_9)
        self.BX_2.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BX_2.setFont(font)
        self.BX_2.setAutoExclusive(False)
        self.BX_2.setObjectName(_fromUtf8("BX_2"))
        self.gridLayout_9.addWidget(self.BX_2, 0, 5, 1, 2)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem16, 0, 7, 1, 1)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem17, 1, 6, 1, 1)
        spacerItem18 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem18, 0, 17, 1, 1)
        spacerItem19 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem19, 0, 11, 1, 1)
        spacerItem20 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem20, 0, 0, 1, 1)
        self.BY_2 = QtGui.QPushButton(self.gridLayoutWidget_9)
        self.BY_2.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BY_2.setFont(font)
        self.BY_2.setObjectName(_fromUtf8("BY_2"))
        self.gridLayout_9.addWidget(self.BY_2, 0, 12, 1, 2)
        self.BHY = QtGui.QPushButton(self.gridLayoutWidget_9)
        self.BHY.setMinimumSize(QtCore.QSize(0, 51))
        self.BHY.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/alex/glyphicons_020_home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BHY.setIcon(icon1)
        self.BHY.setObjectName(_fromUtf8("BHY"))
        self.gridLayout_9.addWidget(self.BHY, 1, 10, 1, 3)
        spacerItem21 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem21, 0, 4, 1, 1)
        spacerItem22 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem22, 0, 20, 1, 1)
        spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem23, 1, 2, 1, 1)
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem24, 0, 14, 1, 1)
        self.BHX = QtGui.QPushButton(self.gridLayoutWidget_9)
        self.BHX.setMinimumSize(QtCore.QSize(0, 51))
        self.BHX.setText(_fromUtf8(""))
        self.BHX.setIcon(icon1)
        self.BHX.setObjectName(_fromUtf8("BHX"))
        self.gridLayout_9.addWidget(self.BHX, 1, 3, 1, 3)
        self.BY = QtGui.QPushButton(self.gridLayoutWidget_9)
        self.BY.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BY.setFont(font)
        self.BY.setObjectName(_fromUtf8("BY"))
        self.gridLayout_9.addWidget(self.BY, 0, 9, 1, 2)
        self.BZ = QtGui.QPushButton(self.gridLayoutWidget_9)
        self.BZ.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BZ.setFont(font)
        self.BZ.setObjectName(_fromUtf8("BZ"))
        self.gridLayout_9.addWidget(self.BZ, 0, 15, 1, 2)
        self.BZ_2 = QtGui.QPushButton(self.gridLayoutWidget_9)
        self.BZ_2.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BZ_2.setFont(font)
        self.BZ_2.setObjectName(_fromUtf8("BZ_2"))
        self.gridLayout_9.addWidget(self.BZ_2, 0, 18, 1, 2)
        self.BHZ = QtGui.QPushButton(self.gridLayoutWidget_9)
        self.BHZ.setMinimumSize(QtCore.QSize(0, 51))
        self.BHZ.setText(_fromUtf8(""))
        self.BHZ.setIcon(icon1)
        self.BHZ.setObjectName(_fromUtf8("BHZ"))
        self.gridLayout_9.addWidget(self.BHZ, 1, 16, 1, 3)
        self.gridLayoutWidget_11 = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(0, 220, 1021, 91))
        self.gridLayoutWidget_11.setObjectName(_fromUtf8("gridLayoutWidget_11"))
        self.gridLayout_11 = QtGui.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        spacerItem25 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem25, 0, 5, 1, 1)
        self.LEExtru = extQLineEdit(self.gridLayoutWidget_11)
        self.LEExtru.setMinimumSize(QtCore.QSize(0, 51))
        self.LEExtru.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LEExtru.setFont(font)
        self.LEExtru.setAlignment(QtCore.Qt.AlignCenter)
        self.LEExtru.setObjectName(_fromUtf8("LEExtru"))
        self.gridLayout_11.addWidget(self.LEExtru, 0, 4, 1, 1)
        self.BED = QtGui.QPushButton(self.gridLayoutWidget_11)
        self.BED.setMinimumSize(QtCore.QSize(0, 51))
        self.BED.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BED.setFont(font)
        self.BED.setCheckable(False)
        self.BED.setObjectName(_fromUtf8("BED"))
        self.gridLayout_11.addWidget(self.BED, 0, 7, 1, 1)
        spacerItem26 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem26, 0, 0, 1, 1)
        self.BRetra = QtGui.QPushButton(self.gridLayoutWidget_11)
        self.BRetra.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BRetra.setFont(font)
        self.BRetra.setObjectName(_fromUtf8("BRetra"))
        self.gridLayout_11.addWidget(self.BRetra, 0, 2, 1, 1)
        self.BExtru = QtGui.QPushButton(self.gridLayoutWidget_11)
        self.BExtru.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BExtru.setFont(font)
        self.BExtru.setObjectName(_fromUtf8("BExtru"))
        self.gridLayout_11.addWidget(self.BExtru, 0, 1, 1, 1)
        self.BECent = QtGui.QPushButton(self.gridLayoutWidget_11)
        self.BECent.setMinimumSize(QtCore.QSize(0, 51))
        self.BECent.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BECent.setFont(font)
        self.BECent.setCheckable(False)
        self.BECent.setObjectName(_fromUtf8("BECent"))
        self.gridLayout_11.addWidget(self.BECent, 0, 8, 1, 1)
        spacerItem27 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem27, 0, 9, 1, 1)
        spacerItem28 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem28, 0, 3, 1, 1)
        self.BEC = QtGui.QPushButton(self.gridLayoutWidget_11)
        self.BEC.setMinimumSize(QtCore.QSize(0, 51))
        self.BEC.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BEC.setFont(font)
        self.BEC.setCheckable(False)
        self.BEC.setObjectName(_fromUtf8("BEC"))
        self.gridLayout_11.addWidget(self.BEC, 0, 6, 1, 1)
        self.BMotor = QtGui.QPushButton(self.groupBox)
        self.BMotor.setGeometry(QtCore.QRect(830, 80, 171, 131))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BMotor.setFont(font)
        self.BMotor.setObjectName(_fromUtf8("BMotor"))
        self.tabWidget1.addTab(self.TControl, _fromUtf8(""))
        self.TCam = QtGui.QWidget()
        self.TCam.setObjectName(_fromUtf8("TCam"))
        self.webView = QtWebKit.QWebView(self.TCam)
        self.webView.setGeometry(QtCore.QRect(10, 20, 640, 480))
        self.webView.setMouseTracking(False)
        self.webView.setAcceptDrops(True)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://127.0.0.1:8080/?action=snapshot")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayoutWidget_7 = QtGui.QWidget(self.TCam)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(680, 20, 321, 521))
        self.gridLayoutWidget_7.setObjectName(_fromUtf8("gridLayoutWidget_7"))
        self.gridLayout_7 = QtGui.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.LEDerImg = extQLineEdit(self.gridLayoutWidget_7)
        self.LEDerImg.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LEDerImg.setFont(font)
        self.LEDerImg.setAlignment(QtCore.Qt.AlignCenter)
        self.LEDerImg.setObjectName(_fromUtf8("LEDerImg"))
        self.gridLayout_7.addWidget(self.LEDerImg, 10, 0, 1, 1)
        self.LEFps = extQLineEdit(self.gridLayoutWidget_7)
        self.LEFps.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LEFps.setFont(font)
        self.LEFps.setAlignment(QtCore.Qt.AlignCenter)
        self.LEFps.setObjectName(_fromUtf8("LEFps"))
        self.gridLayout_7.addWidget(self.LEFps, 7, 0, 1, 1)
        spacerItem29 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem29, 8, 0, 1, 1)
        self.LTime_2 = QtGui.QLabel(self.gridLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LTime_2.setFont(font)
        self.LTime_2.setText(_fromUtf8(""))
        self.LTime_2.setAlignment(QtCore.Qt.AlignCenter)
        self.LTime_2.setObjectName(_fromUtf8("LTime_2"))
        self.gridLayout_7.addWidget(self.LTime_2, 12, 0, 1, 1)
        self.LEZhop = extQLineEdit(self.gridLayoutWidget_7)
        self.LEZhop.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LEZhop.setFont(font)
        self.LEZhop.setAlignment(QtCore.Qt.AlignCenter)
        self.LEZhop.setObjectName(_fromUtf8("LEZhop"))
        self.gridLayout_7.addWidget(self.LEZhop, 13, 0, 1, 1)
        spacerItem30 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem30, 14, 0, 1, 1)
        spacerItem31 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem31, 2, 0, 1, 1)
        self.BSaveTime = QtGui.QPushButton(self.gridLayoutWidget_7)
        self.BSaveTime.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BSaveTime.setFont(font)
        self.BSaveTime.setObjectName(_fromUtf8("BSaveTime"))
        self.gridLayout_7.addWidget(self.BSaveTime, 15, 0, 1, 1)
        self.BRafCam = QtGui.QPushButton(self.gridLayoutWidget_7)
        self.BRafCam.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BRafCam.setFont(font)
        self.BRafCam.setObjectName(_fromUtf8("BRafCam"))
        self.gridLayout_7.addWidget(self.BRafCam, 1, 0, 1, 1)
        spacerItem32 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem32, 11, 0, 1, 1)
        self.LDerImg = QtGui.QLabel(self.gridLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LDerImg.setFont(font)
        self.LDerImg.setAlignment(QtCore.Qt.AlignCenter)
        self.LDerImg.setObjectName(_fromUtf8("LDerImg"))
        self.gridLayout_7.addWidget(self.LDerImg, 9, 0, 1, 1)
        spacerItem33 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem33, 5, 0, 1, 1)
        self.LFps = QtGui.QLabel(self.gridLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LFps.setFont(font)
        self.LFps.setAlignment(QtCore.Qt.AlignCenter)
        self.LFps.setObjectName(_fromUtf8("LFps"))
        self.gridLayout_7.addWidget(self.LFps, 6, 0, 1, 1)
        self.CBTime = QtGui.QComboBox(self.gridLayoutWidget_7)
        self.CBTime.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.CBTime.setFont(font)
        self.CBTime.setObjectName(_fromUtf8("CBTime"))
        self.gridLayout_7.addWidget(self.CBTime, 4, 0, 1, 1)
        self.LTime = QtGui.QLabel(self.gridLayoutWidget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LTime.sizePolicy().hasHeightForWidth())
        self.LTime.setSizePolicy(sizePolicy)
        self.LTime.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LTime.setFont(font)
        self.LTime.setLineWidth(1)
        self.LTime.setScaledContents(False)
        self.LTime.setAlignment(QtCore.Qt.AlignCenter)
        self.LTime.setObjectName(_fromUtf8("LTime"))
        self.gridLayout_7.addWidget(self.LTime, 3, 0, 1, 1)
        self.tabWidget1.addTab(self.TCam, _fromUtf8(""))
        self.TTerminal = QtGui.QWidget()
        self.TTerminal.setObjectName(_fromUtf8("TTerminal"))
        self.LETerminal = extQLineEdit(self.TTerminal)
        self.LETerminal.setGeometry(QtCore.QRect(10, 490, 831, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LETerminal.setFont(font)
        self.LETerminal.setText(_fromUtf8(""))
        self.LETerminal.setObjectName(_fromUtf8("LETerminal"))
        self.LWTerminal = QtGui.QListWidget(self.TTerminal)
        self.LWTerminal.setGeometry(QtCore.QRect(10, 20, 1001, 461))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LWTerminal.setFont(font)
        self.LWTerminal.setStyleSheet(_fromUtf8(""))
        self.LWTerminal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.LWTerminal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.LWTerminal.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.LWTerminal.setProperty("showDropIndicator", False)
        self.LWTerminal.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.LWTerminal.setObjectName(_fromUtf8("LWTerminal"))
        self.BTerminal = QtGui.QPushButton(self.TTerminal)
        self.BTerminal.setGeometry(QtCore.QRect(850, 490, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BTerminal.setFont(font)
        self.BTerminal.setObjectName(_fromUtf8("BTerminal"))
        self.BTerminal.raise_()
        self.LETerminal.raise_()
        self.LWTerminal.raise_()
        self.tabWidget1.addTab(self.TTerminal, _fromUtf8(""))
        self.clavier = QtGui.QFrame(Frame)
        self.clavier.setGeometry(QtCore.QRect(0, 60, 1024, 541))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setItalic(True)
        self.clavier.setFont(font)
        self.clavier.setStyleSheet(_fromUtf8("QFrame{\n"
"    background: #fafafa;\n"
"}\n"
"QPushButton{\n"
"    background-color: #8c8c8c;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 15px;\n"
"    border-color: beige;\n"
"    font: bold 20px;\n"
"    padding: 10;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QProgressBar {\n"
"    background-color: (0,255,0);\n"
"    color: red;\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #38e000;\n"
"    width: 20px;\n"
"}"))
        self.clavier.setFrameShape(QtGui.QFrame.StyledPanel)
        self.clavier.setFrameShadow(QtGui.QFrame.Raised)
        self.clavier.setObjectName(_fromUtf8("clavier"))
        self.verticalLayoutWidget = QtGui.QWidget(self.clavier)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 70, 171, 471))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.PBCG = QtGui.QPushButton(self.verticalLayoutWidget)
        self.PBCG.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCG.setFont(font)
        self.PBCG.setObjectName(_fromUtf8("PBCG"))
        self.verticalLayout.addWidget(self.PBCG)
        self.PBCM = QtGui.QPushButton(self.verticalLayoutWidget)
        self.PBCM.setMinimumSize(QtCore.QSize(0, 200))
        self.PBCM.setObjectName(_fromUtf8("PBCM"))
        self.verticalLayout.addWidget(self.PBCM)
        self.LEClavier = QtGui.QLineEdit(self.clavier)
        self.LEClavier.setGeometry(QtCore.QRect(10, 10, 791, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setItalic(True)
        self.LEClavier.setFont(font)
        self.LEClavier.setText(_fromUtf8(""))
        self.LEClavier.setObjectName(_fromUtf8("LEClavier"))
        self.gridLayoutWidget = QtGui.QWidget(self.clavier)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(700, 70, 321, 381))
        self.gridLayoutWidget.setMinimumSize(QtCore.QSize(0, 60))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.PBC8 = QtGui.QPushButton(self.gridLayoutWidget)
        self.PBC8.setMinimumSize(QtCore.QSize(0, 60))
        self.PBC8.setObjectName(_fromUtf8("PBC8"))
        self.gridLayout.addWidget(self.PBC8, 0, 1, 1, 1)
        self.PBC9 = QtGui.QPushButton(self.gridLayoutWidget)
        self.PBC9.setMinimumSize(QtCore.QSize(0, 60))
        self.PBC9.setObjectName(_fromUtf8("PBC9"))
        self.gridLayout.addWidget(self.PBC9, 0, 2, 1, 1)
        self.PBC5 = QtGui.QPushButton(self.gridLayoutWidget)
        self.PBC5.setMinimumSize(QtCore.QSize(0, 60))
        self.PBC5.setObjectName(_fromUtf8("PBC5"))
        self.gridLayout.addWidget(self.PBC5, 1, 1, 1, 1)
        self.PBC4 = QtGui.QPushButton(self.gridLayoutWidget)
        self.PBC4.setMinimumSize(QtCore.QSize(0, 60))
        self.PBC4.setObjectName(_fromUtf8("PBC4"))
        self.gridLayout.addWidget(self.PBC4, 1, 0, 1, 1)
        self.PBC2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.PBC2.setMinimumSize(QtCore.QSize(0, 60))
        self.PBC2.setObjectName(_fromUtf8("PBC2"))
        self.gridLayout.addWidget(self.PBC2, 2, 1, 1, 1)
        self.PBC3 = QtGui.QPushButton(self.gridLayoutWidget)
        self.PBC3.setMinimumSize(QtCore.QSize(0, 60))
        self.PBC3.setObjectName(_fromUtf8("PBC3"))
        self.gridLayout.addWidget(self.PBC3, 2, 2, 1, 1)
        self.PBC7 = QtGui.QPushButton(self.gridLayoutWidget)
        self.PBC7.setMinimumSize(QtCore.QSize(0, 60))
        self.PBC7.setObjectName(_fromUtf8("PBC7"))
        self.gridLayout.addWidget(self.PBC7, 0, 0, 1, 1)
        self.PBC1 = QtGui.QPushButton(self.gridLayoutWidget)
        self.PBC1.setMinimumSize(QtCore.QSize(0, 60))
        self.PBC1.setObjectName(_fromUtf8("PBC1"))
        self.gridLayout.addWidget(self.PBC1, 2, 0, 1, 1)
        self.PBC6 = QtGui.QPushButton(self.gridLayoutWidget)
        self.PBC6.setMinimumSize(QtCore.QSize(0, 60))
        self.PBC6.setObjectName(_fromUtf8("PBC6"))
        self.gridLayout.addWidget(self.PBC6, 1, 2, 1, 1)
        self.PBC0 = QtGui.QPushButton(self.gridLayoutWidget)
        self.PBC0.setMinimumSize(QtCore.QSize(0, 60))
        self.PBC0.setObjectName(_fromUtf8("PBC0"))
        self.gridLayout.addWidget(self.PBC0, 3, 1, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(self.clavier)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(700, 450, 321, 91))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.PBCAnnuler = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.PBCAnnuler.setMinimumSize(QtCore.QSize(0, 80))
        self.PBCAnnuler.setObjectName(_fromUtf8("PBCAnnuler"))
        self.horizontalLayout.addWidget(self.PBCAnnuler)
        self.PBCEntrer = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.PBCEntrer.setMinimumSize(QtCore.QSize(0, 80))
        self.PBCEntrer.setObjectName(_fromUtf8("PBCEntrer"))
        self.horizontalLayout.addWidget(self.PBCEntrer)
        self.PBCSuppr = QtGui.QPushButton(self.clavier)
        self.PBCSuppr.setGeometry(QtCore.QRect(880, 10, 131, 51))
        self.PBCSuppr.setObjectName(_fromUtf8("PBCSuppr"))
        self.PBCDel = QtGui.QPushButton(self.clavier)
        self.PBCDel.setGeometry(QtCore.QRect(810, 10, 61, 51))
        self.PBCDel.setObjectName(_fromUtf8("PBCDel"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.clavier)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(180, 70, 511, 471))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.PBCH = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCH.sizePolicy().hasHeightForWidth())
        self.PBCH.setSizePolicy(sizePolicy)
        self.PBCH.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCH.setFont(font)
        self.PBCH.setObjectName(_fromUtf8("PBCH"))
        self.gridLayout_3.addWidget(self.PBCH, 3, 1, 1, 1)
        self.PBCC = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCC.sizePolicy().hasHeightForWidth())
        self.PBCC.setSizePolicy(sizePolicy)
        self.PBCC.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCC.setFont(font)
        self.PBCC.setObjectName(_fromUtf8("PBCC"))
        self.gridLayout_3.addWidget(self.PBCC, 3, 0, 1, 1)
        self.PBCI = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCI.sizePolicy().hasHeightForWidth())
        self.PBCI.setSizePolicy(sizePolicy)
        self.PBCI.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCI.setFont(font)
        self.PBCI.setObjectName(_fromUtf8("PBCI"))
        self.gridLayout_3.addWidget(self.PBCI, 2, 1, 1, 1)
        self.PBCEspace = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.PBCEspace.setMinimumSize(QtCore.QSize(0, 60))
        self.PBCEspace.setText(_fromUtf8(""))
        self.PBCEspace.setObjectName(_fromUtf8("PBCEspace"))
        self.gridLayout_3.addWidget(self.PBCEspace, 4, 0, 1, 3)
        self.PBCY = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCY.sizePolicy().hasHeightForWidth())
        self.PBCY.setSizePolicy(sizePolicy)
        self.PBCY.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCY.setFont(font)
        self.PBCY.setObjectName(_fromUtf8("PBCY"))
        self.gridLayout_3.addWidget(self.PBCY, 0, 1, 1, 1)
        self.PBCX = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCX.sizePolicy().hasHeightForWidth())
        self.PBCX.setSizePolicy(sizePolicy)
        self.PBCX.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCX.setFont(font)
        self.PBCX.setObjectName(_fromUtf8("PBCX"))
        self.gridLayout_3.addWidget(self.PBCX, 0, 0, 1, 1)
        self.PBCD = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCD.sizePolicy().hasHeightForWidth())
        self.PBCD.setSizePolicy(sizePolicy)
        self.PBCD.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCD.setFont(font)
        self.PBCD.setObjectName(_fromUtf8("PBCD"))
        self.gridLayout_3.addWidget(self.PBCD, 2, 2, 1, 1)
        self.PBCS = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCS.sizePolicy().hasHeightForWidth())
        self.PBCS.setSizePolicy(sizePolicy)
        self.PBCS.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCS.setFont(font)
        self.PBCS.setObjectName(_fromUtf8("PBCS"))
        self.gridLayout_3.addWidget(self.PBCS, 1, 1, 1, 1)
        self.PBCE = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCE.sizePolicy().hasHeightForWidth())
        self.PBCE.setSizePolicy(sizePolicy)
        self.PBCE.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCE.setFont(font)
        self.PBCE.setObjectName(_fromUtf8("PBCE"))
        self.gridLayout_3.addWidget(self.PBCE, 1, 0, 1, 1)
        self.PBCT = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCT.sizePolicy().hasHeightForWidth())
        self.PBCT.setSizePolicy(sizePolicy)
        self.PBCT.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCT.setFont(font)
        self.PBCT.setObjectName(_fromUtf8("PBCT"))
        self.gridLayout_3.addWidget(self.PBCT, 3, 2, 1, 1)
        self.PBCZ = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCZ.sizePolicy().hasHeightForWidth())
        self.PBCZ.setSizePolicy(sizePolicy)
        self.PBCZ.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCZ.setFont(font)
        self.PBCZ.setFlat(False)
        self.PBCZ.setObjectName(_fromUtf8("PBCZ"))
        self.gridLayout_3.addWidget(self.PBCZ, 0, 2, 1, 1)
        self.PBCF = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCF.sizePolicy().hasHeightForWidth())
        self.PBCF.setSizePolicy(sizePolicy)
        self.PBCF.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCF.setFont(font)
        self.PBCF.setObjectName(_fromUtf8("PBCF"))
        self.gridLayout_3.addWidget(self.PBCF, 1, 2, 1, 1)
        self.PBCP = QtGui.QPushButton(self.gridLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBCP.sizePolicy().hasHeightForWidth())
        self.PBCP.setSizePolicy(sizePolicy)
        self.PBCP.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PBCP.setFont(font)
        self.PBCP.setObjectName(_fromUtf8("PBCP"))
        self.gridLayout_3.addWidget(self.PBCP, 2, 0, 1, 1)
        self.clavier.raise_()
        self.tabWidget1.raise_()

        self.retranslateUi(Frame)
        self.tabWidget1.setCurrentIndex(3)
        QtCore.QObject.connect(self.PBCAnnuler, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clavier.hide)
        QtCore.QObject.connect(self.PBCAnnuler, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tabWidget1.show)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.labeletatprinteuse.setText(_translate("Frame", "Etat  :  ", None))
        self.labelprofileprinteuse.setText(_translate("Frame", "Profile Imprimante  :", None))
        self.BConnect.setText(_translate("Frame", "Connection", None))
        self.BDisconect.setText(_translate("Frame", "Deconnecte", None))
        self.BConectRafr.setText(_translate("Frame", "Rafraichir", None))
        self.RBSysteme.setText(_translate("Frame", "Systeme", None))
        self.RBRedeem.setText(_translate("Frame", "Redeem", None))
        self.PBArret.setText(_translate("Frame", "Arreter", None))
        self.PBReboot.setText(_translate("Frame", "Redemmarer", None))
        self.RBOcto.setText(_translate("Frame", "Octoprint", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.TConnect), _translate("Frame", "Connexion", None))
        self.BPause.setText(_translate("Frame", "Pause", None))
        self.BStop.setText(_translate("Frame", "Stop", None))
        self.BLoadPrint.setText(_translate("Frame", "Load", None))
        self.BPlay.setText(_translate("Frame", "Play", None))
        self.BPrint.setText(_translate("Frame", "Print", None))
        self.labelfilament.setText(_translate("Frame", "Filament  :", None))
        self.labelnom.setText(_translate("Frame", "Nom  :", None))
        self.labeltempasser.setText(_translate("Frame", "Temps passé  :", None))
        self.labeltempsetsitmer.setText(_translate("Frame", "Temps estimé  :", None))
        self.labeltempsrestant.setText(_translate("Frame", "Temps restant  :", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.TPrint), _translate("Frame", "Print", None))
        self.LTemBedC.setText(_translate("Frame", "Cible :  0", None))
        self.BSetExtru.setText(_translate("Frame", "Extruder", None))
        self.LTemExC.setText(_translate("Frame", "Cible :  0", None))
        self.LTemEx_.setText(_translate("Frame", "Actuel :", None))
        self.LTemBed_.setText(_translate("Frame", "Actuel :", None))
        self.PBExtruOff.setText(_translate("Frame", "Off", None))
        self.BSetBed.setText(_translate("Frame", "Bed", None))
        self.PBBedOff.setText(_translate("Frame", "Off", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.TTemp), _translate("Frame", "Température", None))
        self.BFlux.setText(_translate("Frame", "Flux", None))
        self.LTFlux.setText(_translate("Frame", "100", None))
        self.BVitesse.setText(_translate("Frame", "Vitesse", None))
        self.LTVitesse.setText(_translate("Frame", "100", None))
        self.BFan.setText(_translate("Frame", "Ventilation", None))
        self.LTFan.setText(_translate("Frame", "0", None))
        self.PBAlimOn.setText(_translate("Frame", "On", None))
        self.LAlim.setText(_translate("Frame", "Alimentation", None))
        self.PBAlimOff.setText(_translate("Frame", "Off", None))
        self.BFOFF.setText(_translate("Frame", "Fan off", None))
        self.BZZU.setText(_translate("Frame", "0.01", None))
        self.BZU.setText(_translate("Frame", "0.1", None))
        self.BU.setText(_translate("Frame", "1", None))
        self.BD.setText(_translate("Frame", "10", None))
        self.BC.setText(_translate("Frame", "100", None))
        self.BX.setText(_translate("Frame", "X", None))
        self.BX_2.setText(_translate("Frame", "X-", None))
        self.BY_2.setText(_translate("Frame", "Y-", None))
        self.BY.setText(_translate("Frame", "Y", None))
        self.BZ.setText(_translate("Frame", "Z", None))
        self.BZ_2.setText(_translate("Frame", "Z-", None))
        self.BED.setText(_translate("Frame", "10", None))
        self.BRetra.setText(_translate("Frame", "Retract", None))
        self.BExtru.setText(_translate("Frame", "Extrude", None))
        self.BECent.setText(_translate("Frame", "100", None))
        self.BEC.setText(_translate("Frame", "5", None))
        self.BMotor.setText(_translate("Frame", "Moteur Off", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.TControl), _translate("Frame", "Control", None))
        self.BSaveTime.setText(_translate("Frame", "Sauver", None))
        self.BRafCam.setText(_translate("Frame", "Rafraichir", None))
        self.LDerImg.setText(_translate("Frame", "Derniere image", None))
        self.LFps.setText(_translate("Frame", "fps", None))
        self.LTime.setText(_translate("Frame", "Timelaps On/Off", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.TCam), _translate("Frame", "Caméra", None))
        self.BTerminal.setText(_translate("Frame", "Envoyer", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.TTerminal), _translate("Frame", "Terminal", None))
        self.PBCG.setText(_translate("Frame", "G", None))
        self.PBCM.setText(_translate("Frame", "M", None))
        self.PBC8.setText(_translate("Frame", "8", None))
        self.PBC9.setText(_translate("Frame", "9", None))
        self.PBC5.setText(_translate("Frame", "5", None))
        self.PBC4.setText(_translate("Frame", "4", None))
        self.PBC2.setText(_translate("Frame", "2", None))
        self.PBC3.setText(_translate("Frame", "3", None))
        self.PBC7.setText(_translate("Frame", "7", None))
        self.PBC1.setText(_translate("Frame", "1", None))
        self.PBC6.setText(_translate("Frame", "6", None))
        self.PBC0.setText(_translate("Frame", "0", None))
        self.PBCAnnuler.setText(_translate("Frame", "Annuler", None))
        self.PBCEntrer.setText(_translate("Frame", "Entrer", None))
        self.PBCSuppr.setText(_translate("Frame", "suppr", None))
        self.PBCDel.setText(_translate("Frame", "DEL", None))
        self.PBCH.setText(_translate("Frame", "H", None))
        self.PBCC.setText(_translate("Frame", "C", None))
        self.PBCI.setText(_translate("Frame", "I", None))
        self.PBCY.setText(_translate("Frame", "Y", None))
        self.PBCX.setText(_translate("Frame", "X", None))
        self.PBCD.setText(_translate("Frame", "D", None))
        self.PBCS.setText(_translate("Frame", "S", None))
        self.PBCE.setText(_translate("Frame", "E", None))
        self.PBCT.setText(_translate("Frame", "T", None))
        self.PBCZ.setText(_translate("Frame", "Z", None))
        self.PBCF.setText(_translate("Frame", "F", None))
        self.PBCP.setText(_translate("Frame", "P", None))

from PyQt4 import QtWebKit
from eventclavier import extQLineEdit
from pyqtgraph import PlotWidget
import alex_rc
