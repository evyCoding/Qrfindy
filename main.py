import tkinter as tk
from PIL import Image, ImageTk

# setting up the root window
root = tk.Tk()
# changing the logo of the app
root.iconbitmap(r'logos/logo-color.ico')
root.title("Qrfindy")
# changing the background colorf
root.config(bg="#FFF455")
# changing the dimensions of the window
root.geometry("300x450")
root.wm_maxsize(300, 450)
root.wm_minsize(300, 450)
#
root.mainloop()