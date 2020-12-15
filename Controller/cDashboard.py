from PyQt5.QtWidgets  import QApplication
from UI.ListSTNK      import listStnkUI
from UI.inputDataSTNK import inputDataSTNKUI
from UI.Loguser       import logUserUI
from UI.ListRole      import listRoleUI
from UI.ListAdmin     import listAdminUI
from UI.ListExpired   import listExpiredUI
from UI.membuatAdmin  import membuatAdminUI
from UI.membuatRole   import membuatRoleUI
from UI               import login
from Controller       import cLogin
import sys

class cDashboard(object):

    def generateUI(self, obj=None):
        app = QApplication(sys.argv)
        self.dash = dashboardUI(obj)
        self.dash.setVisible(True)
        sys.exit(app.exec_())
        
    def getListSTNK(self, obj):
        ui = listStnkUI(obj)
        obj.hide()
        ui.show()
        
    def getInputDataSTNK(self, obj):
        ui = inputDataSTNKUI(obj)
        obj.hide()
        ui.show()
   
    def getLogUser(self, obj):
        ui = logUserUI(obj)
        obj.hide()
        ui.show()
        
    def getListRole(self, obj):
        ui = listRoleUI(obj)
        obj.hide()
        ui.show()
        
    def getMembuatRole(self, obj):
        ui = membuatRoleUI(obj)
        obj.hide()
        ui.show()
         
    def getListAdmin(self, obj):
        ui = listAdminUI(obj)
        obj.hide()
        ui.show()
        
    def getMembuatAdmin(self, obj):
        ui = membuatAdminUI(obj)
        obj.hide()
        ui.show()
    
    def getListExpired(self, obj):
        ui = listExpiredUI(obj)
        obj.hide()
        ui.show()
        
    def getKeluar(self, obj):
        ui = login.loginUI()
        obj.hide()
        ui.show()
        ui.exec_()

