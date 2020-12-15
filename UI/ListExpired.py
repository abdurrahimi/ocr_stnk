import sys 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui     import QFont
from PyQt5.QtCore    import QRect,QCoreApplication, QMetaObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QPushButton, QStatusBar, QTreeView, QWidget, QTableWidgetItem
from Model.mUser import mUser
from Controller import cListExpired
import datetime

class listExpiredUI(QMainWindow):
    def __init__(self, parent=None):
        super(listExpiredUI, self).__init__(parent)
        self.resize(900, 700)
        self.setupUi()
       
    def setupUi(self):     
        self.setObjectName("MainWindow")  
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 810, 520))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(["Id STNK", "Nomor Registrasi", "Nama Pemilik", "Masa Berlaku"])
        self.tableWidget.setEditTriggers(QTreeView.NoEditTriggers)
        self.tableWidget.setStyleSheet("background-color:#ECEBE4")  
        data_df = self.load_data()
        for data in data_df:
            self.tableWidget.setItem(data[0],data[1], data[2])
        
        #self.btnHapus = QPushButton(self.centralwidget)
        #self.btnHapus.setGeometry(QtCore.QRect(28, 600, 90, 30)) 
        #self.btnHapus.setObjectName("btnHapus")
        #self.setCentralWidget(self.centralwidget)
        #self.btnHapus.clicked.connect()
                        
        self.btnKembali = QPushButton(self.centralwidget)
        self.btnKembali.setGeometry(QtCore.QRect(750, 600, 90, 30))
        self.btnKembali.setStyleSheet("background-color:#3498DB")  
        self.btnKembali.setObjectName("btnKembali")
        self.setCentralWidget(self.centralwidget)
        self.btnKembali.clicked.connect(self.kembali)
       
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()  
        QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "List Expired"))
        self.btnKembali.setText(_translate("MainWindow", "Kembali"))
        #self.btnHapus.setText(_translate("MainWindow", "Hapus"))
   
    def load_data(self):
        model= mUser()
        datenya = datetime.datetime.today() + datetime.timedelta(30)
        data = model.getData("stnk", "where masa_berlaku < '%s'"%datenya)
        key_data = list(data.keys())
        len_data = len(data[key_data[0]])
        data_return = []
        for row in range(len_data):
            for col in range(len(key_data)):
                value = QTableWidgetItem(str(data[key_data[col]][row]))
                data_return.append((row, col, value))
            
        return data_return
        
    """       
    def _removerow(self):
        row = self.tableWidget.currentRow()
        '''query = 
        "DELETE FROM  WHERE  = ?"
        cur.execute(query, (item,customerId,date,qty))
        con.commit()
        '''
        self.tableWidget.removeRow(row)
        print("Berhasil Hapus!")
    """

    def kembali(self):
        dash = cListExpired.cListExpired()
        dash.gotodash(self)