import customtkinter as ctk
from tkinter import filedialog

def pick_folder():
    root = ctk.CTk()
    root.withdraw()

    root.attributes('-topmost', True)
    root.focus_force()

    selected_folder = filedialog.askdirectory()

    root.destroy()
    return selected_folder if selected_folder else None