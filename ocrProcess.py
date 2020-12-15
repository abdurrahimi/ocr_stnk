# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pytesseract
import cv2
import numpy as np
import re

#baca img: R,G,B
def getTesseract(path_img):
    img = cv2.imread(path_img)
    #pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ASUS\AppData\Local\Programs\Python\Python37\Lib\site-packages\pytesseract'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract\tesseract.exe'
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,hasilThresholding = cv2.threshold(img_gray,160,255,cv2.THRESH_TOZERO)

    hasil = pytesseract.image_to_string(hasilThresholding, lang="ind")
    #print(hasil)
    nomer_registrasi = re.findall("\:\s+\w{1,2} \d{1,4} \w{1,3}",hasil)
    nama_pemilik = re.findall("NAMA PEMILIK [\w+ ]+",hasil)
    masa_berlaku = re.findall("BERLAKU SAMPAI\w+\W+ \d{1,2}-\d{1,2}",hasil)
    print(nomer_registrasi,nama_pemilik,masa_berlaku)
    
    data_return = {"nomer_registrasi":"",
                   "nama_pemilik":"",
                   "masa_berlaku":""}
    
    if len(nomer_registrasi)>0:
        data_return["nomer_registrasi"]= re.sub("[^\w ]","", nomer_registrasi[0])
    
    if len(nama_pemilik) >0:
        data_return["nama_pemilik"] = re.sub("NAMA PEMILIK","", nama_pemilik[0])
    
    if len(masa_berlaku) > 0:
        data_return["masa_berlaku"] = re.sub("[^\d-]","", masa_berlaku[0])
    
    return data_return

#print(getTesseract("C:/Users/X441UV/Documents/SKRIPSI-Rivita/Gambar/STNKSCAN1.jpg"))