
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import os
import numpy as np


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Desktop\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def get_binary_data():
  binary_data = entry_1.get()
  return binary_data

def open_gui_3():
    gui_3 = r"C:\Users\HP\Desktop\build\gui_3.py"
    os.system("python "+ gui_3)

def open_gui_principale():
    gui_principale = r"C:\Users\HP\Desktop\build\gui_principale.py"
    os.system("python "+ gui_principale)

def delete_all_plots():
        for widget in canvas.winfo_children():
            if isinstance(widget, tk.Widget) and widget != canvas:
                widget.destroy()

def generate_square_signal(binary_data, Ts):
    samples_per_symbol = int(Ts) 
    signal = []
    for bit in binary_data:
        if bit == '0':
            signal.extend([0] * samples_per_symbol)
        elif bit == '1':
            signal.extend([1] * samples_per_symbol) 
        else:
            raise ValueError("Invalid binary data. Please enter only 0s and 1s.")
    return signal



def generate_random_binary_data_and_plot():
    length = random.randint(5, 11)
    binary_data = ''.join(random.choice('01') for _ in range(length))
    Ts=entry_2.get()
    signal = generate_square_signal(binary_data,Ts)
    with open("binary_data.txt", "w") as file:
     file.write(binary_data)
    if not binary_data.isdigit() or any(c not in '01' for c in binary_data):
        print("Invalid binary data. Please enter only 0s and 1s.")
        return 
    update_plot(signal)
    return binary_data

def update_plot(signal):
    figure = Figure(figsize=(8, 3)) 
    ax = figure.add_subplot(111)
    ax.plot(signal)
    ax.set_xlabel("Temps")
    ax.set_ylabel("Valeur")
    ax.set_title("Signal genéré")

    canvas.delete("plot")

    plot_width = window.winfo_width() // 2  # Divide window width by 2 for left half
    desired_plot_height = 250 

    available_height = canvas.winfo_height() - sum(
        widget.winfo_height() for widget in canvas.winfo_children() if widget != canvas)

    plot_height = min(desired_plot_height, available_height)

    plot_x = 10 
    plot_y = (canvas.winfo_height() - plot_height) / 1.65

    plot_canvas = FigureCanvasTkAgg(figure, master=canvas)
    plot_canvas.get_tk_widget().place(
        x=plot_x,
        y=plot_y,
        width=plot_width,
        height=plot_height
    )
    plot_canvas.draw()

    clock_signal = np.sign(np.sin(np.linspace(0, 40, len(signal))))    
    clock_figure = Figure(figsize=(8, 3))
    clock_ax = clock_figure.add_subplot(111)
    clock_ax.plot(clock_signal)
    clock_ax.set_xlabel("Temps")
    clock_ax.set_ylabel("Value")
    clock_ax.set_title("Horloge")

    clock_plot_x = plot_width + 10 
    clock_plot_canvas = FigureCanvasTkAgg(clock_figure, master=canvas)
    clock_plot_canvas.get_tk_widget().place(
        x=clock_plot_x,
        y=plot_y,
        width=plot_width,
        height=plot_height
    )
    clock_plot_canvas.draw()



def button_clicked():
    binary_data = get_binary_data()
    with open("binary_data.txt", "w") as file:
     file.write(binary_data)
    if not binary_data.isdigit() or any(c not in '01' for c in binary_data):
        print("Invalid binary data. Please enter only 0s and 1s.")
        return 
    Ts=entry_2.get()
    signal = generate_square_signal(binary_data,Ts)
    update_plot(signal)

window = Tk()

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
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    222.0,
    231.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=72.0,
    y=206.0,
    width=300.0,
    height=48.0
)

canvas.create_text(
    72.0,
    178.0,
    anchor="nw",
    text="Entrer Le Message Binaire:",
    fill="#000000",
    font=("Poppins Regular", 15 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    435.0,
    231.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=387.0,
    y=206.0,
    width=96.0,
    height=48.0
)

canvas.create_text(
    387.0,
    178.0,
    anchor="nw",
    text="Entrer Ts:",
    fill="#000000",
    font=("Poppins Regular", 15 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button_clicked,
    relief="flat"
)
button_1.place(
    x=498.0,
    y=206.0,
    width=148.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=generate_random_binary_data_and_plot,
    relief="flat"
)
button_2.place(
    x=661.0,
    y=206.0,
    width=148.0,
    height=50.0
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
    x=1137.0,
    y=652.0,
    width=119.0,
    height=50.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=delete_all_plots,
    relief="flat"
)
button_5.place(
    x=588.0,
    y=618.0,
    width=116.0,
    height=27.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui_principale,
    relief="flat"
)
button_6.place(
    x=25.0,
    y=648.0,
    width=119.0,
    height=50.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    625.0,
    87.0,
    image=image_image_1
)

window.resizable(False, False)
window.mainloop()
