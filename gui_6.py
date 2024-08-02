
import numpy as np
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Desktop\build\assets\frame6")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_gui_5():
    gui_5 = r"C:\Users\HP\Desktop\build\gui_5.py"
    os.system("python "+ gui_5)

def open_gui_7():
    gui_7 = r"C:\Users\HP\Desktop\build\gui_7.py"
    os.system("python "+ gui_7)

def read_binary_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()
    return list(data)

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

def add_noise(t, y, noise_level=0.4):
    noise = np.random.normal(0, noise_level, len(y))
    y_noisy = y + noise
    return t, y_noisy

def remove_noise(t, y_noisy, sigma=1.0):
    y_denoised = gaussian_filter1d(y_noisy, sigma)
    return t, y_denoised

def plot_signals(t, y_original, y_noisy, y_denoised):
    figure = Figure(figsize=(6, 4), dpi=100)
    ax = figure.add_subplot(111)
    ax.plot(t, y_original, label='Original Signal')
    ax.plot(t, y_noisy, label='Noisy Signal', alpha=0.6)
    ax.plot(t, y_denoised, label='Denoised Signal', linestyle='--')
    ax.set_title('Signal Denoising')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.legend()
    ax.grid(True)
    
    canvas.delete("denoise_plot")
    
    plot_width = window.winfo_width() / 2.1
    plot_height = window.winfo_height()
    
    canvas_tkagg = FigureCanvasTkAgg(figure, master=canvas)
    canvas_tkagg.draw()
    canvas_tkagg.get_tk_widget().place(x=plot_width, y=0, width=plot_width, height=plot_height)
    
    canvas.create_window(3 * plot_width / 1.9, plot_height / 1.7, window=canvas_tkagg.get_tk_widget(), tags="denoise_plot")

def plot_denoise():
    file_path = r'C:\Users\HP\Desktop\build\binary_data.txt'
    t, y_original = nyquist_filter(file_path)
    t, y_noisy = add_noise(t, y_original, noise_level=0.4)
    t, y_denoised = remove_noise(t, y_noisy, sigma=1.0)
    plot_signals(t, y_original, y_noisy, y_denoised)

def plot_whitening_filter(ax, binary_data):
    x = range(len(binary_data))
    y = [1 if bit == '1' else -1 for bit in binary_data]
    markerline, stemlines, baseline = ax.stem(x, y, linefmt='b', markerfmt='bo', basefmt='r')
    ax.set_xlabel('Index')
    ax.set_ylabel('Amplitude')
    ax.set_title('Whitening Filter Plot')
    ax.grid(True)

def update_plot_for_signals(binary_data):
    figure = Figure(figsize=(8, 6))
    ax = figure.add_subplot(111)
    
    # Whitening Filter Plot
    plot_whitening_filter(ax, binary_data)

    canvas.delete("plot")
    
    plot_width = window.winfo_width() / 2.1
    desired_plot_height = 250
    available_height = canvas.winfo_height() - sum(
        widget.winfo_height() for widget in canvas.winfo_children() if widget != canvas
    )
    plot_height = min(desired_plot_height, available_height)
    plot_x = (canvas.winfo_width() - plot_width) / 30
    plot_y = (canvas.winfo_height() - plot_height) / 1.6

    plot_canvas = FigureCanvasTkAgg(figure, master=canvas)
    plot_canvas.get_tk_widget().place(
        x=plot_x,
        y=plot_y,
        width=plot_width,
        height=plot_height
    )
    plot_canvas.draw()

def button_clicked_for_whitening_filter():
    binary_data = read_binary_data(r'C:\Users\HP\Desktop\build\binary_data.txt')
    update_plot_for_signals(binary_data)

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
    command=open_gui_7,
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
    command=plot_denoise,
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
    command=button_clicked_for_whitening_filter,
    relief="flat"
)
button_3.place(
    x=191.0,
    y=175.0,
    width=302.0,
    height=35.0
)

canvas.create_rectangle(
    640.000022070315,
    163.0,
    640.0001220703126,
    670.0,
    fill="#000000",
    outline="")

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui_5,
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
