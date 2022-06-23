import tkinter
import customtkinter
from tkinter import *
import random
import SQL

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
app = customtkinter.CTk() 
app.geometry("600x600") #Sets the size of the grid
app.title("Password-Locker") #The title of the window

class globalIDS(): #Makes it so you can access UserID from anywhere
    UserID= 0

def signup_page(): #Displays 'Generate Password'
    signup = customtkinter.CTkToplevel(master=app)  #CTKToplevel puts the fram on-top of the previous window
    signup.geometry("600x600")
    signup.title("Password-Locker")

    def passgen_button(): #When button is clicked it runs this function
        signup.withdraw() #Closes signup_page
        passgen_page() #Opens passgen_page

    frame_1 = customtkinter.CTkFrame(master=signup) #Sets a frame within the signup window
    frame_1.pack(pady=60, padx=60, fill="both", expand=True) #Sets the padding/borders of the window

    button_1 = customtkinter.CTkButton(master=frame_1, command=passgen_button, text="Generate Primary Key") #Creates a button that runs the passgen_buttun function
    button_1.place(relx=0.5, rely=0.5, anchor=CENTER) #Controls the position of the button on the window

    app.mainloop() #runs app

def passgen_page(): #Generates primary keys
    passgen = customtkinter.CTkToplevel(master=app)
    passgen.geometry("600x600")
    passgen.title("Password-Locker")

    def login_button(): #runs this function once the button is pressed
        passgen.withdraw() #closes the passgen window
        login_page() #opens the login_page

    i = 0
    array = []  #Creates empty array
    while i < 3: #loops 3 times
        lines = open("words.txt").readlines() #opens words.txt
        myword = random.choice(lines) #selects random word
        myword = myword.strip('\n') #removes the lines between words
        myword = str(myword) #stores 'myword' as a string
        i += 1 #increments i by 1
        array.append(myword) #stores 'myword' in the array
    SQL.signup(array) #enters the variable 'array' into the SQL.signup function

    frame_1 = customtkinter.CTkFrame(master=passgen) #sets the fram
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    label_1 = customtkinter.CTkLabel(master=frame_1, text=array[0], justify=tkinter.LEFT) #Creates a label on the window displaying the first value in the array
    label_1.pack(pady=12, padx=10) #Padding of the label
    label_1.place(relx=0.2, rely=0.55, anchor=CENTER) #Dimensions of the label
    label_1.configure(font=("Futura", 20)) #font and text size of the label

    label_2 = customtkinter.CTkLabel(master=frame_1, text=array[1], justify=tkinter.LEFT) #Creates another label
    label_2.pack(pady=12, padx=10) #Padding of the label
    label_2.place(relx=0.5, rely=0.55, anchor=CENTER) #Sets position of the label
    label_2. configure(font=("Futura", 20)) #Sets the font and text size

    label_3 = customtkinter.CTkLabel(master=frame_1, text=array[2], justify=tkinter.LEFT) #Creates another label
    label_3.pack(pady=12, padx=10) #Padding of the label
    label_3.place(relx=0.8, rely=0.55, anchor=CENTER) #Sets position of the label
    label_3. configure(font=("Futura", 20)) #Sets the font and text size

    label_4 = customtkinter.CTkLabel(master=frame_1, text='Your Primary Keys Are:', justify=tkinter.LEFT) #Displays 'Your primary keys are' 
    label_4.pack(pady=12, padx=10) #Padding of the label
    label_4.place(relx=0.5, rely=0.3, anchor=CENTER) #Sets position of the label
    label_4. configure(font=("Futura", 30)) #Sets the font and text size

    button_1 = customtkinter.CTkButton(master=frame_1, command=login_button, text="Login") #Creates a button that goes to the login_button function
    button_1.place(relx=0.5, rely=0.8, anchor=CENTER) #Sets position
    
def main(): #Main window
    frame_1 = customtkinter.CTkFrame(master=app) #Creates new frame
    frame_1.pack(pady=60, padx=60, fill="both", expand=True) #Sets padding

    def login_button(): #Runs when 'login_button' is pressed
        app.withdraw() #Closes the main window
        login_page() #runs 'login_page'

    def signup_button(): #Runs when 'signup_button' is pressed
        app.withdraw() #closes the main window
        signup_page() #Opens the 'signup_page'
        
    button_1 = customtkinter.CTkButton(master=frame_1, command=login_button, text="Log In") #Creates button
    button_1.place(relx=0.5, rely=0.4, anchor=CENTER) #Position of button

    button_2 = customtkinter.CTkButton(master=frame_1, command=signup_button, text="Sign Up") #Creates button
    button_2.place(relx=0.5, rely=0.6, anchor=CENTER) #Position of button

    app.mainloop() #Runs the window

