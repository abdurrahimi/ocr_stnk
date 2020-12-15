import sys
from PyQt5           import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget,QPushButton,  QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore    import QRect,QCoreApplication, QMetaObject
from Controller      import cEditDataSTNK
from Model           import mUser

class editDataSTNKUI(QMainWindow):
    def __init__(self, parent=None):
        super(editDataSTNKUI, self).__init__(parent)
        self.resize(500, 200)
        self.setupUi()
    
    def setupUi(self):        
        self.setObjectName("MainWindow") 
        
        self.label = QLabel(self)  
        self.label.setGeometry(QRect(30, 5, 171, 51))  
        self.label.setStyleSheet("color: rgb(23, 32, 42 );")  
        self.label.setObjectName("label")  
        
        self.label2 = QLabel(self)  
        self.label2.setGeometry(QRect(30, 30, 171, 51))  
        self.label2.setStyleSheet("color: rgb(23, 32, 42 );")  
        self.label2.setObjectName("label2")  
        
        self.label3 = QLabel(self)  
        self.label3.setGeometry(QRect(30, 55, 171, 51))  
        self.label3.setStyleSheet("color: rgb(23, 32, 42 );")  
        self.label3.setObjectName("label3")  
        
        self.label4 = QLabel(self)  
        self.label4.setGeometry(QRect(30, 80, 171, 51))  
        self.label4.setStyleSheet("color: rgb(23, 32, 42 );")  
        self.label4.setObjectName("label4")  
        
        #self.idSTNK = QLineEdit(self)  
        #self.idSTNK.setGeometry(QRect(130, 20, 350, 20))  
        #self.idSTNK.setObjectName("idSTNK")
        
        self.nomorRegis = QLineEdit(self)  
        self.nomorRegis.setGeometry(QRect(130, 45, 350, 20))  
        self.nomorRegis.setObjectName("nomorRegis")
        
        self.namaPemilik = QLineEdit(self)  
        self.namaPemilik.setGeometry(QRect(130, 95, 350, 20))  
        self.namaPemilik.setObjectName("namaPemilik")
        
        self.masaBerlaku = QLineEdit(self)  
        self.masaBerlaku.setGeometry(QRect(130, 70, 350, 20))  
        self.masaBerlaku.setObjectName("masaBerlaku")
        
        self.btnOk = QPushButton(self)
        self.btnOk.setGeometry(QtCore.QRect(380, 150, 50, 30))  
        self.btnOk.setObjectName("btnOk")
        self.btnOk.clicked.connect(self.handleActivated)
        
        self.btnCancel = QPushButton(self)
        self.btnCancel.setGeometry(QtCore.QRect(430, 150, 50, 30))  
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.clicked.connect(self.cancel)
        
        self.retranslateUi()  
        QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Edit Data STNK"))
        #self.label.setText(_translate("MainWindow", "ID STNK"))
        self.label2.setText(_translate("MainWindow", "Nomor Registrasi"))
        self.label3.setText(_translate("MainWindow", "Nama Pemilik"))
        self.label4.setText(_translate("MainWindow", "Masa Berlaku"))
        self.btnOk.setText(_translate("MainWindow", "Ok"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))


    def retrieve(self, obj):
        self.id_stnk = obj.value
        model= mUser.mUser()
        data = model.getData("stnk", "WHERE id_stnk = %s"%(obj.value))
        key_data = list(data.keys())
        #print(key_data)
        len_data = len(data[key_data[0]])
        data_return = []
        for row in range(len_data):
            self.nomorRegis.setText(data["nomor_registrasi"][row])
            self.namaPemilik.setText(data["nama_pemilik"][row])
            self.masaBerlaku.setText(data["masa_berlaku"][row].strftime('%Y-%m-%d'))

    def handleActivated(self,obj):
        edit  = cEditDataSTNK.cEditDataSTNK()
        edit.update(self)

    def cancel(self,obj):
        edit  = cEditDataSTNK.cEditDataSTNK()
        edit.cancel(self)
        