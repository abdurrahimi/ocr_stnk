import sys 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui     import QFont
from PyQt5.QtCore    import QRect,QCoreApplication, QMetaObject
from PyQt5.QtWidgets import QApplication,QMainWindow, QTableWidget, QPushButton, QStatusBar, QTreeView, QWidget, QTableWidgetItem,QMessageBox, QAbstractItemView
from Model.mUser import mUser
from Controller import cListAdmin

class listAdminUI(QMainWindow):
    def __init__(self, parent=None):
        super(listAdminUI, self).__init__(parent)
        self.resize(900, 700)
        self.setupUi()
       
    def setupUi(self):     
        self.setObjectName("MainWindow")  
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 810, 520))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(["Id Admin", "Id Role", "Nama Pengguna",  "Kata Sandi", "Nama Lengkap", "Dibuat Oleh", "Dibuat Tanggal"])
        self.tableWidget.setEditTriggers(QTreeView.NoEditTriggers)
        self.tableWidget.setStyleSheet("background-color:#ECEBE4") 
        data_df = self.load_data()
        for data in data_df:
            self.tableWidget.setItem(data[0],data[1], data[2])

        #self.tableWidget.setEditTriggers(QAbstractItemView.CurrentChanged)
        self.btnHapus = QPushButton(self.centralwidget)
        self.btnHapus.setGeometry(QtCore.QRect(28, 600, 90, 30)) 
        self.btnHapus.setObjectName("btnHapus")
        self.setCentralWidget(self.centralwidget)
        self.btnHapus.clicked.connect(self.hapus)
        
        self.btnEdit = QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(650, 600, 90, 30))
        self.btnEdit.setStyleSheet("background-color:#4DAE4E")  
        self.btnEdit.setObjectName("btnEdit")
        self.setCentralWidget(self.centralwidget)
        self.btnEdit.clicked.connect(self.editData)
                
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
        self.setWindowTitle(_translate("MainWindow", "list Admin"))
        self.btnKembali.setText(_translate("MainWindow", "Kembali"))
        self.btnHapus.setText(_translate("MainWindow", "Hapus"))
        self.btnEdit.setText(_translate("MainWindow", "Ubah"))
        
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

    def load_data(self):
        model= mUser()
        data = model.getData("setup_admin", "ORDER BY id_admin")
        key_data = list(data.keys())
        len_data = len(data[key_data[0]])
        data_return = []
        for row in range(len_data):
            for col in range(len(key_data)):
                value = QTableWidgetItem(str(data[key_data[col]][row]))
                data_return.append((row, col, value))
            
        return data_return

    def editData(self,obj):
        if self.tableWidget.currentIndex().row() > -1:
            index=(self.tableWidget.selectionModel().currentIndex())
            #print(index)
            self.value=index.sibling(index.row(),0).data()
            if(self.value == None):
                QMessageBox.question(self,'Message', "Pilih baris yang akan dihapus!", QMessageBox.Ok)
            else:
                dash = cListAdmin.cListAdmin()
                dash.editData(self)
            #print(value)
        else:
             QMessageBox.question(self,'Message', "Pilih baris yang akan dihapus!", QMessageBox.Ok)
             self.show()

    def hapus(self):
        if self.tableWidget.currentIndex().row() > -1:
            index=(self.tableWidget.selectionModel().currentIndex())
            self.value=index.sibling(index.row(),0).data()
            if(self.value == None):
                QMessageBox.question(self,'Message', "Pilih baris yang akan dihapus!", QMessageBox.Ok)
            else:
                hps = QMessageBox.question(self,'Message', "Hapus Data?", QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
                if(hps == QMessageBox.Yes):
                    dash = cListAdmin.cListAdmin()
                    dash.hapusData(self)
            #print(value)
        else:
             QMessageBox.question(self,'Message', "Pilih baris yang akan dihapus!", QMessageBox.Ok)
             self.show()

    def kembali(self):
        dash = cListAdmin.cListAdmin()
        dash.gotodash(self)