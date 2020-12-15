from PyQt5.QtWidgets import QApplication, QMessageBox
#from UI.Loguser      import logUserUI
from UI import dashboard
from UI import Loguser
from Model import mUser
import sys

class cLogUser(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)
        self.ui = logUserUI(obj)
        self.ui.setVisible(True)
        sys.exit(app.exec_())

    def gotodash(self,obj):
        dash = dashboard.dashboardUI(obj)
        obj.hide()
        dash.show()

    def hapusData(self,obj):
        model= mUser.mUser()
        data = model.deleteData("log_user", "WHERE id_log = %s"%(obj.value))
        msg = QMessageBox()
        if(data):
            msg.about(obj, "Success", "Berhasil Menghapus Data")
        else:
            msg.about(obj, "Fail", "Gagal Menghapus Data")
        dash = Loguser.logUserUI(obj)
        obj.hide()
        dash.show()