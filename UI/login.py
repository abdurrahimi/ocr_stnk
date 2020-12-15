#from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtGui     import QFont
from PyQt5.QtCore    import QRect,QCoreApplication, QMetaObject
from PyQt5.QtWidgets import QMainWindow, QDialog, QFrame, QLabel, QLineEdit, QPushButton
from Controller import cLogin

class loginUI(QDialog):
    def __init__(self,parent=None):
        super(loginUI, self).__init__(parent)
        self.resize(900, 900)
        self.setupUi()
        
        
    def setupUi(self):  
        self.setObjectName("Dialog")  
        self.resize(900, 900)
      
        self.frame = QFrame(self)  
        self.frame.setGeometry(QRect(200, 100, 500, 500))  
        self.frame.setFrameShape(QFrame.StyledPanel)  
        self.frame.setFrameShadow(QFrame.Raised)  
        self.frame.setObjectName("frame")  
       
        self.label = QLabel(self.frame)  
        self.label.setGeometry(QRect(190, 80, 171, 51))  
        font = QFont()  
        font.setPointSize(20)  
        self.label.setFont(font)  
        self.label.setStyleSheet("color: rgb(23, 32, 42 );")  
        self.label.setObjectName("label")  
       
        self.label_2 = QLabel(self.frame)  
        self.label_2.setGeometry(QRect(50, 190, 121, 31))  
        font = QFont()  
        font.setPointSize(12)  
        self.label_2.setFont(font)  
        self.label_2.setObjectName("label_2")  
       
        self.label_3 = QLabel(self.frame)  
        self.label_3.setGeometry(QRect(50, 260, 121, 21))  
        font = QFont()  
        font.setPointSize(12)  
        self.label_3.setFont(font)  
        self.label_3.setObjectName("label_3")  
       
        self.userName = QLineEdit(self.frame)  
        self.userName.setGeometry(QRect(200, 190, 231, 31))  
        self.userName.setStyleSheet("background-color: rgb(253, 254, 254);")  
        self.userName.setObjectName("userName")
        
        self.userPassword = QLineEdit(self.frame)  
        self.userPassword.setGeometry(QRect(200, 260, 231, 31))  
        self.userPassword.setStyleSheet("background-color: rgb(253, 254, 254);")  
        self.userPassword.setEchoMode(QLineEdit.Password)  
        self.userPassword.setObjectName("userPassword")  
        font = QFont()  
        font.setPointSize(16)    
        
        self.pushButton = QPushButton(self.frame)  
        self.pushButton.setGeometry(QRect(200, 360, 101, 41))  
        self.pushButton.setStyleSheet("background-color:#3498DB")  
        self.pushButton.setObjectName("pushButton")  
        self.pushButton.clicked.connect(self.on_click_pb)

        self.retranslateUi()  
        QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self): 
        #print("Ya")
        _translate = QCoreApplication.translate  
        self.setWindowTitle(_translate("Dialog", "Login"))  
        self.label.setText(_translate("Dialog", "Log in Form"))  
        self.label_2.setText(_translate("Dialog", "Nama Pengguna"))  
        self.label_3.setText(_translate("Dialog", "Kata Sandi"))  
        self.pushButton.setText(_translate("Dialog", "Masuk"))

    def on_click_pb(self, obj):
        #print("masuk sini")
        loginc  = cLogin.cLogin()
        loginc.getLogin(self)
