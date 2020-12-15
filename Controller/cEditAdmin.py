from PyQt5.QtWidgets import QApplication, QMessageBox
from UI import editAdmin
from UI import ListAdmin
from Model import mUser
import sys

class cEditAdmin(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)  
        self.ui = editAdmin.editAdminUI(obj)    
        self.ui.setVisible(True)
        sys.exit(app.exec_())

    def getDataRole(self):
        model= mUser()
        data = model.getData("setup_role", "ORDER BY id_role")
        key_data = list(data.keys())
        len_data = len(data[key_data[0]])
        data_return = []
        for row in range(len_data):
            for col in range(len(key_data)):
                value = QTableWidgetItem(str(data[key_data[col]][row]))
                data_return.append((row, col, value))
          
        return data_return

    def cancel(self,obj):
        ui = ListAdmin.listAdminUI(obj)
        obj.hide()
        ui.show()

    def update(self,obj):
        model= mUser.mUser()
        index   = obj.combo.currentIndex()
        role    = obj.combo.itemData(index)
        user    = obj.namaPengguna.text()
        nama    = obj.namaLengkap.text()
        sandi   = obj.kataSandi.text()
        id_admin = obj.idUser
        data    = [id_admin,role,user,sandi,nama,1,'2020-04-03',id_admin]
        res = model.updateAdminData('setup_admin',data)
        msg = QMessageBox()
        if(res):
            msg.about(obj, "Success", "Berhasil Menginput Data")
        else:
            msg.about(obj, "Fail", "Gagal Menginput Data")
        print(res)
        ui = ListAdmin.listAdminUI(obj)
        obj.hide()
        ui.show()