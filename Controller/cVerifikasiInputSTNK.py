from PyQt5.QtWidgets        import QApplication,QMessageBox
#from UI.verifikasiInputSTNK import verifikasiInputSTNKUI
from UI import dashboard
from Model import mUser
import sys

class cVerifikasiInputSTNK(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)  
        self.ui = verifikasiInputSTNKUI(obj)    
        self.ui.setVisible(True)
        sys.exit(app.exec_())


    def simpanData(self,obj):
        model= mUser.mUser()
        nomor    = obj.nomorRegis.text()
        nama    = obj.namaPemilik.text()
        masa   = obj.masaBerlaku.text()
        data    = ['',nomor,nama,masa]
        res = model.insertStnkData(data)
        msg = QMessageBox()
        if(res):
            msg.about(obj, "Success", "Berhasil Menginput Data")
        else:
            msg.about(obj, "Fail", "Gagal Menginput Data")
        #print(res)
        ui = dashboard.dashboardUI(obj)
        obj.hide()
        ui.show()