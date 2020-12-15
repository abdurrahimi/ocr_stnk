from PyQt5.QtWidgets import QApplication, QMessageBox
#from UI.ListRole     import listRoleUI
from Model import mUser
from UI import dashboard
from UI import editRole
from UI import ListRole
import sys

class cListRole(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)
        self.ui = listRoleUI(obj)
        self.ui.setVisible(True)
        sys.exit(app.exec_())

    def gotodash(self,obj):
        dash = dashboard.dashboardUI(obj)
        obj.hide()
        dash.show()

    def editData(self,obj):
        dash = editRole.editRoleUI(obj)
        obj.hide()
        dash.retrieve(obj)
        dash.show()

    def hapusData(self,obj):
        model= mUser.mUser()
        data = model.deleteData("setup_role", "WHERE id_role = %s"%(obj.value))
        msg = QMessageBox()
        if(data):
            msg.about(obj, "Success", "Berhasil Menghapus Data")
        else:
            msg.about(obj, "Fail", "Gagal Menghapus Data")
        dash = ListRole.listRoleUI(obj)
        obj.hide()
        dash.show()