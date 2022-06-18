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
        signup.withdraw()
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

    def login_button():
        passgen.withdraw()
        login_page()

    i = 0
    array = []
    while i < 3:
        lines = open("gooeypie/words.txt").readlines() 
        myword = random.choice(lines)
        myword = str(myword)
        array.append(myword)
        i += 1

    frame_1 = customtkinter.CTkFrame(master=passgen)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    label_1 = customtkinter.CTkLabel(master=frame_1, text=array[0], justify=tkinter.LEFT)
    label_1.pack(pady=12, padx=10)
    label_1.place(relx=0.2, rely=0.55, anchor=CENTER)
    label_1. configure(font=("Futura", 20))

    label_2 = customtkinter.CTkLabel(master=frame_1, text=array[1], justify=tkinter.LEFT)
    label_2.pack(pady=12, padx=10)
    label_2.place(relx=0.5, rely=0.55, anchor=CENTER)
    label_2. configure(font=("Futura", 20))

    label_3 = customtkinter.CTkLabel(master=frame_1, text=array[2], justify=tkinter.LEFT)
    label_3.pack(pady=12, padx=10)
    label_3.place(relx=0.8, rely=0.55, anchor=CENTER)
    label_3. configure(font=("Futura", 20)) 

    label_4 = customtkinter.CTkLabel(master=frame_1, text='Your Primary Keys Are:', justify=tkinter.LEFT)
    label_4.pack(pady=12, padx=10)
    label_4.place(relx=0.5, rely=0.3, anchor=CENTER)
    label_4. configure(font=("Futura", 30))

    button_1 = customtkinter.CTkButton(master=frame_1, command=login_button, text="Login")
    button_1.place(relx=0.5, rely=0.8, anchor=CENTER)
    
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

    button_2 = customtkinter.CTkButton(master=frame_1, command=signup_button, text="Sign Up")
    button_2.place(relx=0.5, rely=0.6, anchor=CENTER)

    app.mainloop()

def login_page():
    login = customtkinter.CTkToplevel(master=app)
    login.geometry("600x600")
    login.title("Password-Locker")
    frame_1 = customtkinter.CTkFrame(master=login)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    def login_button():
        login.withdraw()
        encdec_page()

    label_1 = customtkinter.CTkLabel(master=frame_1, text='Login', justify=tkinter.LEFT)
    label_1.pack(pady=12, padx=10)
    label_1.place(relx=0.5, rely=0.2, anchor=CENTER)
    label_1. configure(font=("Helveta", 35,))

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="●●●●●")
    entry_1.place(relx=0.5, rely=0.4, anchor=CENTER)

    entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="●●●●●")
    entry_2.place(relx=0.5, rely=0.5, anchor=CENTER)

    entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="●●●●●")
    entry_3.place(relx=0.5, rely=0.6, anchor=CENTER)

    button_1 = customtkinter.CTkButton(master=frame_1, command=login_button, text="Log In")
    button_1.place(relx=0.5, rely=0.8, anchor=CENTER)

    app.mainloop()

def encdec_page():
    encdec = customtkinter.CTk()
    encdec.geometry("600x600")
    encdec.title("Password-Locker")
    frame_1 = customtkinter.CTkFrame(master=encdec)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    def encode_button():
        encdec.withdraw()
        encode_page()

    def decode_button():
        encdec.withdraw()
        decode_page()

    button_1 = customtkinter.CTkButton(master=frame_1, command=encode_button, text="Encode")
    button_1.place(relx=0.5, rely=0.4, anchor=CENTER)

    button_2 = customtkinter.CTkButton(master=frame_1, command=decode_button, text="Decode")
    button_2.place(relx=0.5, rely=0.6, anchor=CENTER)

    app.mainloop()

def encode_page():
    enc = customtkinter.CTk()
    enc.geometry("600x600")
    enc.title("Password-Locker")
    frame_1 = customtkinter.CTkFrame(master=enc)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    def encodepassword_button():
        password = entry_1.get()
        print(password)
        enc.withdraw()
        encodepassword_page()
        
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
    entry_1.place(relx=0.5, rely=0.45, anchor=CENTER)

    button_1 = customtkinter.CTkButton(master=frame_1, command=encodepassword_button, text="Encode")
    button_1.place(relx=0.5, rely=0.6, anchor=CENTER)

    app.mainloop()

def encodepassword_page():
    enc = customtkinter.CTk()
    enc.geometry("600x600")
    enc.title("Password-Locker")
    frame_1 = customtkinter.CTkFrame(master=enc)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)


    def encdec_button():
        enc.withdraw()
        encdec_page()

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
    entry_1.place(relx=0.5, rely=0.45, anchor=CENTER)

    button_1 = customtkinter.CTkButton(master=frame_1, command=encdec_button, text="Menu")
    button_1.place(relx=0.5, rely=0.6, anchor=CENTER)

    label_1 = customtkinter.CTkLabel(master=frame_1, text='Encoded', justify=tkinter.LEFT)
    label_1.pack(pady=12, padx=10)
    label_1.place(relx=0.5, rely=0.525, anchor=CENTER)
    label_1. configure(font=("Helveta", 15))

    app.mainloop()

def decodepassword_page():
    enc = customtkinter.CTk()
    enc.geometry("600x600")
    enc.title("Password-Locker")
    frame_1 = customtkinter.CTkFrame(master=enc)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)


    def encdec_button():
        enc.withdraw()
        encdec_page()

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
    entry_1.place(relx=0.5, rely=0.45, anchor=CENTER)

    button_1 = customtkinter.CTkButton(master=frame_1, command=encdec_button, text="Menu")
    button_1.place(relx=0.5, rely=0.6, anchor=CENTER)

    label_1 = customtkinter.CTkLabel(master=frame_1, text='Encoded', justify=tkinter.LEFT)
    label_1.pack(pady=12, padx=10)
    label_1.place(relx=0.5, rely=0.525, anchor=CENTER)
    label_1. configure(font=("Helveta", 15))

    app.mainloop()

def decode_page():
    enc = customtkinter.CTk()
    enc.geometry("600x600")
    enc.title("Password-Locker")
    frame_1 = customtkinter.CTkFrame(master=enc)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    def decodepassword_button():
        enc.withdraw()
        decodepassword_page()

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
    entry_1.place(relx=0.5, rely=0.45, anchor=CENTER)

    button_1 = customtkinter.CTkButton(master=frame_1, command=decodepassword_button, text="Decode")
    button_1.place(relx=0.5, rely=0.6, anchor=CENTER)

    app.mainloop()

main()