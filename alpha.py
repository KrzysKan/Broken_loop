import sys, json, io
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QMessageBox, QApplication
from PyQt5.QtCore import QSize, QUrl
from PyQt5 import QtGui
import math
import folium
from folium.plugins import Draw
import os
import pandas as pd
import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt

points=[]
points.append([52.2716, 21.0121, 1])
points.append([50.5015, 22.1707, 2])

img = tiff.imread('baza.tiff')
img_array = np.array(img) 


"""
Alpha uwzględnia użycie jednej narzuconej mapy!!!


lon|||szerokość
lat---długość
(lat,lon)
"""

class MainWindow(QMainWindow):
    def __init__(self):

        self.points = []
        self.result = []
        
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 380))    
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com") 

        self.nameLabel1 = QLabel(self)
        self.nameLabel1.setText('Lat:')
        self.line1 = QLineEdit(self)

        self.line1.move(80, 20)
        self.line1.resize(200, 32)
        self.nameLabel1.move(20, 20)

        #------
        
        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('lon:')
        self.line2 = QLineEdit(self)

        self.line2.move(80, 60)
        self.line2.resize(200, 32)
        self.nameLabel2.move(20, 60)
        
        #------
        
        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Wys w m:')
        self.line3 = QLineEdit(self)

        self.line3.move(80, 100)
        self.line3.resize(200, 32)
        self.nameLabel3.move(20, 100)

        #------

        button1 = QPushButton('Dodaj wieże', self)
        button1.clicked.connect(self.clickMethod1)
        button1.resize(200,32)
        button1.move(80, 140)
        
        #------

        button2 = QPushButton('Sprawdź dane', self)
        button2.clicked.connect(self.clickMethod2)
        button2.resize(200,32)
        button2.move(80, 180)

        #------

        button2 = QPushButton('Wyczyść dane', self)
        button2.clicked.connect(self.clickMethod3)
        button2.resize(200,32)
        button2.move(80, 220)

        #------

        button2 = QPushButton('Odległość między wieżami', self)
        button2.clicked.connect(self.clickMethod4)
        button2.resize(200,32)
        button2.move(80, 260)

        #------

        button2 = QPushButton('Szybkie sprawdzenie', self)
        button2.clicked.connect(self.clickMethod5)
        button2.resize(200,32)
        button2.move(80, 300)

        #------

        button2 = QPushButton('Sprawdzneie z wizualizacją', self)
        button2.clicked.connect(self.clickMethod6)
        button2.resize(200,32)
        button2.move(80, 340)


    def clickMethod1(self):
        #dodawaie danych
        if len(points)<2:
            global h
            global lat
            global lon
            try:
                print(float(self.line1.text()))
                print(float(self.line2.text()))
                print(float(self.line3.text()))
                h = float(self.line3.text())
                lat = float(self.line1.text())
                lon = float(self.line2.text())
                points.append([lat, lon, h])
                print("Dodano dane")
            except:
                print("Nie da się przekonwertować na float")
                """
                msg = QMessageBox(self)
                msg.setWindowTitle("Alert zapisu")
                msg.setText("Podane dane nie są liczbami!")
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()
                """
        else:
            print("Nie można dodać danych za dużo punktów")
        
    def clickMethod2(self):
        #Wyświetlanie dancyh
        for i in points:
            print(i)
        print("Wyświetlono dane")

        
    def clickMethod3(self):
        #Usuwanie dancyh
        points.clear()
        print("wyczyszczono dane")

        
    def clickMethod4(self):
        #Odległość między punktami
        #nie do końca dokładne
        x1 = float(points[0][0])
        y1 = float(points[0][1])
        x2 = float(points[1][0])
        y2 = float(points[1][1])
        krzywizna = (40075.704 / 360);
        odleglosc = math.sqrt(pow(x2 - x1, 2)+ pow((math.cos(x1*math.pi/180)*(y2-y1)),2))*krzywizna;
        print(odleglosc)
        print("Obliczono odległość")

        
    def clickMethod5(self):
        print("btn5")
        MainWindow.get_height(self)
        MainWindow.get_height(self)
        MainWindow.bres(self, points[0][1], points[0][0], points[1][1], points[1][0])
        print(result)

        
    def clickMethod6(self):
        print("btn6")



    def bres(self,x1,y1,x2,y2):
    
        temp = self.result.pop()
        x = [1,2,34,5]
        x,y = x1,y1
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        gradient = float(dy)/float(dx)

        if gradient > 1:
            dx, dy = dy, dx
            x, y = y, x
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        p = 2*dy - dx
        print(f"x = {x}, y = {y}")
        print(dx, p, y, y2, dy, x, x2)
        for k in range(2, dx + 2):
            print(k)
            if p > 0:
                y = y + 1 if y < y2 else y - 1
                p = p + 2 * (dy - dx)
            else:
                p = p + 2 * dy
            x = x + 1 if x < x2 else x - 1

            print("test2")
            self.result.append(img_array[y][math.ceil(x/2)])  
        #MainWindow.petla(self, dx, p, y, y2, dy, x, x2)
        print("test3")
        self.result.append(temp)
        #plt.plot(xcoordinates, ycoordinates)
        #plt.show()
"""
    def petla(self, dx, p, y, y2, dy, x, x2):
        print("petalaa")
        for k in range(2, dx + 2):
            print(k)
            if p > 0:
                y = y + 1 if y < y2 else y - 1
                p = p + 2 * (dy - dx)
            else:
                p = p + 2 * dy
            x = x + 1 if x < x2 else x - 1

            print("test2")
            self.result.append(img_array[y][math.ceil(x/2)])     
 """   


#Tymczasowa funkcja docelowo zastąpiona gui
    def get_coordinates(self):
        lat = input("Podaj szerokość geograficzną (w formacie ddd mm ss): ")
        lon = input("Podaj długość geograficzną (w formacie ddd mm ss): ")
        return lat, lon

#Funkcja zwracająca resztę sekund 
    def convert_to_seconds(self, coordinate):
        degrees, minutes, seconds = coordinate.split(" ")
        total_seconds = int(minutes) * 60 + int(seconds)
        return total_seconds
    
    def get_height(self):
        lat, lon = MainWindow.get_coordinates(self)
    
        lat_seconds = MainWindow.convert_to_seconds(self, lat)#y
        lon_seconds = MainWindow.convert_to_seconds(self, lon)#x

        print("Szerokość geograficzna w sekundach: ", lat_seconds)
        print("Długość geograficzna w sekundach: ", lon_seconds)

        array_x = [i for i in range(len(img_array[0])*2)]
        array_y = [i for i in range(len(img_array))]

        result_x = math.ceil((array_x.index(lon_seconds)/2))
        result_y = math.ceil(array_y.index(lat_seconds))
    
        self.result.append(img_array[result_y][result_x])
        self.points.append([lat_seconds, lon_seconds])
    
        print("get_height:")
        print(self.result)
        print(self.points)
    def zebranie(self):
        get_height()
        get_height()
        bres(self, self.points[0][1], self.points[0][0], self.points[1][1], self.points[1][0])
        print(self.result)
        
     

    

        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
