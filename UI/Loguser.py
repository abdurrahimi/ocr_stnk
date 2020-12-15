import sys 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui     import QFont
from PyQt5.QtCore    import QRect,QCoreApplication, QMetaObject
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QPushButton, QStatusBar, QTreeView, QWidget, QTableWidgetItem, QMessageBox
from Model.mUser import mUser
from Controller import cLogUser

class logUserUI(QMainWindow):
    def __init__(self, parent=None):
        super(logUserUI, self).__init__(parent)
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
        self.tableWidget.setHorizontalHeaderLabels(["Id Log", "Id Admin", "Nama Pengguna", "Tanggal Login"])
        self.tableWidget.setEditTriggers(QTreeView.NoEditTriggers)
        self.tableWidget.setStyleSheet("background-color:#ECEBE4") 
        data_df = self.load_data()
        for data in data_df:
            self.tableWidget.setItem(data[0],data[1], data[2])
            
        self.btnHapus = QPushButton(self.centralwidget)
        self.btnHapus.setGeometry(QtCore.QRect(28, 600, 90, 30)) 
        self.btnHapus.setObjectName("btnHapus")
        self.setCentralWidget(self.centralwidget)
        self.btnHapus.clicked.connect(self.hapus)
                            
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
        self.setWindowTitle(_translate("MainWindow", "Log User"))
        self.btnKembali.setText(_translate("MainWindow", "Kembali"))
        self.btnHapus.setText(_translate("MainWindow", "Hapus"))
        
    def load_data(self):
        model= mUser()
        data = model.getData("log_user", "ORDER BY tanggal_login")
        key_data = list(data.keys())
        len_data = len(data[key_data[0]])
        data_return = []
        for row in range(len_data):
            for col in range(len(key_data)):
                value = QTableWidgetItem(str(data[key_data[col]][row]))
                data_return.append((row, col, value))
            
        return data_return

    def hapus(self):
        if self.tableWidget.currentIndex().row() > -1:
            index=(self.tableWidget.selectionModel().currentIndex())
            self.value=index.sibling(index.row(),0).data()
            if(self.value == None):
                QMessageBox.question(self,'Message', "Pilih baris yang akan dihapus!", QMessageBox.Ok)
            else:
                hps = QMessageBox.question(self,'Message', "Hapus Data?", QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
                if(hps == QMessageBox.Yes):
                    dash = cLogUser.cLogUser()
                    dash.hapusData(self)
            #print(value)
        else:
             QMessageBox.question(self,'Message', "Pilih baris yang akan dihapus!", QMessageBox.Ok)
             self.show()

    def kembali(self):
        dash = cLogUser.cLogUser()
        dash.gotodash(self)