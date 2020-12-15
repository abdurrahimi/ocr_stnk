from PyQt5.QtWidgets import QApplication
#from UI.ListExpired  import listExpiredUI
from UI import dashboard
import sys

class cListExpired(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)
        self.ui = listExpiredUI(obj)
        self.ui.setVisible(True)
        sys.exit(app.exec_())

    def gotodash(self,obj):
        dash = dashboard.dashboardUI(obj)
        obj.hide()
        dash.show()