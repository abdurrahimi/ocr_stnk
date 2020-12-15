from PyQt5.QtWidgets  import QApplication, QMessageBox
#from UI.inputDataSTNK import inputDataSTNKUI
from UI import verifikasiInputSTNK
import ocrProcess
import sys

class cInputDataSTNK(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)
        self.dash = inputDataSTNKUI(obj)
        self.dash.show()
        sys.exit(app.exec_())
    
    def uploadImage(self,obj):
    	#img = obj.filePath
        dash = verifikasiInputSTNK.verifikasiInputSTNKUI(obj)
        #obj.hide()
        dash.retrieve(obj)
        dash.show()
    	#print(img)
