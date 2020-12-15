from PyQt5.QtWidgets import QApplication,QMessageBox
from UI import dashboard
from UI import editAdmin,ListAdmin
from Model import mUser
#from UI.ListAdmin    import listAdminUI
import sys

class cListAdmin(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)
        self.ui = listAdminUI(obj)
        self.ui.setVisible(True)
        sys.exit(app.exec_())

    def editData(self,obj):
        dash = editAdmin.editAdminUI(obj)
        obj.hide()
        dash.retrieve(obj)
        dash.show()

    def hapusData(self,obj):
        model= mUser.mUser()
        data = model.deleteData("setup_admin", "WHERE id_admin = %s"%(obj.value))
        msg = QMessageBox()
        if(data):
            msg.about(obj, "Success", "Berhasil Menghapus Data")
        else:
            msg.about(obj, "Fail", "Gagal Menghapus Data")
        dash = ListAdmin.listAdminUI(obj)
        obj.hide()
        dash.show()

    def gotodash(self,obj):
        dash = dashboard.dashboardUI(obj)
        obj.hide()
        dash.show()