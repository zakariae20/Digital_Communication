
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Desktop\build\assets\debut")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_gui_principale():
    gui_principale = r"C:\Users\HP\Desktop\build\gui_principale.py"
    os.system("python " + gui_principale)

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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    300.0,
    360.0,
    image=image_image_1
)

canvas.create_rectangle(
    657.0,
    3.0,
    1280.0,
    720.0,
    fill="#074173",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui_principale,
    relief="flat"
)
button_1.place(
    x=719.0,
    y=421.0,
    width=174.0,
    height=49.0
)

canvas.create_text(
    719.0,
    144.0,
    anchor="nw",
    text="CHAINE DE TRANSMISSION",
    fill="#FFFFFF",
    font=("Poppins ExtraBold", 32 * -1)
)

canvas.create_text(
    719.0,
    193.0,
    anchor="nw",
    text="NUMÉRIQUE",
    fill="#FFFFFF",
    font=("Poppins ExtraBold", 32 * -1)
)

canvas.create_text(
    719.0,
    265.0,
    anchor="nw",
    text="Découvrez notre simulateur intuitif de",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 24 * -1)
)

canvas.create_text(
    719.0,
    296.0,
    anchor="nw",
    text="communication numérique. Visualisez,",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 24 * -1)
)

canvas.create_text(
    719.0,
    327.0,
    anchor="nw",
    text="expérimentez et maîtrisez le flux",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 24 * -1)
)

canvas.create_text(
    719.0,
    358.0,
    anchor="nw",
    text="de données facilement.",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 24 * -1)
)
window.resizable(False, False)
window.mainloop()

