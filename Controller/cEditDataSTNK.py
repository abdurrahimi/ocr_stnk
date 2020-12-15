from PyQt5.QtWidgets import QApplication, QMessageBox
from UI import editDataSTNK
from UI import ListSTNK
from Model import mUser
import sys

class cEditDataSTNK(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)  
        self.ui = editDataSTNK.editDataSTNKUI(obj)    
        self.ui.setVisible(True)
        sys.exit(app.exec_())

    def cancel(self,obj):
        ui = ListSTNK.listStnkUI(obj)
        obj.hide()
        ui.show()

    def update(self,obj):
        model= mUser.mUser()
        #nama_role    = obj.namaRole.text()
        nama_pemilik = obj.namaPemilik.text()
        nomor = obj.nomorRegis.text()
        masa = obj.masaBerlaku.text()
        id_stnk = obj.id_stnk
        data    = [nomor,nama_pemilik,masa,id_stnk]
        res = model.updateStnkData('stnk',data)
        msg = QMessageBox()
        if(res):
            msg.about(obj, "Success", "Berhasil Menginput Data")
        else:
            msg.about(obj, "Fail", "Gagal Menginput Data")
        #print(res)  
        ui = ListSTNK.listStnkUI(obj)
        obj.hide()
        ui.show()