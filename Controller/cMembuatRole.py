from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
#from UI.membuatRole  import membuatRoleUI
from Model    import mUser
from UI import dashboard

import sys

class cMembuatRole(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)
        self.ui = membuatRoleUI(obj)
        self.ui.setVisible(True)
        sys.exit(app.exec_())

    def buatRole(self, obj=None):
        role = obj.namaRole.text()
        data = role
        print(data)
        model = mUser.mUser()
        res = model.insertRoleData('setup_role',data)
        msg = QMessageBox()
        if(res):
            msg.about(obj, "Success", "Berhasil Menginput Data")
        else:
        	msg.about(obj, "Fail", "Gagal Menginput Data")
        print(res)
        ui = dashboard.dashboardUI(obj)
        obj.hide()
        ui.show()

    def cancel(self,obj):
        ui = dashboard.dashboardUI(obj)
        obj.hide()
        ui.show()
