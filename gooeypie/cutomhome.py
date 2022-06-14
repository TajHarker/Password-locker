import tkinter
import customtkinter
from tkinter import *
import random

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
app = customtkinter.CTk()
app.geometry("600x600")
app.title("Password-Locker")

def close():
    app.deiconify

def signup_page():
    signup = customtkinter.CTkToplevel(master=app)
    signup.geometry("600x600")
    signup.title("Password-Locker")

    def passgen_button():
        app.withdraw()
        passgen_page()

    frame_1 = customtkinter.CTkFrame(master=signup)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    button_1 = customtkinter.CTkButton(master=frame_1, command=passgen_button, text="Generate Primary Key")
    button_1.place(relx=0.5, rely=0.5, anchor=CENTER)

    app.mainloop()

def passgen_page():
    passgen = customtkinter.CTkToplevel(master=app)
    passgen.geometry("600x600")
    passgen.title("Password-Locker")
    
    frame_1 = customtkinter.CTkFrame(passgen=app)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    i = 0
    array = []
    while i < 3:
        lines = open("words.txt").readlines() 
        myword = random.choice(lines)
        myword = str(myword)
        array.append(myword)
        i += 1

    array = (array[0] + array[1] + array[2])
    label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT)

    #label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Your Primary Keys Are:" + (array))
    label_1.pack(pady=12, padx=10)
    
def main():
    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    def login_button():
        app.withdraw()
        login_page()

    def signup_button():
        app.withdraw()
        signup_page()
        
    button_1 = customtkinter.CTkButton(master=frame_1, command=login_button, text="Log In")
    button_1.place(relx=0.5, rely=0.4, anchor=CENTER)

    button_1 = customtkinter.CTkButton(master=frame_1, command=signup_button, text="Sign Up")
    button_1.place(relx=0.5, rely=0.6, anchor=CENTER)

    app.mainloop()

def login_page():
    login = customtkinter.CTkToplevel(master=app)
    login.geometry("600x600")
    login.title("Password-Locker")
    frame_1 = customtkinter.CTkFrame(master=login)
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

def encdec():
    app = customtkinter.CTk()
    app.geometry("600x600")
    app.title("Password-Locker")
    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    button_1 = customtkinter.CTkButton(master=frame_1, command=login_page, text="Log In")
    button_1.place(relx=0.5, rely=0.4, anchor=CENTER)

    button_1 = customtkinter.CTkButton(master=frame_1, command=close, text="Sign Up")
    button_1.place(relx=0.5, rely=0.6, anchor=CENTER)

    app.mainloop()

main()
