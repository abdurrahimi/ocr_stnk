from PyQt5.QtWidgets import QApplication
from UI.popupInvalidPicture import popupInvalidPictureUI
import sys

class cPopupInvalidPicture(object):
    def generateUI(self, obj=None):
        app = QApplication(sys.argv)
        self.ui = popupInvalidPictureUI(obj)
        self.ui.setVisible(True)
        sys.exit(app.exec_())