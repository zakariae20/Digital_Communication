from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import os
import numpy as np


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Desktop\build\assets\frame4")

def open_gui_5():
    gui_5 = r"C:\Users\HP\Desktop\build\gui_5.py"
    os.system("python "+ gui_5)

def open_gui_3():
    gui_3 = r"C:\Users\HP\Desktop\build\gui_3.py"
    os.system("python "+ gui_3)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def read_data_from_file():
    with open("binary_data.txt", "r") as file:
        binary_data = file.read()
    return binary_data

def read_binary_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()
    return list(data)

def plot_whitening_filter(ax, binary_data):
    x = range(len(binary_data))
    y = [1 if bit == '1' else -1 for bit in binary_data]
    markerline, stemlines, baseline = ax.stem(x, y, linefmt='b', markerfmt='bo', basefmt='r')
    ax.set_xlabel('Index')
    ax.set_ylabel('Amplitude')
    ax.set_title('Whitening Filter Plot')
    ax.grid(True)

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

def update_plot_for_signals(signal1, binary_data):
    figure, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [1, 1]})
    
    # Adjust space between plots
    figure.subplots_adjust(hspace=0.75)
    
    # NRZ Signal Plot
    ax1.plot(signal1)
    ax1.set_ylabel("Signal Value")
    ax1.set_xlabel("NRZ Signal")
    ax1.grid(True)

    # Whitening Filter Plot
    plot_whitening_filter(ax2, binary_data)
    
    canvas.delete("plot")
    
    plot_width = window.winfo_width() / 2.1
    desired_plot_height = 500  # Combined height for both plots
    available_height = canvas.winfo_height() - sum(
        widget.winfo_height() for widget in canvas.winfo_children() if widget != canvas
    )
    plot_height = min(desired_plot_height, available_height)
    plot_x = (canvas.winfo_width() - plot_width) / 30  # Center horizontally
    plot_y = (canvas.winfo_height() - plot_height) / 1.3  # Center vertically

    plot_canvas = FigureCanvasTkAgg(figure, master=canvas)
    plot_canvas.get_tk_widget().place(
        x=plot_x,
        y=plot_y,
        width=plot_width,
        height=plot_height
    )
    plot_canvas.draw()

def button_clicked_for_nrz():
    binary_data = read_binary_data(r'C:\Users\HP\Desktop\build\binary_data.txt')
    nrz_signal = generate_nrz_signal(binary_data)
    update_plot_for_signals(nrz_signal, binary_data)

def nyquist_filter(file_path):
    samples_per_bit = 100
    # Read binary data from the text file
    with open(file_path, 'r') as file:
        binary_data = file.read().strip()
    t = np.linspace(0, len(binary_data), len(binary_data) * samples_per_bit)
    y = np.zeros(len(t))
    # Define a Gaussian function
    def gaussian(x, mu, sigma):
        return np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    # Define a small sinusoidal wave function
    def sinusoidal_wave(x, amplitude, frequency):
        return amplitude * np.sin(2 * np.pi * frequency * x)
    for i, bit in enumerate(binary_data):
        start_idx = i * samples_per_bit
        end_idx = (i + 1) * samples_per_bit
        center = (start_idx + end_idx) / 2
        sigma = samples_per_bit / 8  # Standard deviation of the Gaussian
        if bit == '1':
            y[start_idx:end_idx] = gaussian(np.linspace(start_idx, end_idx, samples_per_bit), center, sigma)
        elif bit == '0':
            y[start_idx:end_idx] = -gaussian(np.linspace(start_idx, end_idx, samples_per_bit), center, sigma)
        # Adding the small sinusoidal wave between symbols
        if i < len(binary_data) - 1:
            transition_end = end_idx + samples_per_bit // 2
            x_trans = np.linspace(end_idx, transition_end, samples_per_bit // 2)
            y[end_idx:transition_end] += sinusoidal_wave(x_trans, amplitude=0.1, frequency=2)

    return t, y

def plot_nyquist_filter(t, y):
    figure = Figure(figsize=(6, 4), dpi=100)
    ax = figure.add_subplot(111)
    ax.plot(t, y)
    ax.set_title('Nyquist Filter')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.grid(True)
    ax.set_ylim(-1.5, 1.5)
    
    canvas.delete("nyquist_plot")
    
    plot_width = window.winfo_width() / 2.1
    plot_height = window.winfo_height()
    
    # Create the canvas and add it to the Tkinter canvas
    canvas_tkagg = FigureCanvasTkAgg(figure, master=canvas)
    canvas_tkagg.draw()
    canvas_tkagg.get_tk_widget().place(x=plot_width, y=0, width=plot_width, height=plot_height)
    
    canvas.create_window(3 * plot_width / 1.9, plot_height / 1.7, window=canvas_tkagg.get_tk_widget(), tags="nyquist_plot")

# Add a button to plot the Nyquist filter
def on_plot_nyquist_filter():
    file_path = r'C:\Users\HP\Desktop\build\binary_data.txt'
    t, y = nyquist_filter(file_path)
    plot_nyquist_filter(t, y)

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
    command=open_gui_5,
    relief="flat"
)
button_1.place(
    x=1137.0,
    y=652.0,
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

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=on_plot_nyquist_filter,
    relief="flat"
)
button_2.place(
    x=793.0,
    y=175.0,
    width=302.0,
    height=35.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=button_clicked_for_nrz,
    relief="flat"
)
button_3.place(
    x=191.0,
    y=175.0,
    width=302.0,
    height=35.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui_3,
    relief="flat"
)
button_4.place(
    x=24.0,
    y=652.0,
    width=119.0,
    height=50.0
)

canvas.create_line(640, 163, 640, 670, fill="#1167B1", width=3)

def draw_diamond(x, y, size):
    points = [x, y - size, x + size, y, x, y + size, x - size, y]
    canvas.create_polygon(points, fill="#2A9DF4", outline="#2A9DF4")

draw_diamond(640, 163, 10)
draw_diamond(640, 670, 10)

window.resizable(False, False)
window.mainloop()