import customtkinter as ctk
from tkinter import filedialog

def pick_folder():
    root = ctk.CTk()
    root.withdraw()

    return filedialog.askdirectory()