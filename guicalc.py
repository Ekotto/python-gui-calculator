from glob import glob
import tkinter as tk
from tkinter import *

#on defini une variable global
calculation = ""

#on defini la fonction qui permet prendre les entrer des boutons de la calculatrice en utilisant la variable global
def add_to_calculate(num):
    global calculation
    calculation = calculation + str(num) # on converti notre parametre "num" en chaine de caractere
    text_field.delete(1.0, "end") # la ligne permetant de nettoyer le champ de text chaque fois qu'on y ajoute une valeur
    text_field.insert(1.0, calculation) # la ligne qui permet d'inserer la valeur appuyer(entrer)

# on definit la fonction qui permet de faire les operation de calcul
def operate():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_field.delete(1.0, "end")
        text_field.insert(1.0, calculation)
    except:
        clear_field()
        text_field.insert(1.0, "Error")

# on definit la fonction qui permet d'effacer tout entrer inserer (meme le resultat) pour un nouveau calclue
def clear_field():
    global calculation
    calculation = ""
    text_field.delete(1.0, "end")

#on debute le codage de la calculatrice en lui donnant un nom,dimension, restraindre l'agrandissement
calc= Tk()
calc.title("Python Calculator")
calc.geometry("300x300")
calc.resizable(0,0)
#calc.configure(background="black")

# les text_field represente le champ de text et ces parametres
text_field = tk.Text(calc, height=2, width=16, font=("Arial", 24))
text_field.grid(columnspan=5)

#on ajoute les bouton et leur commandes
btn_1 = tk.Button(calc, text="1", command=lambda: add_to_calculate("1"), width=5, font="Arial, 14")
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(calc, text="2", command=lambda: add_to_calculate(2), width=5, font="Arial, 14")
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(calc, text="3", command=lambda: add_to_calculate(3), width=5, font="Arial, 14")
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(calc, text="4", command=lambda: add_to_calculate(4), width=5, font="Arial, 14")
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(calc, text="5", command=lambda: add_to_calculate(5), width=5, font="Arial, 14")
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(calc, text="6", command=lambda: add_to_calculate(6), width=5, font="Arial, 14")
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(calc, text="7", command=lambda: add_to_calculate(7), width=5, font="Arial, 14")
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(calc, text="8", command=lambda: add_to_calculate(8), width=5, font="Arial, 14")
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(calc, text="9", command=lambda: add_to_calculate(9), width=5, font="Arial, 14")
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(calc, text="0", command=lambda: add_to_calculate(0), width=5, font="Arial, 14")
btn_0.grid(row=5, column=2)

btn_div = tk.Button(calc, text="/", command=lambda: add_to_calculate("/"), width=5, font="Arial, 14")
btn_div.grid(row=2, column=4)

btn_mult = tk.Button(calc, text="*", command=lambda: add_to_calculate("*"), width=5, font="Arial, 14")
btn_mult.grid(row=3, column=4)

btn_add = tk.Button(calc, text="+", command=lambda: add_to_calculate("+"), width=5, font="Arial, 14")
btn_add.grid(row=4, column=4)

btn_sub = tk.Button(calc, text="-", command=lambda: add_to_calculate("-"), width=5, font="Arial, 14")
btn_sub.grid(row=5, column=4)

btn_openb = tk.Button(calc, text="(", command=lambda: add_to_calculate("("), width=5, font="Arial, 14")
btn_openb.grid(row=5, column=1)

btn_closeb = tk.Button(calc, text=")", command=lambda: add_to_calculate(")"), width=5, font="Arial, 14")
btn_closeb.grid(row=5, column=3)

btn_clear = tk.Button(calc, text="C", command= clear_field, width=11, font="Arial, 14")
btn_clear.grid(row=6, column=1,columnspan=2)

btn_equal = tk.Button(calc, text="=", command= operate, width=11, font="Arial, 14")
btn_equal.grid(row=6, column=3,columnspan=3)

#on demarre le Gui de la calculatrice
calc.mainloop()