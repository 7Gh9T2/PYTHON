from tkinter import *
import subprocess

def abrir_calculadora():
    subprocess.Popen('calc.exe')

ventana = Tk()
ventana.title("Primera ventana")
ventana.geometry("520x480")
ventana.config(bg="skyblue")
ventana.resizable(0, 0)

# Botón para abrir la calculadora
boton = Button(ventana, text="Abrir calculadora", command=abrir_calculadora)
boton.place(x=50, y=50)

ventana.mainloop()
