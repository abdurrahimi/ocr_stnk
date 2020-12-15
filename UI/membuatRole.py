import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget,QPushButton,  QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore    import QRect,QCoreApplication, QMetaObject
from Controller      import cMembuatRole

class membuatRoleUI(QMainWindow):
    def __init__(self, parent=None):
        super(membuatRoleUI, self).__init__(parent)
        self.resize(500, 150)
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
        
        #self.idRole = QLineEdit(self)  
        #self.idRole.setGeometry(QRect(130, 20, 350, 20))  
        #self.idRole.setObjectName("roleID")
        
        self.namaRole = QLineEdit(self)  
        self.namaRole.setGeometry(QRect(130, 45, 350, 20))  
        self.namaRole.setObjectName("namaRole")
        
        self.btnOk = QPushButton(self)
        self.btnOk.setGeometry(QtCore.QRect(380, 100, 50, 30))  
        self.btnOk.setObjectName("btnOk")
        self.btnOk.clicked.connect(self.submit)
        
        self.btnCancel = QPushButton(self)
        self.btnCancel.setGeometry(QtCore.QRect(430, 100, 50, 30))  
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.clicked.connect(self.cancel)
        
        self.retranslateUi()  
        QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Membuat Role"))
        #self.label.setText(_translate("MainWindow", "ID Role"))
        self.label2.setText(_translate("MainWindow", "Nama Role"))
        self.btnOk.setText(_translate("MainWindow", "Ok"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))

    def submit(self,obj):
        buat  = cMembuatRole.cMembuatRole()
        buat.buatRole(self)

    def cancel(self,obj):
        buat  = cMembuatRole.cMembuatRole()
        buat.cancel(self)