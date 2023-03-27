from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

#******************Ventana Principal**********************
mainwindow = tk.Tk()
mainwindow.title('Menu principal: Codigo Hamming')
canvas_principal = tk.Canvas(mainwindow, width=850, height=500)
file=PhotoImage(file="resources//main.png",master=mainwindow)
canvas_principal.create_image(0,0,anchor=NW,image=file)
canvas_principal.pack()

#******************Creacion de ventanas(Inicio)************************
def openNewWindow_Hamming_Code():
    newWindow = tk.Toplevel(mainwindow)
    newWindow.title('Codigo Hamming')
    canvas_principal1 = tk.Canvas(newWindow, width=850, height=500)
    bg1=PhotoImage(file="resources//Hamming Code.png",master=newWindow)
    label2 = Label( canvas_principal1, image = bg1)
    label2.image = bg1
    label2.place(x = 0, y = 0)
    canvas_principal1.pack()

def openNewWindow_Conversion():
    newWindow2 = tk.Toplevel(mainwindow)
    newWindow2.title('Conversion')
    canvas_principal2 = tk.Canvas(newWindow2, width=850, height=500)
    #Cargar y colocar el fondo
    bg2 = PhotoImage(file = "resources//Conversion.png", master=newWindow2)
    label2 = Label( canvas_principal2, image = bg2)
    label2.image = bg2
    label2.place(x = 0, y = 0)
    #Solcitar al usuario el número en hexadecimal
    lbl_hex1 = tk.Label (canvas_principal2,text="Introduce un número hexadecimal de 3 dígitos: ", font=("Adobe Gothic Std B",12),background="#27363B",foreground="white" ).place(x=30,y=150)
    ent_hex1= tk.Entry(canvas_principal2,font=("Adobe Gothic Std B",12),width=25)
    ent_hex1.place(x=355,y=151)
    def get_value():
        hex=ent_hex1.get()
        print(hex)
    convert_btn= tk.Button(canvas_principal2, text="Convertir",command= get_value).place(x=590,y=150)
    #Tabla
    #******************Creación de tabla para mostrar datos***********************
    ent_hex = tk.Entry(canvas_principal2, width=12, justify="center")
    ent_hex.insert(0, "Hexadecimal")
    ent_octal = tk.Entry(canvas_principal2, width=12, justify="center")
    ent_octal.insert(0, "Octal")
    ent_decimal = tk.Entry(canvas_principal2, width=12, justify="center")
    ent_decimal.insert(0, "Decimal")
    ent_binario = tk.Entry(canvas_principal2, width=12, justify="center")
    ent_binario.insert(0, "Binario")
    hex_value = tk.Entry(canvas_principal2, width=12, justify="center")
    oct_value = tk.Entry(canvas_principal2, width=12, justify="center")
    dec_value = tk.Entry(canvas_principal2, width=12, justify="center")
    bin_value = tk.Entry(canvas_principal2, width=12, justify="center")
    ent__list = [ent_hex, ent_octal, ent_decimal, ent_binario, hex_value, oct_value, dec_value, bin_value]

    # Ubicamos los ent_ utilizando place
    ent_hex.place(x=30, y=200)
    ent_octal.place(x=110, y=200)
    ent_decimal.place(x=190, y=200)
    ent_binario.place(x=270, y=200)
    hex_value.place(x=30, y=225)
    oct_value.place(x=110, y=225)
    dec_value.place(x=190, y=225)
    bin_value.place(x=270, y=225)

    # Bloqueamos los ent_
    for ent_ in ent__list:
        ent_.config(state="disabled")        
    canvas_principal2.pack()
#******************Creacion de ventanas(FIN)************************

btn_create_window_Hamming = tk.Button(mainwindow,
             text ="Conversiones/NZRI",
             command = openNewWindow_Conversion)
btn_create_window_Hamming.place(x=480, y=400)

btn2_create_window_Conversion = tk.Button(mainwindow,
             text ="Codigo Hamming",
             command = openNewWindow_Hamming_Code)
btn2_create_window_Conversion.place(x=620, y=400)

mainwindow.mainloop()