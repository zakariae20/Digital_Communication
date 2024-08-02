from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import os
import numpy as np

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Desktop\build\assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_gui_4():
    gui_4 = r"C:\Users\HP\Desktop\build\gui_4.py"
    os.system("python "+ gui_4)

def open_gui_2():
    gui_2 = r"C:\Users\HP\Desktop\build\gui_4.py"
    os.system("python "+ gui_2)

def read_data_from_file():
    with open("binary_data.txt", "r") as file:
        binary_data = file.read()
    return binary_data

def delete_all_plots():
        for widget in canvas.winfo_children():
            if isinstance(widget, tk.Widget) and widget != canvas:
                widget.destroy()

def generate_square_signal(binary_data):
    signal = []
    for bit in binary_data:
        if bit == '0':
            signal.extend([0] * 100)
        elif bit == '1':
            signal.extend([1] * 100) 
        else:
            raise ValueError("Invalid binary data. Please enter only 0s and 1s.")
    return signal

def generate_nrz_signal(binary_data):
    signal = []
    for bit in binary_data:
        if bit == '0':
            signal.extend([-1] * 100)
        elif bit == '1':
            signal.extend([1] * 100) 
        else:
            raise ValueError("Invalid binary data. Please enter only 0s and 1s.")
    return signal

def generate_rz_signal(binary_data):
    signal = []
    for bit in binary_data:
        if bit == '0':
            signal.extend([0] * 50 + [0] * 50)
        elif bit == '1':
            signal.extend([1] * 50 + [0] * 50) 
        else:
            raise ValueError("Invalid binary data. Please enter only 0s and 1s.")
    return signal

def update_plot_for_nrz(signal1, signal2):
    figure = Figure(figsize=(8, 6)) 
    ax1 = figure.add_subplot(211)
    ax1.plot(signal1)
    ax1.set_ylabel("Signal Value")
    ax1.set_title("Input")
    ax1.grid(True)
    ax2 = figure.add_subplot(212)
    ax2.plot(signal2)
    ax2.set_ylabel("Signal Value")
    ax2.set_xlabel("NRZ Signal")
    ax2.grid(True)
    canvas.delete("plot")
    plot_width = window.winfo_width()
    desired_plot_height = 400 
    available_height = canvas.winfo_height() - sum(
        widget.winfo_height() for widget in canvas.winfo_children() if widget != canvas)
    plot_height = min(desired_plot_height, available_height)
    plot_x = (plot_width - plot_width) / 2  # Center horizontally
    plot_y = (canvas.winfo_height() - plot_height) / 1.65  # Center vertically
    plot_canvas = FigureCanvasTkAgg(figure, master=canvas)
    plot_canvas.get_tk_widget().place(
        x=plot_x,
        y=plot_y,
        width=plot_width,
        height=plot_height
    )
    plot_canvas.draw()

def button_clicked_for_nrz():
    binary_data = read_data_from_file()
    square_signal = generate_square_signal(binary_data)
    nrz_signal = generate_nrz_signal(binary_data)
    update_plot_for_nrz(square_signal, nrz_signal)

def update_plot_for_rz(signal1, signal2):
    figure = Figure(figsize=(8, 6)) 
    ax1 = figure.add_subplot(211)
    ax1.plot(signal1)
    ax1.set_ylabel("Signal Value")
    ax1.set_title("Input")
    ax2 = figure.add_subplot(212)
    ax2.plot(signal2)
    ax2.set_ylabel("Signal Value")
    ax2.set_xlabel("RZ Signal")
    canvas.delete("plot")
    plot_width = window.winfo_width() 
    desired_plot_height = 400 
    available_height = canvas.winfo_height() - sum(
        widget.winfo_height() for widget in canvas.winfo_children() if widget != canvas)
    plot_height = min(desired_plot_height, available_height)
    plot_x = (plot_width - plot_width) / 2  # Center horizontally
    plot_y = (canvas.winfo_height() - plot_height) / 1.65  # Center vertically
    plot_canvas = FigureCanvasTkAgg(figure, master=canvas)
    plot_canvas.get_tk_widget().place(
        x=plot_x,
        y=plot_y,
        width=plot_width,
        height=plot_height
    )
    plot_canvas.draw()

def button_clicked_for_rz():
    binary_data = read_data_from_file()
    square_signal = generate_square_signal(binary_data)
    rz_signal = generate_rz_signal(binary_data)
    update_plot_for_rz(square_signal, rz_signal)

def generate_manchester_signal(binary_data):
    signal = []
    for bit in binary_data:
        if bit == '0':
            signal.extend([-1] * 50 + [1] * 50) 
        elif bit == '1':
            signal.extend([1] * 50 + [-1] * 50)
        else:
            raise ValueError("Invalid binary data. Please enter only 0s and 1s.")
    return signal

def update_plot_for_manchester(signal1, signal2):
    figure = Figure(figsize=(8, 6)) 
    ax1 = figure.add_subplot(211)
    ax1.plot(signal1)
    ax1.set_ylabel("Signal Value")
    ax1.set_title("Input")
    ax2 = figure.add_subplot(212)
    ax2.plot(signal2)
    ax2.set_ylabel("Signal Value")
    ax2.set_xlabel("Manchester Signal")
    canvas.delete("plot")
    plot_width = window.winfo_width() 
    desired_plot_height = 400 
    available_height = canvas.winfo_height() - sum(
        widget.winfo_height() for widget in canvas.winfo_children() if widget != canvas)
    plot_height = min(desired_plot_height, available_height)
    plot_x = (plot_width - plot_width) / 2  # Center horizontally
    plot_y = (canvas.winfo_height() - plot_height) / 1.65  # Center vertically
    plot_canvas = FigureCanvasTkAgg(figure, master=canvas)
    plot_canvas.get_tk_widget().place(
        x=plot_x,
        y=plot_y,
        width=plot_width,
        height=plot_height
    )
    plot_canvas.draw()

