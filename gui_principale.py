
from pathlib import Path

import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Desktop\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_gui_2():
    gui_2 = r"C:\Users\HP\Desktop\build\gui_2.py"
    os.system("python " + gui_2)

def open_gui_3():
    gui_3 = r"C:\Users\HP\Desktop\build\gui_3.py"
    os.system("python "+ gui_3)


window = tk.Tk()

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    54.0,
    549.0,
    1118.0,
    706.0,
    fill="#D9D9D9",
    outline="#000000")

canvas.create_rectangle(
    54.0,
    170.0,
    1118.0,
    336.0,
    fill="#D9D9D9",
    outline="#000000")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    616.0,
    376.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui_2,
    relief="flat"
)
button_1.place(
    x=91.0,
    y=202.0,
    width=193.0,
    height=95.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=91.0,
    y=578.0,
    width=193.0,
    height=95.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui_3,
    relief="flat"
)
button_3.place(
    x=364.0,
    y=202.0,
    width=193.0,
    height=95.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=364.0,
    y=578.0,
    width=193.0,
    height=95.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=637.0,
    y=202.0,
    width=193.0,
    height=95.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=637.0,
    y=578.0,
    width=193.0,
    height=95.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=910.0,
    y=202.0,
    width=193.0,
    height=95.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=910.0,
    y=578.0,
    width=193.0,
    height=95.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=1125.000022649765,
    y=342.0,
    width=94.99997735023499,
    height=192.99995398521423
)

canvas.create_line(
    824.9999750256538, 623.3392271129414,  
    909.9971313476562, 623.3392271129414,  
    fill="#000000",                        
    arrow=tk.FIRST,                         
    arrowshape=(10, 12, 10),                
    width=3                               
)

canvas.create_line(
    1099.0000311350118, 625.3392272189735,  
    1175.0, 625.3392272189735,               
    arrow=tk.FIRST,
    arrowshape=(9, 12, 10),                
    fill="#000000",                         
    width=3                                
)

canvas.create_line(
    826.0, 247.40715119382366,              
    910.9959058761597, 247.40715119382366,  
    arrow=tk.LAST,
    arrowshape=(9, 12, 10), 
    fill="#000000",                         
    width=3)                       

canvas.create_rectangle(
    1169.0,
    245.0,
    1173.3759015335518,
    621.0043688560636,
    fill="#000000",
    outline="") 

# Rectangle 2
canvas.create_line(
    553.0, 248.5,                         
    637.9959058761597, 248.5,             
    arrow=tk.LAST,
    arrowshape=(9, 12, 10), 
    fill="#000000",                       
    width=3                               
)

canvas.create_line(
    280.5, 248.5,                         
    365.49590587615967, 248.5,            
    arrow=tk.LAST,
    arrowshape=(9, 12, 10), 
    fill="#000000",                       
    width=3                               
)

canvas.create_line(
    551.9999750256538, 624.0,             
    636.9971313476562, 624.0,             
    arrow=tk.FIRST,
    arrowshape=(9, 12, 10), 
    fill="#000000",                       
    width=3                               
)

canvas.create_line(
    279.00000554323196, 625.0,            
    363.9971618652344, 625.0,             
    arrow=tk.FIRST,
    arrowshape=(9, 12, 10), 
    fill="#000000",                       
    width=3                               
)

canvas.create_rectangle(
    1099.0,          
    245.0,
    1175.0,
    249.0,
    fill="#000000",
    outline="#000000")

canvas.create_rectangle(
    1169.0,
    531.0,
    1173.3759015335518,
    625.0043688560636,
    fill="#000000",
    outline="") 


canvas.create_text(
    77.0,
    391.0,
    anchor="nw",
    text="+ Assurez-Vous D'Interagir Avec Chaque Bouton Pour Découvrir Ses Fonctionnalités.",
    fill="#000000",
    font=("NunitoSans Bold", 16 * -1)
)

canvas.create_text(
    77.0,
    422.0,
    anchor="nw",
    text="+ Procédez Étape Par Étape Pour Utiliser Efficacement L'Application.",
    fill="#000000",
    font=("NunitoSans Bold", 16 * -1)
)

canvas.create_text(
    77.0,
    453.0,
    anchor="nw",
    text="+ Assurez-Vous D'Entrer Lefs Informations Nécessaires Avec Précision Pour Éviter Les Erreurs.",
    fill="#000000",
    font=("NunitoSans Bold", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
