from tkinter import *
from tkinter.messagebox import *

def failist_sõnastikusse():
        tund_kirjeldus={}
        f = open("tundid_kirjeldused.txt","r")
        for line in f:
            tund,kirjeldus=line.strip().split(":")
            tund_kirjeldus[tund.strip()]=kirjeldus.strip()
        f.close()
        print(tund_kirjeldus)
        return tund_kirjeldus
        

def kirjeldus_aknasse(t:str):
    if (askyesno("Küsimus", "Kas tahad kirjeldust näha?")):
        alam_aken=Toplevel()
        alam_aken.title(t)
        lbl_kirjeldus=Label(alam_aken,text=tund_kirjeldus[t]).pack()
        c=Canvas(alam_aken,height=800,width=1200)
        file=PhotoImage(file=t)
        c.create_image(10,10,image=file,anchor=NW)
        c.pack()
        alam_aken.mainloop()
    else:
         showinfo("Vastus","Kui ei taha siis ei taha")
    print(tund_kirjeldus[t])
    
tund_kirjeldus=failist_sõnastikusse()


aken = Tk()
aken.title("Tunniplaan TARpv21")
aken.geometry("1920x1080")
p=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede"]
j=0
for i in range(1,10,2):
    paev=Label(aken, text=p[j],relief="solid",font="Calibri 20").grid(row=i, column=0, rowspan=2, sticky=N+S+W+E)
    j+=1

kell=["7:40-8:25","8:30-9:15","9:20-10:05","10:10-10:55","11:00-11:45","11:50-12:35","12:40-13:25","13:30-14:15","14:20-15:05","15:10-15:55","16:00-16:45"]
for i in range(11):
    tund="t"+str(i)
    tund=tund1=Label(aken, text=str(i)+"\n"+kell[i], relief="solid",font="Calibri 15").grid(row=0, column=i+1, sticky=N+S+W+E)


#Понедельник
p1=Button(text="Multimeedia", command=lambda:kirjeldus_aknasse("multimedia.png"),font="Calibri 15",bg="cornflowerblue",relief="groove").grid(row=1,column=3,columnspan=2,sticky=N+S+W+E)
p2=Button(text="Inglise keel",command=lambda:kirjeldus_aknasse("eng.png"), font="Calibri 15",bg="floralwhite",relief="groove").grid(row=1,column=5,columnspan=2,sticky=N+S+W+E)
p3=Button(text="Programmeerimise alused",command=lambda:kirjeldus_aknasse("programmerimine.png"), font="Calibri 15",bg="skyblue",relief="groove").grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
p4=Button(text="Multimeedia",command=lambda:kirjeldus_aknasse("multimedia.png"), font="Calibri 15",bg="cornflowerblue",relief="groove").grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
p5=Button(text="Operatsioonisüsteemide alused",command=lambda:kirjeldus_aknasse("OS.png"), font="Calibri 15",bg="mediumorchid",relief="groove").grid(row=1,column=8,columnspan=2,rowspan=2,sticky=N+S+W+E)
p6=Button(text="Matemaatika tugiõpe",command=lambda:kirjeldus_aknasse("maths.png"), font="Calibri 15",bg="lightpink",relief="groove").grid(row=1,column=10,columnspan=1,rowspan=2,sticky=N+S+W+E)

