# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Weather_API.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from decimal import Decimal
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Find_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Find_Button.setGeometry(QtCore.QRect(550, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Find_Button.setFont(font)
        self.Find_Button.setObjectName("Find_Button")
        
        self.Search_Bar = QtWidgets.QTextEdit(self.centralwidget)
        self.Search_Bar.setGeometry(QtCore.QRect(90, 60, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Search_Bar.setFont(font)
        self.Search_Bar.setObjectName("Search_Bar")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 140, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.Current_Status = QtWidgets.QLabel(self.centralwidget)
        self.Current_Status.setGeometry(QtCore.QRect(200, 140, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Current_Status.setFont(font)
        self.Current_Status.setObjectName("Current_Status")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 210, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 270, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 330, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 390, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.Temp_Status = QtWidgets.QLabel(self.centralwidget)
        self.Temp_Status.setGeometry(QtCore.QRect(290, 210, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Temp_Status.setFont(font)
        self.Temp_Status.setObjectName("Temp_Status")
        
        self.Humidity_Status = QtWidgets.QLabel(self.centralwidget)
        self.Humidity_Status.setGeometry(QtCore.QRect(290, 270, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Humidity_Status.setFont(font)
        self.Humidity_Status.setObjectName("Humidity_Status")
        
        self.Pressure_Status = QtWidgets.QLabel(self.centralwidget)
        self.Pressure_Status.setGeometry(QtCore.QRect(290, 330, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Pressure_Status.setFont(font)
        self.Pressure_Status.setObjectName("Pressure_Status")
        
        self.WindSpeed_Status = QtWidgets.QLabel(self.centralwidget)
        self.WindSpeed_Status.setGeometry(QtCore.QRect(290, 390, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.WindSpeed_Status.setFont(font)
        self.WindSpeed_Status.setObjectName("WindSpeed_Status")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        """Search Button"""
        self.Find_Button.clicked.connect(self.requestAPI)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Find_Button.setText(_translate("MainWindow", "Find"))
        self.Search_Bar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5f5f5f;\">London</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Status :"))
        self.Current_Status.setText(_translate("MainWindow", "Disconnected"))
        self.label_3.setText(_translate("MainWindow", "Temperature :"))
        self.label_4.setText(_translate("MainWindow", "Humidity :"))
        self.label_5.setText(_translate("MainWindow", "Pressure :"))
        self.label_6.setText(_translate("MainWindow", "Wind Speed :"))
        self.Temp_Status.setText(_translate("MainWindow", "Unavailable"))
        self.Humidity_Status.setText(_translate("MainWindow", "Unavailable"))
        self.Pressure_Status.setText(_translate("MainWindow", "Unavailable"))
        self.WindSpeed_Status.setText(_translate("MainWindow", "Unavailable"))
        
    """Code Begin Here"""
    
    def requestAPI(self) :
        
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        API_KEY = "9d0b9d6e781510cf4b47c6796371f605"
        CITY = self.Search_Bar.toPlainText()

        url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
        response = requests.get(url).json()
        temperature = response['main']['temp'] - 273.15
    
        
        if response['cod'] == 200 :
            self.Current_Status.setText('Connected')
            
            self.Temp_Status.setText(f'{temperature:.2f}°C')
            """self.Temp_Status.setText(str(response['main']['temp'] - 273.15) + " °C")"""
            self.Humidity_Status.setText(str(response['main']['humidity']) + " %")
            self.Pressure_Status.setText(str(response['main']['pressure']) + " hPa")
            self.WindSpeed_Status.setText(str(response['wind']['speed']) + " meter/sec")
            
        else :
            self.Current_Status.setText(response['message'].capitalize())

    
    """Code End Here"""


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

