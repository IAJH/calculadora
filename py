from tkinter import *
from math import *
ventana = Tk()
ventana.title("CALCULADORA")
ventana.configure(background=("gray"))
ventana.geometry("392x600")
ancho_boton = 11
alto_boton = 3
Salida = Entry(ventana, font=("arial", 20, "bold"), width=22, bd=20, insertwidth=4, bg="white", justify="right")
Salida.place(x=10, y=60)
def agregar_caracter(caracter):
    Salida.insert(END,caracter)
def calcular():
        expresion= Salida.get()
        resultado= eval(expresion)
        Salida.delete(0, END)
        Salida.insert(END, resultado)
Boton0 = Button(ventana, text="0", width=ancho_boton, height=alto_boton, command=lambda: agregar_caracter("0"),bg="red")
Boton0.place(x=17, y=180)
Boton1 = Button(ventana, text="1", width=ancho_boton, height=alto_boton, command=lambda: agregar_caracter("1"),bg="yellow")
Boton1.place(x=107, y=180)
Boton2 = Button(ventana, text="2", width=ancho_boton, height=alto_boton, command=lambda: agregar_caracter("2"),bg="blue")
Boton2.place(x=197, y=180)
Boton3 = Button(ventana, text="3", width=ancho_boton, height=alto_boton, command=lambda: agregar_caracter("3"))
Boton3.place(x=285, y=180)
Boton4 = Button(ventana, text="4", width=ancho_boton, height=alto_boton, command=lambda: agregar_caracter("4"))
Boton4.place(x=17, y=240)
Boton5 = Button(ventana, text="5", width=ancho_boton, height=alto_boton,command=lambda: agregar_caracter("5"))
Boton5.place(x=107, y=240)
Boton6 = Button(ventana, text="6", width=ancho_boton, height=alto_boton,command=lambda: agregar_caracter("6"))
Boton6.place(x=197, y=240)
Boton7 = Button(ventana, text="7", width=ancho_boton, height=alto_boton,command=lambda: agregar_caracter("7"))
Boton7.place(x=285, y=240)
Boton8 = Button(ventana, text="8", width=ancho_boton, height=alto_boton,command=lambda: agregar_caracter("8"))
Boton8.place(x=17, y=300)
Boton9 = Button(ventana, text="9", width=ancho_boton, height=alto_boton,command=lambda: agregar_caracter("9"))
Boton9.place(x=107, y=300)
botonP=Button(ventana,text="%",width=ancho_boton,height=alto_boton,command=lambda: agregar_caracter("%"))
botonP.place(x=197,y=300)
BotonComa = Button(ventana, text=",", width=ancho_boton, height=alto_boton,command=lambda: agregar_caracter(","))
BotonComa.place(x=285, y=300)
BotonSma = Button(ventana, text="+", width=ancho_boton, height=alto_boton, command=lambda: agregar_caracter("+"))
BotonSma.place(x=17, y=360)
BotonResta = Button(ventana, text="-", width=ancho_boton, height=alto_boton, command=lambda: agregar_caracter("-"))
BotonResta.place(x=107, y=360)
BotonMulti = Button(ventana, text="*", width=ancho_boton, height=alto_boton, command=lambda: agregar_caracter("*"))
BotonMulti.place(x=197, y=360)
BotonDiv = Button(ventana, text="/", width=ancho_boton, height=alto_boton, command=lambda: agregar_caracter("/"))
BotonDiv.place(x=285, y=360)
BotonSqrt = Button(ventana, text="√", width=ancho_boton, height=alto_boton,command=lambda: agregar_caracter("√"))
BotonSqrt.place(x=17, y=420)
BotonPare1 = Button(ventana, text="(", width=ancho_boton, height=alto_boton,command=lambda: agregar_caracter("("))
BotonPare1.place(x=17, y=480)
BotonaParen2 = Button(ventana, text=")", width=ancho_boton, height=alto_boton,command=lambda: agregar_caracter(")"))
BotonaParen2.place(x=107, y=480)
BotonResto = Button(ventana, text="%", width=ancho_boton, height=alto_boton)
BotonResto.place(x=197, y=480)
BotonIn = Button(ventana, text="In", width=ancho_boton, height=alto_boton)
BotonIn.place(x=187, y=480)
BotonX= Button(ventana,text="X",width=ancho_boton, height=alto_boton,command=lambda:Salida.delete(-1))
BotonX.place(x=196,y=480)
BotonC = Button(ventana, text="C", width=ancho_boton, height=alto_boton,command=lambda:Salida.delete(0, END))
BotonC.place(x=107, y=420)
BotonResul = Button(ventana, text="=", width=ancho_boton, height=alto_boton,command=calcular)
BotonResul.place(x=197, y=420)
ventana.mainloop()
