# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg 
import random


NOMBRES_MONSTRUOS = ["Mistich", "Mutt", "Guttalon", "Cinder", "Hagger", "Dusty"]

NOMBRES_HEROE = ["Blaster", "Tracer", "Tim"]

ARMAS = ["una espada", "un hacha", "una varita mágica"]


class SerViviente:
    """Clase para definir tanto héroes como mónstruos en nuestro juego"""
    def __init__(self, tipo, nombre, fuerza, arma):
        self.tipo = tipo
        self.nombre = nombre
        self.fuerza = fuerza
        self.arma = arma
        self.describir_ser_viviente()

    def estado_ser_viviente(self):
        print("El {} ahora tiene un nivel de fuerza de {}".format(self.tipo, self.fuerza))
        if self.fuerza == 0:
            print("El {} ha muerto!!!!".format(self.tipo))


    def describir_ser_viviente(self):
        print("Este es un {} llamado {}.  Tiene fuerza nivel {} y posee {}.".format(self.tipo, self.nombre, self.fuerza, self.arma))

class Monster(SerViviente):
    """Sub clase para redefinir al monstruo"""
    
    def atacar(self):
        print("El mónstruo te ataca")
        heroe1.fuerza = heroe1.fuerza -1
        heroe1.estado_ser_viviente()

    def defender(self):
        print("El mónstruo se defiende de tu ataque")
        chance = random.randint(1,3)
        if chance is 2:
            self.atacar()

        def huir(self):
            print("El mónstruo huye ante tu presencia!")


class Hero(SerViviente):
    """Sub clase para redefinir al heroe"""
    def atacar(self):
        print("Has decidido atacar al mónstruo!")
        monster1.fuerza = monster1.fuerza -1
        label_monster_fuerza.config(text = f"Fuerza             {monster1.fuerza}")
        monster1.estado_ser_viviente()

    def defender(self):
        print("Te defiendes del ataque del monstruo")

    def huir(self):
        print("Decides huir... COBARDE!!!")

    
monster1 = Monster("mónstruo", random.choice(NOMBRES_MONSTRUOS), random.randint(1, 10), random.choice(ARMAS))

heroe1 = Hero("héroe", random.choice(NOMBRES_HEROE), random.randint(1, 10), random.choice(ARMAS))



#####################################
######   Diseño de GUI inicia acá
#####################################


window = tk.Tk()
window.title("Monsters vs Heroes")
window.geometry("500x400")
window.resizable(False, False)

#Label-Frame for the monster specs:
label_frame1 = ttk.LabelFrame(window, text = "Your monster specs:")
label_frame1.grid(column = 0, row = 1, padx = 20, pady = 5)

label_monster_name = ttk.Label(label_frame1, text = f"Nombre:      {monster1.nombre}")
label_monster_name.grid(column = 0, row = 0, pady = 20)

label_monster_fuerza = ttk.Label(label_frame1, text = f"Fuerza             {monster1.fuerza}")
label_monster_fuerza.grid(column = 0, row = 1, pady = 20)

label_monster_arma = ttk.Label(label_frame1, text = f"Arma:       {monster1.arma.capitalize()}")
label_monster_arma.grid(column = 0, row = 2, pady = 20)

#Label-Frame for the heroe specs:
label_frame2 = ttk.LabelFrame(window, text = "Your heroe specs:")
label_frame2.grid(column = 1, row = 1, padx = 20, pady = 5)

label_heroe_name = ttk.Label(label_frame2, text = f"Nombre:    {heroe1.nombre}")
label_heroe_name.grid(column = 0, row = 0, pady = 20)

label_heroe_fuerza = ttk.Label(label_frame2, text = f"Fuerza:           {heroe1.fuerza}")
label_heroe_fuerza.grid(column = 0, row = 1, pady = 20)

label_heroe_arma = ttk.Label(label_frame2, text = f"Arma:       {heroe1.arma}")
label_heroe_arma.grid(column = 0, row = 2, pady = 20)

# Action buttons:
attack_button = ttk.Button(window, text = "Atacar!!", command = heroe1.atacar)
attack_button.grid(column = 0, row = 10)

defender_button = ttk.Button(window, text = "Defenderse!!")
defender_button.grid(column = 1, row = 10)

huir_button = ttk.Button(window, text = "Huir, cobarde!!")
huir_button.grid(column = 2, row = 10)


window.mainloop()