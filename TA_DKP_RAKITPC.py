#Ratstsan Nur Akmal Adiwijaya 21120121120019
#MODUL 1 ada
#MODUL 2 ada (if)
#MODUL 3 tidak ada
#MODUL 4 ada (def)
#MODUL 5 ada (inheritance)
#MODUL 6 ada (seter geter)
#MODUL 7 tidak ada
#MODUL 8 ada (GUI)

from ctypes import resize
from tkinter import *
from tkinter.messagebox import *
from tkinter.messagebox import showerror
from abc import ABC

class Processor(ABC):
    model = None
    year = None
    color = None

class Intel(Processor):

    def __init__(self,model):
        self.model = model

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model

class VGA(Processor):

    def __init__(self,model):
        self.model = model

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model

intel = Intel("i5 4590                                    ") #1jt
intel2 = Intel("AMD Ryzen5 3600                           ") #10jt
intel3 = Intel("i7 11700                                  ") #100jt

vga = VGA("NVIDIA NVS 315                                 ") #1jt
vga2 = VGA("GeForce GTX1650                               ") #10jt
vga3 = VGA("GeForce RTX3080                               ") #100jt

def display():
    num = entry.get()
    try:
       num = int(num)
    except ValueError:
        showerror('Error', 'Yang Anda Masukkan Bukan Angka')
    else:
        if num <= 800000:
            showerror('Error', 'Kami belum bisa menemukan PC semurah itu')
        elif 800000 < num <= 1000000:
            hasil = Label(window, text= ((intel.getModel())))
            hasil.place(x=100,y=153)
            hasil = Label(window, text= ((vga.getModel())))
            hasil.place(x=100,y=193)
        elif 1000000 < num <= 10000000:
            hasil = Label(window, text= ((intel2.getModel())))
            hasil.place(x=100,y=153)
            hasil = Label(window, text= ((vga2.getModel())))
            hasil.place(x=100,y=193)
        elif 10000000 < num <= 100000000:
            hasil = Label(window, text= ((intel3.getModel())))
            hasil.place(x=100,y=153)
            hasil = Label(window, text= ((vga3.getModel())))
            hasil.place(x=100,y=193)
        else:
            showerror('Error', 'Kami belum bisa menemukan PC semahal itu')
            
window = Tk()

window.geometry("320x300")
window.title("rakitpc.net")
window.resizable(width = 0, height = 0)

menu = Menu(window)
itemfile = Menu(menu, tearoff=0)
itemhelp = Menu(menu, tearoff=0)
itemhelp.add_command(label = 'Hubungi Ratstsan 21120121120019')
menu.add_cascade(label='Help', menu=itemhelp)
menu.add_cascade(label='Edit')
menu.add_cascade(label='View')
window.config(menu=menu)

labelwelcome = Label(window, 
                    text = "Selamat Datang di rakitpc.net",
                    font = ("times new roman", 12))
labelwelcome.pack(pady=20)   

labelbudget = Label(window, 
                    text = "Budget\t:",
                    font = ("times new roman", 12))
labelbudget.place(x=10,y=65)   

labelintel = Label(window, 
                    text = "Processor\t:",
                    font = ("times new roman", 12))
labelintel.place(x=10,y=150)   

labelvga = Label(window, 
                    text = "VGA\t:",
                    font = ("times new roman", 12))
labelvga.place(x=10,y=190)   

entry = Entry(window)
entry.pack(pady=5)
btn = Button(window, text = "Masukkan Budget", command = display)
btn.pack(pady=5)

window.mainloop()