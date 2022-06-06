import tkinter
import customtkinter
from tkinter import *
from customencdenc import encdec

def login_page():
    customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    app = customtkinter.CTk()
    app.geometry("600x600")
    app.title("CustomTkinter simple_example.py")
    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
    entry_1.place(relx=0.5, rely=0.2, anchor=CENTER)

    entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
    entry_2.place(relx=0.5, rely=0.3, anchor=CENTER)

    entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
    entry_3.place(relx=0.5, rely=0.4, anchor=CENTER)

    button_1 = customtkinter.CTkButton(master=frame_1, command=encdec, text="Log In")
    button_1.place(relx=0.5, rely=0.8, anchor=CENTER)

    app.mainloop()