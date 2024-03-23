import tkinter as tk
import qrcode
from PIL import Image, ImageTk


def firstWind(rootwin1):
    # changing the background color
    rootwin1.config(bg="#FFF455")
    # changing the dimensions of the window
    rootwin1.geometry("300x450")
    rootwin1.wm_maxsize(300, 450)
    rootwin1.wm_minsize(300, 450)
    # element 1
    logo_text = "Qrfindy\n"
    logo_text_label = tk.Label(rootwin1,
                               text=logo_text,
                               fg="#4CCD99",
                               font=("Lilita One", 30),
                               bg="#FFF455")
    logo_text_label.pack()
    # element 2
    button = tk.Button(rootwin1,
                       text="Get Started",
                       bg="#FFF455",
                       font=("Lilita One", 30),
                       fg="#4CCD99",
                       command=secondWind(rootwin1)
                       )
    button.pack(pady=80)


def secondWind(root):
    root.destroy()
    # make a new root for the second window
    rootwin2 = tk.Tk()


    # changing the background color
    root.config(bg="#FFF455")
    # changing the dimensions of the window
    root.geometry("300x450")
    root.wm_maxsize(300, 450)
    root.wm_minsize(300, 450)


class Tkfont:
    def __int__(self):
        # setting up the root window
        root = tk.Tk()
        # changing the logo of the app
        root.iconbitmap(r'logos/logo-color.ico')
        root.title("Qrfindy")
        return root

#class Qr :
  #  def __init__(self):
