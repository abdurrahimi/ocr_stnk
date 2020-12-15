from PyQt5.QtWidgets import QApplication,QMessageBox
from UI import ListSTNK
from UI import dashboard
from UI import editDataSTNK
from Model import mUser
import sys

class cListSTNK(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)  
        self.ui = ListSTNK.listStnkUI(obj)    
        self.ui.setVisible(True)
        sys.exit(app.exec_())
  
    def getBack(self, obj):
        ui = dashboard.dashboardUI(obj)
        obj.hide()
        ui.show()
        
    def getUpdate(self, obj):
        ui = editDataSTNK.editDataSTNKUI(obj)
        obj.hide()
        ui.show()

    def editData(self,obj):
        dash = editDataSTNK.editDataSTNKUI(obj)
        obj.hide()
        dash.retrieve(obj)
        dash.show()

    def hapusData(self,obj):
        model= mUser.mUser()
        data = model.deleteData("stnk", "WHERE id_stnk = %s"%(obj.value))
        msg = QMessageBox()
        if(data):
            msg.about(obj, "Success", "Berhasil Menghapus Data")
        else:
            msg.about(obj, "Fail", "Gagal Menghapus Data")
    
        dash = ListSTNK.listStnkUI(obj)
        obj.hide()
        dash.show()

