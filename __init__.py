import os
from tkinter import *
import customtkinter
from PIL import Image
import CTk_MainPage_GUI

class LoginPage():
    def __init__(self):
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.root = customtkinter.CTk()
        self.root.geometry('450x400')
        self.root.minsize(450, 400)
        self.root.maxsize(450, 400)

        self.root.title("THE VAULT")

        self.image_path = os.path.join(os.path.dirname(__file__), 'images')

        self.root.iconbitmap(os.path.join(self.image_path, "RedLockNeon.ico"))

        self.createWidgets()

    def createWidgets(self):

        self.f1 = customtkinter.CTkFrame(self.root, width=200, height=200, border_width=1)

        self.f1.pack(fill="both", expand=True, padx=100, pady=50)

        # lock = customtkinter.CTkImage(Image.open(os.path.join(image_path, "RedLock.png")), size = (100, 100))
        # lock_image = customtkinter.CTkLabel(f2, image = lock, text = '')
        # lock_image.pack()

        self.master_password_entry = customtkinter.CTkEntry(self.f1, placeholder_text="Master Password", corner_radius=30, border_color="red")
        self.master_password_entry.place(anchor="c", rely=.7, relx=.5)

        self.root.update()
        self.master_password_entry.focus()

        self.master_password_button = customtkinter.CTkButton(self.f1, text="Submit", fg_color="Red", hover_color="red4",command=lambda master_password_entry=self.master_password_entry: self.testEntryButton(master_password_entry))
        self.master_password_button.pack(pady=20, side="bottom")

        self.root.bind('<Return>', lambda event, master_password_entry=self.master_password_entry: self.testEntryButton(self.master_password_entry))
        self.root.bind('<Escape>', self.quitWindow)
        self.root.mainloop()

    def testEntryButton(self, entry):
        if(entry.get() == "F"):
            print("Pass")
            self.root.destroy()
            CTk_MainPage_GUI.MainPage()
            
        else:
            print("Fail")

    def testEntryReturn(self, entry, event):
        if(entry.get() == "F"):
            print("Pass")
            self.root.destroy()
            CTk_MainPage_GUI.MainPage()
        else:
            print("Fail")

    def quitWindow(self, event):
        self.root.destroy()

LoginPage()