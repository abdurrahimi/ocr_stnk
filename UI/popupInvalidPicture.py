import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui     import QIcon
from PyQt5.QtCore    import pyqtSlot

def popupInvalidPictureUI():
   msgBox = QMessageBox() 
   msgBox.setIcon(QMessageBox.Information)
   msgBox.setText("Maaf, format harus gambar!")
   msgBox.setWindowTitle("Pop Up Invalid Picture")
   msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      print('OK clicked')
   
def msgButtonClick(i):
   print("Button clicked is:",i.text())