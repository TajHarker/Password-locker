# Import Library
from tkinter import *
 
# Create Object
root = Tk()
 
# Set title
root.title("Password Locker")
 
# Set Geometry
root.geometry("400x400")
 
# Open New Window
def login():
    global second
    second = Toplevel()
    second.title("Password Locker")
    second.geometry("400x400")
 
# Show the window
def signup():
    global second
    second = Toplevel()
    second.title("Password Locker")
    second.geometry("400x400")
 
# Hide the window
def hide():
    root.withdraw()

 
# Add Buttons
Button(root, text="Login", command=login).pack(pady=10)
Button(root, text="Sign up", command=signup).pack(pady=10)
 
# Execute Tkinter
root.mainloop()