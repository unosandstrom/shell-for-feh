#!/usr/bin/python3

from tkinter import *
import tkinter
import os
import sys
import random



#print ("This is the name of the script: ", sys.argv[0])
#print ("Number of arguments:", len(sys.argv))
#print ("Argument List:", str(sys.argv))



# Läs filen feh_info.txt som huvudprogrammet skapade

fo = open("feh_info.txt", "r")

datum = fo.readline()
datum = datum.strip()

ort = fo.readline()
ort = ort.strip()

kamera = fo.readline()
kamera = kamera.strip()

film = fo.readline()
film = film.strip()

blixt = fo.readline()
blixt = blixt.strip()

iso = fo.readline()
iso = iso.strip()

slutartid = fo.readline()
slutartid = slutartid.strip()

blandare = fo.readline()
blandare = blandare.strip()

bias = fo.readline()
bias = bias.strip()

demo = fo.readline()
demo = demo.strip()

fo.close()



#Skriv ut fotots datum (taget ur filnamnet), filnamnet kommer som ett argument från FEH 
filnamn=sys.argv[1]

fotodatum = filnamn.split(' ')[0]
fotodatum = fotodatum.split('/')[5]
fotodatum = fotodatum.split('.')[0]
if datum == "datum": print (fotodatum)


#Skriv ut ort, information hämtas från filen fototext.txt som ligger ihop fotofilerna
if ort == "ort": 
    txtdatum = "1900-01-01"
    uttxt = "-"
    a = open("/home/uno/serverfoto/fototext.txt", "r")
    while (txtdatum <= fotodatum):
        line = a.readline()
        txtdatum, txt = line.split(",")
        if (fotodatum == txtdatum): uttxt = txt
    fo.close()
    print(uttxt)



# Skriv ut kameramodellen, information hämtas från programmet exiftool som måste installeras 
bild = sys.argv[1]
if kamera == "kamera": 
    print('Kamera: ', end='', flush=True)
    exifstr = "exiftool -exif:Model -s3 '" + bild +"'"
    os.system(exifstr)



# Skriv ut ISO-talet,information hämtas från programmet exiftool som måste installeras
bild = sys.argv[1]
if iso == "ISO": 
    print('ISO: ', end='', flush=True)
    exifstr = "exiftool -exif:ISO -s3 '" + bild +"'"
    os.system(exifstr)



#Skriv ut slutartiden, information hämtas från programmet exiftool som måste installeras
bild = sys.argv[1]
if slutartid == "slutartid": 
    print('Slutartid: ', end='', flush=True)
    exifstr = "exiftool -exif:ExposureTime -s3 '" + bild +"'"
    os.system(exifstr)



#Skriv ut bländaren, information hämtas från programmet exiftool som måste installeras
bild = sys.argv[1]
if blandare == "bländare": 
    print('Bländare: ', end='', flush=True)
    exifstr = "exiftool -exif:FNumber -s3 '" + bild +"'"
    os.system(exifstr)



# Skriv ut blixtinformation, information hämtas från programmet exiftool som måste installeras
bild = sys.argv[1]
if blixt == "blixt": 
    print('Blixt: ', end='', flush=True)
    exifstr = "exiftool -exif:Flash -s3 '" + bild +"'"
    os.system(exifstr)



# Skriv ut bias information hämtas från programmet exiftool som måste installeras
bild = sys.argv[1]
if bias == "exposure_bias": 
    print('Exp_bias: ', end='', flush=True)
    exifstr = "exiftool -exif:ExposureCompensation -s3 '" + bild +"'"
    os.system(exifstr)



#Visa en film, programmet vlc måste installeras. vlc skall ställas in så att programmet stoppas när en film är klar

if (demo == 'demo'): 
    slumptal = random.randint(0,11)
else: 
    slumptal = random.randint(0,40)

if ((slumptal == 0) and (film == "film")):

    all_years = [1960, 1980, 1989, 2007, 2010, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    random_year = random.randint(0,11)
    selected_year = all_years[random_year]

    number_of_films = [152, 473, 54, 6, 8, 12, 40, 69, 36, 73, 73, 76]
    random_number = random.randint(1,499)
    filmnumber = (random_number % number_of_films[random_year]) +1
    selected_filmnumber = '{0:04d}'.format(filmnumber)

    filmstr = ("serverfilm/"+ str(selected_year)+ "/" + str(selected_year) + "-" + str(selected_filmnumber) + ".mp4")
    vlcstr = ("vlc -f --playlist-autostart " + filmstr)
    os.system(vlcstr)
    os.system('clear')
    exit()




