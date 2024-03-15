import tkinter as tk
from PIL import Image, ImageTk


class Qrfindy:
    def __int__(self):
        # setting up the root window
        root = tk.Tk()
        # changing the logo of the app
        root.iconbitmap(r'logos/logo-color.ico')
        root.title("Qrfindy")
        return root
    def __firstWind(self, root: tk) -> None:
        # changing the background colorf
        root.config(bg="#FFF455")
        # changing the dimensions of the window
        root.geometry("300x450")
        root.wm_maxsize(300, 450)
        root.wm_minsize(300, 450)
        # element 1
        logo_text = "Qrfindy\n"
        logo_text_label = tk.Label(root,
                                   text=logo_text,
                                   fg="#4CCD99",
                                   font=("Lilita One", 30),
                                   bg="#FFF455")
        logo_text_label.pack()
        # element 2
        button = tk.Button(root,
                           text="Get Started",
                           bg="#FFF455",
                           font=("Lilita One", 30),
                           fg="#4CCD99")
        button.pack(pady=80)

