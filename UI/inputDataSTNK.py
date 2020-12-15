import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QPushButton, QLabel, QVBoxLayout,QMessageBox
from PyQt5.QtGui     import QPixmap
from PyQt5.QtCore    import QRect,QCoreApplication, QMetaObject
from Controller import cInputDataSTNK

class inputDataSTNKUI(QMainWindow):
    def __init__(self, parent=None):
        super(inputDataSTNKUI, self).__init__(parent)
        self.resize(900, 550)
        self.setupUi()
     
    def setupUi(self):     
        self.setObjectName("MainWindow") 
        self.filePath = ''
        self.btnUnggah = QPushButton(self)
        self.btnUnggah.setGeometry(QtCore.QRect(50, 390, 800, 50))
        self.btnUnggah.setObjectName("btnUnggah")
        self.btnUnggah.setStyleSheet("background-color:#4DAE4E")  
        self.btnUnggah.clicked.connect(self.get_image_file)
        
        self.btnProses = QPushButton(self)
        self.btnProses.setGeometry(QtCore.QRect(50, 450, 800, 50))  
        self.btnProses.setObjectName("btnProses")
        self.btnProses.clicked.connect(self.uploadImage)
        
        self.labelImage = QLabel(self)
        self.labelImage.setGeometry(QtCore.QRect(50, 50, 810, 300))
        self.labelImage.setStyleSheet("background-color:#D5C4C4") 
        self.btnUnggah.setObjectName("labelImage")
        
        self.retranslateUi()  
        QMetaObject.connectSlotsByName(self)
        
    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif)")
        self.filePath = file_name
        self.labelImage.setPixmap(QPixmap(file_name).scaled(810, 300))
        
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Input Data STNK"))
        self.btnUnggah.setText(_translate("MainWindow", "Unggah Gambar"))
        self.btnProses.setText(_translate("MainWindow", "Proses Gambar"))

    def uploadImage(self):
        if(self.filePath == ''):
            QMessageBox.question(self,'Message', "Tidak ada gambar yang di upload!", QMessageBox.Ok)
        else:
            stnkc  = cInputDataSTNK.cInputDataSTNK()
            stnkc.uploadImage(self)
        
