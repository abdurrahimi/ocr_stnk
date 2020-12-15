# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:35:10 2020

@author: X441UV
"""

import mysql.connector
import json
import pandas as pd

class mUser():    
    def __init__(self,config = ""):
        try:
            self.connect = mysql.connector.connect(
                host="localhost",
                user="root",
                password = "",
                database="mayasari_bakti"
                )
        except:
            print("error database cannot connect")
            self.connect = None
    
    def getData(self, tabel, condition):
        query = """
            SELECT *
            FROM {tables}
            {conditions}
        """.format(tables=tabel,conditions=condition)
        
        value = pd.read_sql(query, self.connect)
        #print(value)
        return value
    
    def insertData(self, data, table):
        mycursor = self.connect.cursor()
        sql = """
            INSERT INTO {tables} VALUES {val}
        """
        vals = "%s,"* len(data)
        vals = "(" + vals[:-1] + ")" 
        #print(sql)
        hasil = mycursor.execute(sql, vals)
        return hasil

    def insertLogData(self, table, data):
        mycursor = self.connect.cursor()
        sql = "INSERT INTO log_user VALUES (%s,%s,%s,%s)"
        val = (data)
        print(sql)
        mycursor.execute(sql, val)
        try :
            self.connect.commit()
            hasil = True
        except mysql.connector.Error as error :
    
            hasil = False
        return hasil
    
    def insertRoleData(self, table, data):
        mycursor = self.connect.cursor()
        sql = "INSERT INTO setup_role VALUES (%s,%s)"
        val = ("",data)
        print(sql)
        mycursor.execute(sql, val)
        try :
            self.connect.commit()
            hasil = True
        except mysql.connector.Error as error :
            hasil = False
        return hasil

    def insertAdminData(self, table, data):
        mycursor = self.connect.cursor()
        sql = "INSERT INTO setup_admin VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (data)
        print(sql)
        mycursor.execute(sql, val)
        try :
            self.connect.commit()
            hasil = True
        except mysql.connector.Error as error :
            hasil = False
        return hasil

    def updateAdminData(self, table, data):
        mycursor = self.connect.cursor()
        sql = "UPDATE setup_admin set  id_admin = %s,id_role = %s, nama_pengguna = %s, kata_sandi = %s, nama_lengkap = %s, dibuat_oleh = %s, dibuat_tanggal = %s where id_admin = %s"
        val = (data)
        print(sql)
        mycursor.execute(sql, val)
        try :
            self.connect.commit()
            hasil = True
        except mysql.connector.Error as error :
            hasil = False
        return hasil

    def updateRoleData(self, table, data):
        mycursor = self.connect.cursor()
        sql = "UPDATE setup_role set  id_role = %s,nama_role = %s where id_role = %s"
        val = (data)
        print(sql)
        mycursor.execute(sql, val)
        try :
            self.connect.commit()
            hasil = True
        except mysql.connector.Error as error :
            hasil = False
        return hasil


    def insertStnkData(self, data):
        mycursor = self.connect.cursor()
        sql = "INSERT INTO stnk VALUES (%s,%s,%s,%s)"
        val = (data)
        #print(sql)
        mycursor.execute(sql, val)
        try :
            self.connect.commit()
            hasil = True
        except mysql.connector.Error as error :
            hasil = False
        return hasil

    def updateStnkData(self, table, data):
        mycursor = self.connect.cursor()
        sql = "UPDATE stnk set nomor_registrasi = %s, nama_pemilik =%s, masa_berlaku = %s where id_stnk = %s"
        val = (data)
        print(sql)
        mycursor.execute(sql, val)
        try :
            self.connect.commit()
            hasil = True
        except mysql.connector.Error as error :
            hasil = False
        return hasil


    def deleteData(self, tabel, condition):
        mycursor = self.connect.cursor()
        sql = """
            DELETE 
            FROM {tables}
            {conditions}
        """.format(tables=tabel,conditions=condition)
        print(sql)
        mycursor.execute(sql)
        try :
            self.connect.commit()
            hasil = True
        except mysql.connector.Error as error :
            hasil = False
        return hasil
        
