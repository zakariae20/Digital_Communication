
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Desktop\build\assets\frame5")

def open_gui_4():
    gui_4 = r"C:\Users\HP\Desktop\build\gui_4.py"
    os.system("python "+ gui_4)

def open_gui_6():
    gui_6 = r"C:\Users\HP\Desktop\build\gui_6.py"
    os.system("python "+ gui_6)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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

def plot_noise_signal():
    file_path = r'C:\Users\HP\Desktop\build\binary_data.txt' 
    t, y = nyquist_filter(file_path)
    t, y_noisy = add_noise(t, y)

    fig, ax = plt.subplots()
    ax.plot(t, y_noisy)
    ax.set(title='Noisy Signal', xlabel='Time', ylabel='Amplitude')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=200, y=150, width=910, height=520)


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
    command=open_gui_6,
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
    command=open_gui_4,
    relief="flat"
)
button_2.place(
    x=25.0,
    y=646.0,
    width=119.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=plot_noise_signal,
    relief="flat"
)
button_3.place(
    x=551.0,
    y=620.0,
    width=179.0,
    height=32.0
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