#Вторник
p7=Button(text="programmerimine inglise keeles",command=lambda:kirjeldus_aknasse("eng.png"), font="Calibri 15",bg="floralwhite",relief="groove").grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
p8=Button(text="Inglise keel",command=lambda:kirjeldus_aknasse("eng.png"), font="Calibri 15",bg="mediumslateblue",relief="groove").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
p9=Button(text="Füüsika",command=lambda:kirjeldus_aknasse("phs.png"), font="Calibri 15",bg="floralwhite",relief="groove").grid(row=3,column=4,columnspan=2,rowspan=2,sticky=N+S+W+E)
p10=Button(text="Eesti keel",command=lambda:kirjeldus_aknasse("Eesti keel Gruup 1"), font="Calibri 15",bg="mediumpurple",relief="groove").grid(row=3,column=7,columnspan=2,sticky=N+S+W+E)
p11=Button(text="programmerimine inglise keeles",command=lambda:kirjeldus_aknasse("eng.png"), font="Calibri 15",bg="floralwhite",relief="groove").grid(row=4,column=7,columnspan=2,sticky=N+S+W+E)
p12=Button(text="Matemaatika",command=lambda:kirjeldus_aknasse("maths.png"), font="Calibri 15",bg="lightpink",relief="groove").grid(row=3,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)
p13=Button(text="Tugiõppe keemia",command=lambda:kirjeldus_aknasse("kemia.png"), font="Calibri 15",bg="lightpink",relief="groove").grid(row=3,column=11,columnspan=2,rowspan=2,sticky=N+S+W+E)

#Среда
p14=Button(text="Programmeerimise alused",command=lambda:kirjeldus_aknasse("programmerimine.png"), font="Calibri 15",bg="skyblue",relief="groove").grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
p15=Button(text="Eesti keel",command=lambda:kirjeldus_aknasse("Eesti keel Gruup 2"), font="Calibri 15",bg="darkgrey",relief="groove").grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
p16=Button(text="Multimeedia",command=lambda:kirjeldus_aknasse("multimedia.png"), font="Calibri 15",bg="cornflowerblue",relief="groove").grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
p17=Button(text="Programmeerimise alused",command=lambda:kirjeldus_aknasse("programmerimine.png"), font="Calibri 15",bg="skyblue",relief="groove").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
p18=Button(text="Kehaline kasvatus",command=lambda:kirjeldus_aknasse("fizra.png"), font="Calibri 15",bg="palevioletred",relief="groove").grid(row=5,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)

#Четверг
p19=Button(text="Eesti keel",command=lambda:kirjeldus_aknasse("Eesti keel Gruup 1"), font="Calibri 15",bg="mediumpurple",relief="groove").grid(row=7,column=1,sticky=N+S+W+E)
p20=Button(text="Ajalugu",command=lambda:kirjeldus_aknasse("history.png"), font="Calibri 15",bg="khaki",relief="groove").grid(row=7,column=2,columnspan=2,rowspan=2,sticky=N+S+W+E)
p21=Button(text="Füüsika arvuti ja taristu osad",command=lambda:kirjeldus_aknasse("phs.png"), font="Calibri 15",bg="floralwhite",relief="groove").grid(row=7,column=4,columnspan=2,rowspan=2,sticky=N+S+W+E)
p22=Button(text="Programmeerimise alused",command=lambda:kirjeldus_aknasse("programmerimine.png"), font="Calibri 15",bg="skyblue",relief="groove").grid(row=7,column=8,columnspan=3,sticky=N+S+W+E)
p23=Button(text="Multimeedia",command=lambda:kirjeldus_aknasse("multimedia.png"), font="Calibri 15",bg="cornflowerblue",relief="groove").grid(row=8,column=8,columnspan=3,sticky=N+S+W+E)


#Пятница
p24=Button(text="Vene keel",command=lambda:kirjeldus_aknasse("rus.png"), font="Calibri 15",bg="greenyellow",relief="groove").grid(row=9,column=5,columnspan=2,rowspan=2,sticky=N+S+W+E)
p25=Button(text="Kunstiained",command=lambda:kirjeldus_aknasse("kunst.png"), font="Calibri 15",bg="orchid",relief="groove").grid(row=9,column=7,columnspan=2,rowspan=2,sticky=N+S+W+E)
p26=Button(text="Matemaatika",command=lambda:kirjeldus_aknasse("maths.png"), font="Calibri 15",bg="lightpink",relief="groove").grid(row=9,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)


























aken.mainloop()