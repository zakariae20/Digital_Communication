from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import os
import numpy as np
import matplotlib.pyplot as plt

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Desktop\build\assets\frame8")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_gui_7():
    gui_7 = r"C:\Users\HP\Desktop\build\gui_7.py"
    os.system("python "+ gui_7)

def open_gui_9():
    gui_9 = r"C:\Users\HP\Desktop\build\gui_9.py"
    os.system("python "+ gui_9)


def read_data_from_file():
    with open("binary_data.txt", "r") as file:
        binary_data = file.read()
    return binary_data

def generate_square_signal(binary_data):
    samples_per_symbol = 100
    signal = []
    for bit in binary_data:
        if bit == '0':
            signal.extend([0] * samples_per_symbol)
        elif bit == '1':
            signal.extend([1] * samples_per_symbol) 
        else:
            raise ValueError("Invalid binary data. Please enter only 0s and 1s.")
    return signal

def plot_signal(signal, binary_data_file, root):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(signal, drawstyle='steps-pre')
    ax.set_title('Signal')
    ax.set_xlabel('Sample Number')
    ax.set_ylabel('Amplitude')
    ax.grid(True)

    # Draw the plot on the canvas
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()

    # Calculate the center position for the plot
    window_width = 1280
    window_height = 720
    plot_width = 1000  # Approximate width of the plot
    plot_height = 400  # Approximate height of the plot

    center_x = (window_width - plot_width) // 2
    center_y = (window_height - plot_height) // 2.55

    canvas_widget.place(x=center_x, y=center_y)

    # Add the first text below the plot
    text1_y = center_y + plot_height + 30 
    text1_label = tk.Label(root, text="Voila notre sequence binaire recue: ", font=("Arial", 14))
    text1_label.place(x=center_x + plot_width // 2, y=text1_y, anchor=tk.CENTER)

    # Load binary data from file (replace with your file path)
    with open(binary_data_file, 'r') as file:
        binary_data = file.read().strip()

    # Add the second text below the first text
    text2_y = text1_y + 40  
    text2_label = tk.Label(root, text=f"{binary_data}", font=("Arial", 24, "bold"), wraplength=800)
    text2_label.place(x=center_x + plot_width // 2, y=text2_y, anchor=tk.CENTER)


def on_button3_click():
    binary_data = read_data_from_file()
    binary_data_file = r'C:\Users\HP\Desktop\build\binary_data.txt' 
    signal = generate_square_signal(binary_data)
    plot_signal(signal , binary_data_file , window)

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
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui_9,
    relief="flat"
)
button_1.place(
    x=1137.0,
    y=652.0,
    width=119.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui_7,
    relief="flat"
)
button_2.place(
    x=25.0,
    y=646.0,
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
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=on_button3_click,
    relief="flat"
)
button_3.place(
    x=551.0,
    y=663.0,
    width=179.0,
    height=32.0
)
window.resizable(False, False)
window.mainloop()