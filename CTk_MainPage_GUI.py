import os
from tkinter import *
import customtkinter
from PIL import Image
import __init__

class MainPage():
    def __init__(self):
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.root = customtkinter.CTk()
        self.root.geometry('450x400')

        self.root.title("THE VAULT")

        self.image_path = os.path.join(os.path.dirname(__file__), 'images')

        self.root.iconbitmap(os.path.join(self.image_path, "RedLockNeon.ico"))

        self.root.mainloop()

