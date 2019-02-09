# !/usr/bin/python3



# information om istallation

# - Fotona och filmerna bör ligga på en server och länkar med namnen "serverfoto resp. serverfoto" skapas i egna datorns 
#    hemmamapp, länkarna riktas till servern plats där fotona resp. filmerna ligger

# - I roten till fotolänken skall filen fototext.txt ligga som innehåller information om var fotona togs samt
#   en map för varje årtal (2018, 2017, 2016 osv). Samma gäller filmlänken men här finns ingen textfil.

# - Python programmen feh_skal.py och feh_info.py läggs i egna datorn 





from tkinter import *

import tkinter
import os


# skapa klassen 'Window', ärvd från tkinterklassen 'Frame'
class Window(Frame):

    # definera startinställningarna
    def __init__(self, master=None):
        
        # parametrar som skall skickas genom "Frame class". 
        Frame.__init__(self, master)   

        # en referens till huvudfönster, dvs tk window                 
        self.master = master

        # skapa "init_window som vi senare skall köra men det existerar inte ännu
        self.init_window()



    # skapa 'startfönstret' init_window
    def init_window(self):

        # namnet på huvudfönstret     
        self.master.title("BILDVISNINGSPROGRAM  v1.2    av Uno Sandström 2019-02-09")

        # tillåta programmet att uppta hela ytan av "root window"
        self.pack(fill=BOTH, expand=1)

        # skapa en ram för val av fotoinformation
        vram = LabelFrame(self, width=300, height=800)
        vram.place(x=10, y=10)
        vram.pack_propagate(False) 

        # skapa en ram för val av år
        fram = LabelFrame(self, width=300, height=800)
        fram.place(x=310, y=10)
        fram.pack_propagate(False) 

        # skapa en ram för val av semster
        sram = LabelFrame(self, width=300, height=800)
        sram.place(x=610, y=10)
        sram.pack_propagate(False) 

        # vad jag kallar huvudprogram
        self.startpanel(vram, fram, sram)



    # skapa en panel för valparametrar
    def startpanel(self, vram, fram, sram):

        #dekarationer av valparamterar	 
        val101 = IntVar()
        val102 = IntVar()
 
        val201 = IntVar()
        val202 = IntVar()
        val203 = IntVar()
        val204 = IntVar()
        val205 = IntVar()
        val206 = IntVar()
        val207 = IntVar()
        val208 = IntVar()
        val209 = IntVar()
        val210 = IntVar()
        val211 = IntVar()
        val212 = IntVar()
        val213 = IntVar()
        val214 = IntVar()
        val215 = IntVar()
        val216 = IntVar()
        val217 = IntVar()

        val301 = IntVar()
        val302 = IntVar()
        val303 = IntVar()
        val304 = IntVar()
        val305 = IntVar()
        val306 = IntVar()
        val307 = IntVar()
        val308 = IntVar()

        val401 = IntVar()
        val402 = IntVar()
        val403 = IntVar()
        val404 = IntVar()
        val405 = IntVar()
        val406 = IntVar()
        val407 = IntVar()
        val408 = IntVar()
        val409 = IntVar()
        val410 = IntVar()
        val411 = IntVar()
        val412 = IntVar()
        val413 = IntVar()
        val414 = IntVar()
        val415 = IntVar()
        val416 = IntVar()
        val417 = IntVar()

        C101 = Checkbutton(vram, text = "Bildspel", variable = val101, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C102 = Checkbutton(vram, text = "Demo", variable = val102, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)            
        #fram = årsval
        C201 = Checkbutton(fram, text = "2019", variable = val201, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C202 = Checkbutton(fram, text = "2018", variable = val202, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C203 = Checkbutton(fram, text = "2017", variable = val203, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C204 = Checkbutton(fram, text = "2016", variable = val204, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C205 = Checkbutton(fram, text = "2015", variable = val205, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C206 = Checkbutton(fram, text = "2014", variable = val206, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C207 = Checkbutton(fram, text = "2013", variable = val207, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C208 = Checkbutton(fram, text = "2012", variable = val208, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C209 = Checkbutton(fram, text = "2011", variable = val209, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C210 = Checkbutton(fram, text = "2010", variable = val210, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C211 = Checkbutton(fram, text = "2000", variable = val211, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C212 = Checkbutton(fram, text = "1990", variable = val212, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C213 = Checkbutton(fram, text = "1980", variable = val213, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C214 = Checkbutton(fram, text = "1970", variable = val214, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C215 = Checkbutton(fram, text = "1960", variable = val215, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C216 = Checkbutton(fram, text = "1950", variable = val216, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C217 = Checkbutton(fram, text = "1940", variable = val217, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)

        #vram = fotoinformation
        C301 = Checkbutton(vram, text = "Datum", variable = val301, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C302 = Checkbutton(vram, text = "Ort", variable = val302, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C303 = Checkbutton(vram, text = "Kamera", variable = val303, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C304 = Checkbutton(vram, text = "Filmer", variable = val304, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C305 = Checkbutton(vram, text = "Blixt", variable = val305, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C306 = Checkbutton(vram, text = "ISO", variable = val306, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C307 = Checkbutton(vram, text = "Slutartid", variable = val307, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C308 = Checkbutton(vram, text = "Bländare", variable = val308, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)

        #sram = semesterram
        C401 = Checkbutton(sram, text = "Rom 2003", variable = val401, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C402 = Checkbutton(sram, text = "Taiwan 2005", variable = val402, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C403 = Checkbutton(sram, text = "Taiwan 2006", variable = val403, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C404 = Checkbutton(sram, text = "Mosel 2006", variable = val404, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C405 = Checkbutton(sram, text = "Skottland 2008", variable = val405, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C406 = Checkbutton(sram, text = "Nice 2009", variable = val406, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C407 = Checkbutton(sram, text = "Taiwan 2010", variable = val407, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C408 = Checkbutton(sram, text = "Volterra 2012", variable = val408, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C409 = Checkbutton(sram, text = "Irland 2012", variable = val409, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C410 = Checkbutton(sram, text = "Sicilien 2013", variable = val410, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C411 = Checkbutton(sram, text = "New York 2014", variable = val411, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C412 = Checkbutton(sram, text = "Milano 2015", variable = val412, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C413 = Checkbutton(sram, text = "Spanien 2016", variable = val413, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C414 = Checkbutton(sram, text = "Prag 2016", variable = val414, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C415 = Checkbutton(sram, text = "Portugal 2017", variable = val415, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C416 = Checkbutton(sram, text = "Haag 2018", variable = val416, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)
        C417 = Checkbutton(sram, text = "Bratislava 2018", variable = val417, onvalue = 1, offvalue = 0, height=2, width = 20, anchor=W)

        #presentationsordning i respektive ram
        C101.pack()

        C201.pack()
        C202.pack()
        C203.pack()
        C204.pack()
        C205.pack()
        C206.pack()
        C207.pack()
        C208.pack()
        C209.pack()
        C210.pack()
        C211.pack()
        C212.pack()
        C213.pack()
        C214.pack()
        C215.pack()
        C216.pack()
        C217.pack()

        C301.pack()
        C302.pack()
        C303.pack()
        C305.pack()
        C306.pack()
        C307.pack()
        C308.pack()
        C304.pack()
        C102.pack()

        C417.pack()
        C416.pack()
        C415.pack()
        C414.pack()
        C413.pack()
        C412.pack()
        C411.pack()
        C410.pack()
        C409.pack()
        C408.pack()
        C407.pack()
        C406.pack()
        C405.pack()
        C404.pack()
        C403.pack()
        C402.pack()
        C401.pack()

        # skapa klar-knapp och starta fuktion för FEH scriptet
        skapaKnapp = Button(vram, text="Starta",
                                  anchor=SW, bg="green",
                                  command= lambda:self.skapa_FEH_fil(val101.get(),val102.get(),
                                                                val201.get(),val202.get(),val203.get(),val204.get(),
                                                                val205.get(),val206.get(),val207.get(),val208.get(),
                                                                val209.get(),val210.get(),val211.get(),val212.get(),
                                                                val213.get(),val214.get(),val215.get(),val216.get(),
                                                                val217.get(),
                                                                val301.get(),val302.get(),val303.get(),val304.get(),
                                                                val305.get(),val306.get(),val307.get(),val308.get(),
                                                                val401.get(),val402.get(),val403.get(),val404.get(),
                                                                val405.get(),val406.get(),val407.get(),val408.get(),
                                                                val409.get(),val410.get(),val411.get(),val412.get(),
                                                                val413.get(),val414.get(),val415.get(),val416.get(),
                                                                val417.get()))
        
        skapaKnapp.place(relx=.5, rely=.6, anchor="c")





    # skriv till en info-fil som öppnas i programmet feh_info.py
    def skapaInfofil(self,v301,v302,v303,v304,v305,v306,v307,v308,v102):
        infostr = ""

        if v301 == 1: infostr = "datum\n" 
        else: infostr = "inget\n"

        if v302 == 1: infostr = infostr + "ort\n"
        else: infostr = infostr + "inget\n"

        if v303 == 1: infostr = infostr + "kamera\n"
        else: infostr = infostr + "inget\n"

        if v304 == 1: infostr = infostr + "film\n"
        else: infostr = infostr + "inget\n"

        if v305 == 1: infostr = infostr + "blixt\n"
        else: infostr = infostr + "inget\n"

        if v306 == 1: infostr = infostr + "ISO\n"
        else: infostr = infostr + "inget\n"

        if v307 == 1: infostr = infostr + "slutartid\n"
        else: infostr = infostr + "inget\n"

        if v308 == 1: infostr = infostr + "bländare\n"
        else: infostr = infostr + "inget\n"

        if v102 == 1: infostr = infostr + "demo\n"
        else: infostr = infostr + "inget\n"

        saveFile = open('feh_info.txt','w')
        saveFile.write(infostr)
        saveFile.close()



    # starta FEH med ett anpassat startscrip
    def skapa_FEH_fil(self,v101,v102,
                      v201,v202,v203,v204,v205,v206,v207,v208,v209,v210,v211,v212,v213,v214,v215,v216,v217,
                      v301,v302,v303,v304,v305,v306,v307,v308,
                      v401,v402,v403,v404,v405,v406,v407,v408,v409,v410,v411,v412,v413,v414,v415,v416,v417):
        fehstr = "feh --hide-pointer --borderless --fullscreen --zoom max --draw-tinted --auto-rotate --recursive"

        if ((v101 == 1) and (v102 == 1)):
            fehstr = fehstr + " --slideshow-delay 2 "
        elif ((v101 == 1) and (v102 == 0)):
            fehstr = fehstr + " --slideshow-delay 6 "

        if v201 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2019/*.*" 
        if v202 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2018/*.*"
        if v203 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2017/*.*" 
        if v204 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2016/*.*"
        if v205 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2015/*.*" 
        if v206 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2014/*.*"
        if v207 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2013/*.*" 
        if v208 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2012/*.*"
        if v209 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2011/*.*" 
        if v210 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2010/*.*"
        if v211 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2000/*.*" 
        if v212 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/1990/*.*"
        if v213 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/1980/*.*" 
        if v214 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/1970/*.*"
        if v215 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/1960/*.*" 
        if v216 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/1950/*.*"
        if v217 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/1940/*.*"
        if v401 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2003/'2003-11-04 22.58.49.jpg'"
        if v402 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2005/'2005-02-20 14.52.15.jpg'"
        if v403 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2006/'2006-04-01 19.39.32.jpg'"
        if v404 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2006/'2006-09-13 20.30.38.jpg'"
        if v405 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2008/'2008-05-23 22.21.20.jpg'"
        if v406 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2009/'2009-09-11 12.11.05.jpg'"
        if v407 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2010/'2010-03-31 06.15.02.jpg'"
        if v408 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2012/'2012-04-18 20.50.17.jpg'"
        if v409 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2012/'2012-07-31 14.47.26.jpg'"
        if v410 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2013/'2013-04-25 18.21.20.jpg'"
        if v411 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2014/'2014-04-25 07.44.20.jpg'"
        if v412 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2015/'2015-10-03 17.54.04.jpg'"
        if v413 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2016/'2016-04-22 09.25.57.jpg'"
        if v414 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2016/'2016-10-08 13.49.58.jpg'"
        if v415 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2017/'2017-05-05 17.36.13.jpg'"
        if v416 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2018/'2018-04-19 12.00.00.jpg'" 
        if v417 == 1: fehstr = fehstr + " --start-at /home/uno/serverfoto/2018/'2018-09-18 18.29.56.jpg'" 
 
        if "start-at" not in fehstr: fehstr = fehstr + "  --randomize"
        
        if ((v301 == 1) or (v302 == 1) or (v303 == 1) or (v304 == 1) or (v305 == 1) or (v306 == 1) or (v307 == 1) or (v308 == 1)): 
             fehstr = fehstr + ' --info "python3 feh_info.py %F"'
        fehstr = fehstr + " /home/uno/serverfoto/*/*.*"

        self.skapaInfofil(v301,v302,v303,v304,v305,v306,v307,v308,v102)
     
        os.system(fehstr)
        print (fehstr)

        exit()



# "root window" skapas, det är det enda fönstret men det går att skapa fler fönster inuti detta
root = Tk()

root.geometry("900x800")

#skapa en instans
app = Window(root)

#huvudprogrammet
root.mainloop()  