def login_page(): #Where user enters their primary keys
    login = customtkinter.CTkToplevel(master=app) 
    login.geometry("600x600")
    login.title("Password-Locker")
    frame_1 = customtkinter.CTkFrame(master=login)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    def login_button(): #Runs when the login_button in pressed
        if SQL.login(entry_1.get(), entry_2.get(), entry_3.get()) == True: #Enters the users inputs into the SQL.login function and checks if true
            globalIDS.UserID = SQL.retrieve_userID(entry_1.get(), entry_2.get(), entry_3.get()) #Retrieves the useID of assigned to the entries
            login.withdraw() #closes login page
            encdec_page() #runs encdec_page
        else:
            label_2 = customtkinter.CTkLabel(master=frame_1, text='Incorrect Primary Keys', justify=tkinter.LEFT) #Displays incorrect primary key
            label_2.pack(pady=12, padx=10) #padding
            label_2.place(relx=0.5, rely=0.7, anchor=CENTER) #position
            label_2. configure(font=("Helveta", 15,)) #text and font

    label_1 = customtkinter.CTkLabel(master=frame_1, text='Login', justify=tkinter.LEFT) #displays login
    label_1.pack(pady=12, padx=10)
    label_1.place(relx=0.5, rely=0.2, anchor=CENTER)
    label_1. configure(font=("Helveta", 35,))

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="●●●●●") #Gets user input and displays ●●●●●
    entry_1.place(relx=0.5, rely=0.4, anchor=CENTER)

    entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="●●●●●") #Gets user input and displays ●●●●●
    entry_2.place(relx=0.5, rely=0.5, anchor=CENTER)

    entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="●●●●●") #Gets user input and displays ●●●●●
    entry_3.place(relx=0.5, rely=0.6, anchor=CENTER)

    button_1 = customtkinter.CTkButton(master=frame_1, command=login_button, text="Log In") #Login button
    button_1.place(relx=0.5, rely=0.8, anchor=CENTER)

    app.mainloop()

def encdec_page(): #the main page once logged in
    encdec = customtkinter.CTk()
    encdec.geometry("600x600")
    encdec.title("Password-Locker")
    frame_1 = customtkinter.CTkFrame(master=encdec)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    def encode_button(): #Runs when encode_button is pressed
        encdec.withdraw() #Closes current window
        encode_page() #Goes to encode_page window

    def decode_button(): #Runs decode_page when pressed
        encdec.withdraw() #Closes current window
        decode_page() #Goes to decode_page window

    button_1 = customtkinter.CTkButton(master=frame_1, command=encode_button, text="Encode") #Encode button
    button_1.place(relx=0.5, rely=0.4, anchor=CENTER)

    button_2 = customtkinter.CTkButton(master=frame_1, command=decode_button, text="Decode") #Decode button
    button_2.place(relx=0.5, rely=0.6, anchor=CENTER)

    app.mainloop()

def encode_page(): #The encode passwords page
    enc = customtkinter.CTk()
    enc.geometry("600x600")
    enc.title("Password-Locker")
    frame_1 = customtkinter.CTkFrame(master=enc)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    def encodepassword_button(): #Creates random 8 character string
        string = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%*()" #Random 8 charcaters
        array = [] #Open arrray
        for c in string: #Runs one time for every character in 'string'
            array += [c] #Adds characters to the array
        randpassword = "" #sets randpassword as an empty string
        for i in range(8): #runs 8 times
            ((array[random.randint(0, len(array)-1)])) #stores a random character from the string in the array
            randpassword = randpassword + (random.choice(string)) #Stores the random strings into the randpassword variable
        password = entry_1.get() #Gets an input from user
        currentpass = SQL.encode(globalIDS.UserID, password, randpassword) #Enters userID, password and randpassword into the SQL.encode function
        label_1.configure(text = currentpass)
    
    def To_menu(): #Closes current window and opens encdec_page
        enc.withdraw()
        encdec_page()
     
    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="") #Gets user input
    entry_1.place(relx=0.5, rely=0.35, anchor=CENTER)

    button_1 = customtkinter.CTkButton(master=frame_1, command=encodepassword_button, text="Encode") #Button goes to encodepassword_button function
    button_1.place(relx=0.5, rely=0.5, anchor=CENTER)

    button_1 = customtkinter.CTkButton(master=frame_1, command=To_menu, text="Menu")
    button_1.place(relx=0.5, rely=0.6, anchor=CENTER)

    label_1 = customtkinter.CTkLabel(master=frame_1, text='', justify=tkinter.LEFT) #Displays encoded password
    label_1.pack(pady=12, padx=10)
    label_1.place(relx=0.5, rely=0.425, anchor=CENTER)
    label_1. configure(font=("Helveta", 15))

    app.mainloop()

def decode_page(): #Gets the encoded password from user
    enc = customtkinter.CTk()
    enc.geometry("600x600")
    enc.title("Password-Locker")
    frame_1 = customtkinter.CTkFrame(master=enc)
    frame_1.pack(pady=60, padx=60, fill="both", expand=True)

    def To_menu(): #Closes current window and opens encdec_page
        enc.withdraw()
        encdec_page()

    def decode():
        encpassword = entry_1.get()
        decodedpass = SQL.decode(globalIDS.UserID, encpassword) #Gets decoded password 
        label_1.configure(text=decodedpass)

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="")
    entry_1.place(relx=0.5, rely=0.35, anchor=CENTER)

    button_1 = customtkinter.CTkButton(master=frame_1, command=To_menu, text="Menu")
    button_1.place(relx=0.5, rely=0.6, anchor=CENTER)

    button_2 = customtkinter.CTkButton(master=frame_1, command=decode, text="Decode") #Returns to the encdec page
    button_2.place(relx=0.5, rely=0.5, anchor=CENTER)

    label_1 = customtkinter.CTkLabel(master=frame_1, text='', justify=tkinter.LEFT) #Displays encoded password
    label_1.pack(pady=12, padx=10)
    label_1.place(relx=0.5, rely=0.425, anchor=CENTER)
    label_1. configure(font=("Helveta", 15))

    app.mainloop()

main() #Begins program