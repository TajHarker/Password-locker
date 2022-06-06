import tkinter
import customtkinter
from tkinter import *
from customlogin import login_page

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("600x600")
app.title("CustomTkinter simple_example.py")

def login():
    pass

def button_callback():
    print("Log in")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=60, padx=60, fill="both", expand=True)

button_1 = customtkinter.CTkButton(master=frame_1, command=login_page, text="Log In")
button_1.place(relx=0.5, rely=0.4, anchor=CENTER)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Sign Up")
button_1.place(relx=0.5, rely=0.6, anchor=CENTER)

app.mainloop()