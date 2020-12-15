from PyQt5.QtWidgets import QApplication
from UI.popupReminder  import popupReminderUI
import sys

class cPopupReminder(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)
        self.ui = popupReminderUI(obj)
        self.ui.setVisible(True)
        sys.exit(app.exec_())