def button_clicked_for_manchester():
    binary_data = read_data_from_file()
    square_signal = generate_square_signal(binary_data)
    manchester_signal = generate_manchester_signal(binary_data)
    update_plot_for_manchester(square_signal, manchester_signal)

def generate_miller_signal(binary_data):
    signal = []
    last_value = 1
    for bit in binary_data:
        if bit == '0':
            signal.extend([last_value]*100)
        elif bit == '1':
            signal.extend([last_value] * 50 + [-last_value] * 50) 
        else:
            raise ValueError("Invalid binary data. Please enter only 0s and 1s.")

    return signal


def update_plot_for_miller(signal1, signal2):
    figure = Figure(figsize=(8, 6)) 
    ax1 = figure.add_subplot(211)
    ax1.plot(signal1)
    ax1.set_ylabel("Signal Value")
    ax1.set_title("Input")
    ax2 = figure.add_subplot(212)
    ax2.plot(signal2)
    ax2.set_ylabel("Signal Value")
    ax2.set_xlabel("Miller Signal")
    canvas.delete("plot")
    plot_width = window.winfo_width() 
    desired_plot_height = 400 
    available_height = canvas.winfo_height() - sum(
        widget.winfo_height() for widget in canvas.winfo_children() if widget != canvas)
    plot_height = min(desired_plot_height, available_height)
    plot_x = (plot_width - plot_width) / 2  # Center horizontally
    plot_y = (canvas.winfo_height() - plot_height) / 1.65  # Center vertically
    plot_canvas = FigureCanvasTkAgg(figure, master=canvas)
    plot_canvas.get_tk_widget().place(
        x=plot_x,
        y=plot_y,
        width=plot_width,
        height=plot_height
    )
    plot_canvas.draw()

def button_clicked_for_miller():
    binary_data = read_data_from_file()
    square_signal = generate_square_signal(binary_data)
    miller_signal = generate_miller_signal(binary_data)
    update_plot_for_miller(square_signal, miller_signal)

def generate_hdb3_signal(binary_data, duration=4):
    signal = []
    zero_count = 0
    last_nonzero = 1
    for bit in binary_data:
        if bit == '0':
            zero_count += 1
            if zero_count == 4:
                if sum(signal[-3*duration:]) == 0:  
                    signal.extend([last_nonzero] * duration)  
                else:
                    signal.extend([0] * duration) 
                    continue
                zero_count = 0
            else:
                signal.extend([0] * duration)
        elif bit == '1':
            if zero_count == 0 or zero_count == 4:
                last_nonzero = -last_nonzero
            signal.extend([last_nonzero] * duration)
            zero_count = 0
        else:
            raise ValueError("Invalid binary data. Please enter only 0s and 1s.")
    return signal

def update_plot_for_hdb3(signal1, signal2):
    figure = Figure(figsize=(8, 6)) 
    ax1 = figure.add_subplot(211)
    ax1.plot(signal1)
    ax1.set_ylabel("Signal Value")
    ax1.set_title("Input")
    ax2 = figure.add_subplot(212)
    ax2.plot(signal2)
    ax2.set_ylabel("Signal Value")
    ax2.set_xlabel("HDB3 Signal")
    canvas.delete("plot")
    plot_width = window.winfo_width() 
    desired_plot_height = 400 
    available_height = canvas.winfo_height() - sum(
        widget.winfo_height() for widget in canvas.winfo_children() if widget != canvas)
    plot_height = min(desired_plot_height, available_height)
    plot_x = (plot_width - plot_width) / 2  # Center horizontally
    plot_y = (canvas.winfo_height() - plot_height) / 1.65  # Center vertically
    plot_canvas = FigureCanvasTkAgg(figure, master=canvas)
    plot_canvas.get_tk_widget().place(
        x=plot_x,
        y=plot_y,
        width=plot_width,
        height=plot_height
    )
    plot_canvas.draw()

def button_clicked_for_hdb3():
    binary_data = read_data_from_file()
    square_signal = generate_square_signal(binary_data)
    miller_signal = generate_hdb3_signal(binary_data)
    update_plot_for_hdb3(square_signal, miller_signal)

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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    625.0,
    87.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button_clicked_for_nrz,
    relief="flat"
)
button_1.place(
    x=168.0,
    y=166.0,
    width=148.0,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button_clicked_for_hdb3,
    relief="flat"
)
button_2.place(
    x=964.0,
    y=166.0,
    width=148.0,
    height=35.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=button_clicked_for_miller,
    relief="flat"
)
button_3.place(
    x=765.0,
    y=166.0,
    width=148.0,
    height=35.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=button_clicked_for_manchester,
    relief="flat"
)
button_4.place(
    x=566.0,
    y=166.0,
    width=148.0,
    height=35.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=button_clicked_for_rz,
    relief="flat"
)
button_5.place(
    x=367.0,
    y=166.0,
    width=148.0,
    height=35.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui_4,
    relief="flat"
)
button_6.place(
    x=1137.0,
    y=654.0,
    width=119.0,
    height=50.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=delete_all_plots,
    relief="flat"
)
button_7.place(
    x=588.0,
    y=618.0,
    width=116.0,
    height=27.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui_2,
    relief="flat"
)
button_8.place(
    x=31.0,
    y=654.0,
    width=119.0,
    height=50.0
)

window.resizable(False, False)
window.mainloop()
