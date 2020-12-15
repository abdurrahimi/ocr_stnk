import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget,QPushButton,  QDialog, QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QVBoxLayout, QComboBox
from PyQt5.QtCore    import QRect,QCoreApplication, QMetaObject
from Model import mUser
from Controller import cEditAdmin

class editAdminUI(QMainWindow):
    def __init__(self, parent=None):
        super(editAdminUI, self).__init__(parent)
        #self.dataNya = obj
        self.resize(500, 200)
        self.setupUi()

    
    def setupUi(self):        
        self.setObjectName("MainWindow") 
                
        self.label = QLabel(self)  
        self.label.setGeometry(QRect(30, 5, 171, 51))  
        self.label.setStyleSheet("color: rgb(23, 32, 42 );")  
        self.label.setObjectName("label")
        #print(self.dataNya)
        # self.labelx = QLabel(self)  
        # self.labelx.setGeometry(QRect(30, 5, 171, 51))  
        # self.labelx.setStyleSheet("color: rgb(23, 32, 42 );")  
        # self.labelx.setObjectName("label")
        
        # self.label2 = QLabel(self)  
        # self.label2.setGeometry(QRect(30, 30, 171, 51))  
        # self.label2.setStyleSheet("color: rgb(23, 32, 42 );")  
        # self.label2.setObjectName("label2")  
        
        self.label3 = QLabel(self)  
        self.label3.setGeometry(QRect(30, 30, 171, 51))  
        self.label3.setStyleSheet("color: rgb(23, 32, 42 );")  
        self.label3.setObjectName("label3")  
        
        self.label4 = QLabel(self)  
        self.label4.setGeometry(QRect(30, 55, 171, 51))  
        self.label4.setStyleSheet("color: rgb(23, 32, 42 );")  
        self.label4.setObjectName("label4")  
        
        self.label5 = QLabel(self)  
        self.label5.setGeometry(QRect(30, 80, 171, 51))  
        self.label5.setStyleSheet("color: rgb(23, 32, 42 );")  
        self.label5.setObjectName("label5")  
        
        self.idRole = QLineEdit(self)  
        self.idRole.setGeometry(QRect(130, 20, 350, 20))  
        self.idRole.setObjectName("roleID")
        
        data = self.getDataRole()
        #print(data)
        self.combo = QComboBox(self)
        
        for value in data :
            #print(value)
            #self.tableWidget.setItem(value[0],value[1], value[2])
            self.combo.addItem(value[0],value[1])

        self.combo.setGeometry(QRect(130, 20, 350, 20))
        #self.combo.activated.connect()
        #self.labelx.move(50, 150)

        #combo.activated[str].connect(self.onActivated)

        
        # self.idAdmin = QLineEdit(self)  
        # self.idAdmin.setGeometry(QRect(130, 45, 350, 20))  
        # self.idAdmin.setObjectName("adminID")
        
        self.namaPengguna = QLineEdit(self)  
        self.namaPengguna.setGeometry(QRect(130, 45, 350, 20))  
        self.namaPengguna.setObjectName("nama")
        
        self.namaLengkap = QLineEdit(self)  
        self.namaLengkap.setGeometry(QRect(130, 70, 350, 20))  
        self.namaLengkap.setObjectName("username")
        
        self.kataSandi = QLineEdit(self)  
        self.kataSandi.setGeometry(QRect(130, 95, 350, 20))  
        self.kataSandi.setObjectName("password")
        
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
        self.setWindowTitle(_translate("MainWindow", "Membuat Admin"))
        self.label.setText(_translate("MainWindow", "ID Role"))
        #self.label2.setText(_translate("MainWindow", "ID Admin"))
        self.label3.setText(_translate("MainWindow", "Nama Pengguna"))
        self.label4.setText(_translate("MainWindow", "Nama Lengkap"))
        self.label5.setText(_translate("MainWindow", "Kata Sandi"))
        self.btnOk.setText(_translate("MainWindow", "Ok"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))

    def getDataRole(self):
        model= mUser.mUser()
        data = model.getData("setup_role", "ORDER BY id_role")
        key_data = list(data.keys())
        #print(key_data)
        len_data = len(data[key_data[0]])
        data_return = []
        for row in range(len_data):
            nama = str(data["nama_role"][row])
            value = str(data["id_role"][row])

            #print(value)
            data_return.append((nama, value))
            
        return data_return

    def retrieve(self, obj):
        self.idUser = obj.value
        model= mUser.mUser()
        data = model.getData("setup_admin", "WHERE id_admin = %s"%(obj.value))
        key_data = list(data.keys())
        #print(key_data)
        len_data = len(data[key_data[0]])
        data_return = []
        for row in range(len_data):
            print(data["nama_pengguna"][row])
            self.namaPengguna.setText(data["nama_pengguna"][row])
            self.namaLengkap.setText(data["nama_lengkap"][row])
            self.kataSandi.setText(data["kata_sandi"][row])
            index = self.combo.findData(int(data["id_role"][row]))
            print(index)
            if ( index != -1 ) :
               self.combo.setCurrentIndex(index);
            

        #self.retranslateUi()  
    def handleActivated(self,obj):
        edit  = cEditAdmin.cEditAdmin()
        edit.update(self)

    def cancel(self,obj):
        edit  = cEditAdmin.cEditAdmin()
        edit.cancel(self)
        