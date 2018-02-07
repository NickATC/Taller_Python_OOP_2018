# -*- coding: utf-8 -*-

# Ejercicio 2

# Implementar el código del ejercicio 1.0 a una GUI

# Requisitos:
# 1.  No habrá login.  Simplemente cree las opciones de un ATM
# 2.  Un ATM da muchos mensajes al usuario.  Agregue los mensajes a donde pertenen.
# 3.  Vamos a mantenerlo muy sencillo.  Los retiros y consignaciones serán de 10$
# 4.  A las líneas 42 y 47 les falta la matemática para hallar el nuevo saldo.
# 5.  Las 4 opciones están ya diseñadas con botones.  Solo asigne el código a ejecutar (líneas 80, 83, 86, 89)

# Quiere reto?
# Reto 1.  Modifique su código para que no pueda retirar más de su balance.  Use el mensaje FALLO. 
# Reto 2.  Modifique su código para que tan pronto ejecutemos el ATM, veamos un mensaje de bienvenida. 
#          Use el mensaje MEN_BIENVENIDA.  Use el método en líneas 33 y 34 para lograrlo.

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


class ATM:
    def __init__(self, balance):
        self.__balance = balance    # Observe que es una variable PRIVADA __
        self.saldo = "Su saldo actual es: "
        self.exito = "Transación Exitosa !"
        self.fallo = "Fondos insuficientes !"   # Quiere un reto? y si retira más de su saldo... 
        self.men_bienvenida = "Bienvenido a su cajero automático !"
        self.terminar_sesion = "Cerrando su sesión. \n      Espere un momento... "

    def mensaje_bienvenida(self):
        atm_screen.insert(tk.INSERT, ## inserte mensaje de bienvenida acá ##)

    def ver_balance(self):
        atm_screen.delete(1.0,"end")
        atm_screen.insert(tk.INSERT, ## inserte mensaje de saldo acá ##)
        atm_screen.insert(tk.INSERT, ## inserte balance acá ##)
        
    def retirar(self):
        self.__balance = # A qué es igual el nuevo balance? Falta la matemática en esta línea
        atm_screen.delete(1.0,"end")
        atm_screen.insert(tk.INSERT, ## inserte mensaje de transacción exitosa acá ##)
        
    def consignar(self):
        self.__balance = # A qué es igual el nuevo balance? Falta la matemática en esta línea  
        atm_screen.delete(1.0,"end")
        atm_screen.insert(tk.INSERT, ## inserte mensaje de transacción exitosa acá ##)

    def terminar(self):
        atm_screen.delete(1.0,"end")
        atm_screen.insert(tk.INSERT, ## inserte mensaje de terminar transacción acá ##)



account1 = ATM(100)


##########################
#####  GUI starts here
##########################

window = tk.Tk()
window.title("Simple ATM")
window.geometry("550x200")
window.resizable(False, False)

#Label-Frame for the ATM:
label_frame1 = ttk.LabelFrame(window, text = "Bienvenido a su ATM")
label_frame1.grid(column = 0, row = 1, padx = 15, pady = 30)

# ATM Screen
scrol_w = 30
scrol_h = 3
atm_screen = scrolledtext.ScrolledText(label_frame1, width = scrol_w, height = scrol_h, wrap = tk.WORD)
atm_screen.grid(column = 2, row = 2, padx = 20, pady = 10)

# Action buttons:
saldo_button = ttk.Button(label_frame1, text = "Ver saldo", command = ## inserte código para ver saldo acá ##)
saldo_button.grid(column = 0, row = 2)

retirar_button = ttk.Button(label_frame1, text = "Retirar 10$", command = ## inserte código para retirar acá ##) 
retirar_button.grid(column = 0, row = 3)

depositar_button = ttk.Button(label_frame1, text = "Hacer depósito de 10$", command = ## inserte código para consignar acá ##)
depositar_button.grid(column = 3, row = 2)

terminar_button = ttk.Button(label_frame1, text = "Terminar transacción", command = ## inserte código para terminar la transacción acá ##)
terminar_button.grid(column = 3, row = 3)

window.mainloop()
