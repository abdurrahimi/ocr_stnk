from PyQt5.QtWidgets import QApplication
from UI.popupInvalidLogin  import popupInvalidLoginUI
import sys

class cPopupInvalidLogin(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)
        self.ui = popupInvalidLoginUI(obj)
        self.ui.setVisible(True)
        sys.exit(app.exec_())