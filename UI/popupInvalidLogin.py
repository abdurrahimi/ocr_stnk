import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui     import QIcon
from PyQt5.QtCore    import pyqtSlot

def popupInvalidLoginUI():
   msgBox = QMessageBox() 
   msgBox.setIcon(QMessageBox.Information)
   msgBox.setText("Nama pengguna atau kata sandi anda salah, silahkan coba lagi!")
   msgBox.setWindowTitle("Pop Up Invalid Login")
   msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      print('OK clicked')
   
def msgButtonClick(i):
   print("Button clicked is:",i.text())