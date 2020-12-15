import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget,QPushButton,  QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore    import QRect,QCoreApplication, QMetaObject
from Model import mUser
from Controller import cEditRole

class editRoleUI(QMainWindow):
    def __init__(self, parent=None):
        super(editRoleUI, self).__init__(parent)
        self.resize(500, 150)
        self.setupUi()
    
    def setupUi(self):        
        self.setObjectName("MainWindow") 
                
        #self.label = QLabel(self)  
        #self.label.setGeometry(QRect(30, 5, 171, 51))  
        #self.label.setStyleSheet("color: rgb(23, 32, 42 );")  
        #self.label.setObjectName("label")  
        
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
        self.btnOk.clicked.connect(self.handleActivated)
        
        self.btnCancel = QPushButton(self)
        self.btnCancel.setGeometry(QtCore.QRect(430, 100, 50, 30))  
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.clicked.connect(self.cancel)
        
        self.retranslateUi()  
        QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Edit Data Role"))
        #self.label.setText(_translate("MainWindow", "ID Role"))
        self.label2.setText(_translate("MainWindow", "Nama Role"))
        self.btnOk.setText(_translate("MainWindow", "Ok"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))

    def retrieve(self, obj):
        self.idRole = obj.value
        model= mUser.mUser()
        data = model.getData("setup_role", "WHERE id_role = %s"%(obj.value))
        key_data = list(data.keys())
        #print(key_data)
        len_data = len(data[key_data[0]])
        data_return = []
        for row in range(len_data):
            print(data["nama_role"][row])
            self.namaRole.setText(data["nama_role"][row])

    def handleActivated(self,obj):
        edit  = cEditRole.cEditRole()
        edit.update(self)

    def cancel(self,obj):
        edit  = cEditRole.cEditRole()
        edit.cancel(self)
            
            