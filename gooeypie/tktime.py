# Import Library
from tkinter import *
 
# Create Object
root = Tk()
 
# Set title
root.title("Password Locker")
 
# Set Geometry
root.geometry("400x400")

# Open New Window

def encdenc():
    pass

def login():
    global second
    second = Toplevel()
    second.title("Password Locker")
    second.geometry("400x400")
    exit_button = Button(root, text="Exit", command=close).pack(pady=10)
    exit_button.pack(pady=20)
# my_text = Text(root, width=60, height=20)
# my_text.pack(pady=20)

# Show the window
def signup():
    global second
    second = Toplevel()
    second.title("Password Locker")
    second.geometry("400x400")
 
# Hide the window
def close():
    root.destroy()

# Add Buttons
loginbtn = Button(root, text="Login", command=login).pack(pady=10)
signupbtn = Button(root, text="Sign up", command=signup).pack(pady=10) 
   
# Execute Tkinter
root.mainloop()