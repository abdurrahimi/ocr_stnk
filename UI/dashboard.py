# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:21:56 2020

@author: X441UV
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtGui import QIcon
from Controller import cDashboard
from Model import mUser
import datetime


class dashboardUI(QMainWindow):
    
    def __init__(self, parent=None):
        super(dashboardUI, self).__init__(parent)
        self.resize(900, 900)  
        self.initUI()

    
    def initUI(self):     
        act1 = QAction(QIcon('open.png'), '&List STNK', self)      
        act1.setStatusTip('Open application')
        act1.triggered.connect(self.menuListSTNK)
        
        act2 = QAction(QIcon('open.png'), '&Input data STNK', self) 
        act2.setStatusTip('Open application')
        act2.triggered.connect(self.menuInputDataSTNK)
        
        act3 = QAction(QIcon('open.png'), '&Log User', self)     
        act3.setStatusTip('Open application')
        act3.triggered.connect(self.menuLogUser)
        
        act4 = QAction(QIcon('open.png'), '&List Role', self)      
        act4.setStatusTip('Open application')
        act4.triggered.connect(self.menuListRole)
        
        act5 = QAction(QIcon('open.png'), '&Membuat Role', self)        
        act5.setStatusTip('Open application')
        act5.triggered.connect(self.menuMembuatRole)

        act6 = QAction(QIcon('open.png'), '&List Admin', self)     
        act6.setStatusTip('Open application')
        act6.triggered.connect(self.menuListAdmin)
        
        act7 = QAction(QIcon('open.png'), '&Membuat Admin', self)     
        act7.setStatusTip('Open application')
        act7.triggered.connect(self.menuMembuatAdmin)
        
        act8 = QAction(QIcon('open.png'), '&List Expired', self)     
        act8.setStatusTip('Open application')
        act8.triggered.connect(self.menuListExpired)
        
        act9 = QAction(QIcon('open.png'), '&Keluar', self)     
        act9.setStatusTip('Open application')
        act9.triggered.connect(self.keluarAplikasi)
        
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&STNK')
        fileMenu.addAction(act1)
        fileMenu.addAction(act2)
        fileMenu.addAction(act8)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Pengaturan Role')
        fileMenu.addAction(act4)
        fileMenu.addAction(act5)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Pengaturan Admin')
        fileMenu.addAction(act6)
        fileMenu.addAction(act7)
        fileMenu.addAction(act3)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Keluar')
        fileMenu.addAction(act9)
        
        self.setGeometry(90, 25, 900, 800)
        self.setWindowTitle('Dashboard')    
    
    def menuListSTNK(self):
        dashboardc  = cDashboard.cDashboard()
        dashboardc.getListSTNK(self)
        
    def menuInputDataSTNK(self):
        dashboardc  = cDashboard.cDashboard()
        dashboardc.getInputDataSTNK(self)

    def menuLogUser(self):
        dashboardc  = cDashboard.cDashboard()
        dashboardc.getLogUser(self)
 
    def menuListRole(self):
        dashboardc  = cDashboard.cDashboard()
        dashboardc.getListRole(self)
                
    def menuMembuatRole(self):
        dashboardc  = cDashboard.cDashboard()
        dashboardc.getMembuatRole(self)
                
    def menuListAdmin(self):
        dashboardc  = cDashboard.cDashboard()
        dashboardc.getListAdmin(self)
        
    def menuMembuatAdmin(self):
        dashboardc  = cDashboard.cDashboard()
        dashboardc.getMembuatAdmin(self)
        
    def menuListExpired(self):
        dashboardc  = cDashboard.cDashboard()
        dashboardc.getListExpired(self)
        
    def keluarAplikasi(self):
        dashboardc  = cDashboard.cDashboard()
        dashboardc.getKeluar(self)

    def retrieve(self,obj):
        model= mUser.mUser()
        datenya = datetime.datetime.today() + datetime.timedelta(30)
        data = model.getData("stnk", "where masa_berlaku < '%s'"%datenya)
        msg = QtWidgets.QMessageBox()
        if len(data)> 0:
            hps = QMessageBox.question(self,'Message', "Terdapat STNK yang akan expired. \n Lihat?", QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
            if(hps == QMessageBox.Yes):
                self.menuListExpired()
                