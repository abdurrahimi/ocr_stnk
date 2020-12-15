from PyQt5.QtWidgets import QApplication, QMessageBox
#from UI.editRole import editRoleUI
from UI import ListRole
from Model import mUser
import sys

class cEditRole(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)  
        self.ui = editRoleUI(obj)    
        self.ui.setVisible(True)
        sys.exit(app.exec_())

    def cancel(self,obj):
        ui = ListRole.listRoleUI(obj)
        obj.hide()
        ui.show()

    def update(self,obj):
        model= mUser.mUser()
        nama_role    = obj.namaRole.text()
        id_role = obj.idRole
        data    = [id_role,nama_role,id_role]
        res = model.updateRoleData('setup_role',data)
        msg = QMessageBox()
        if(res):
            msg.about(obj, "Success", "Berhasil Menginput Data")
        else:
            msg.about(obj, "Fail", "Gagal Menginput Data")
        print(res)  
        ui = ListRole.listRoleUI(obj)
        obj.hide()
        ui.show()