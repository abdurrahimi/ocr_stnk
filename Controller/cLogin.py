# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:12:13 2020

@author: X441UV
"""
import sys
from PyQt5          import QtCore, QtGui, QtWidgets
from UI.login       import loginUI
from UI.dashboard   import dashboardUI
from Model.mUser    import mUser
import datetime

class cLogin(object):
    def __init__(self,UIgenerate=False):
        if not UIgenerate:
            self.model= mUser()
            
        if UIgenerate:
            self.generateUI()
    
    def generateUI(self):
        app = QtWidgets.QApplication(sys.argv)
        #app.quit()
        self.ui = loginUI()
        self.ui.show()
        sys.exit(app.exec_())


    def getLogin(self, obj):
        """
        params: obj = object of main view (login view)
        """
        user    = obj.userName.text()
        passwd  = obj.userPassword.text()
        where = """
        WHERE nama_pengguna = '%s' AND kata_sandi = '%s'
        """%(user, passwd)
        data = self.model.getData("setup_admin",where)
        msg = QtWidgets.QMessageBox()
        if len(data)> 0:
            
            """
            ada dua cara untuk memunculkan dan menghilangkan gui
            1. menggunakan setVisible: dengan memasukkan parameter 
                a. False untuk menghilangkan UI
                b. True untuk menampilkan UI
            contoh: 
                dash = dashboardUI(obj)
                obj.setVisible(False)             
                dash.setVisible(True)

            2. menggunakan show() dan hide(): cara simple
                a. show() untuk menampilkan ui
                b. hide() untuk menyembunyikan ui
            contoh:
                ada di codenya!
            
            """
            idadmin = data['id_admin'][0]
            nama = data['nama_pengguna'][0]
            tgl = datetime.date.today().strftime("%Y-%m-%d")
            isinya = ['',str(idadmin),str(nama),tgl]
            self.model.insertLogData('log_user',isinya)
            dash = dashboardUI(obj)
            obj.setVisible(False)
            dash.setVisible(True)
            dash.retrieve(obj)
        else :
            msg.about(obj, "Gagal", "Username atau password tidak sesuai!")
