import gooeypie as gp
import random

app = gp.GooeyPieApp('Password Locker')
app.width = 600
app.height = 500

def login(event):
    login_lbl.text = login

def signup(event):
    signup_lbl.text = generate_password

def generate_password(event):
    passgen_btn = gp.Button(app, 'Generate password' , generate_password)
    passgen_lbl = gp.Label(app, '')

    app.set_grid(2, 1)
    app.add(passgen_btn, 1, 1, align='center', valign='bottom')
    app.add(passgen_lbl, 2, 1, align='center', valign='middle')
    i = 0
    array = []
    while i < 3:
        lines = open("Password-locker/gooeypie/words.txt").readlines() 
        myword = random.choice(lines)
        myword = str(myword)
        array.append(myword)
        i += 1
    passgen_lbl.text = ('Your three passwords are', array[0] + array[1] + array[2])

login_btn = gp.Button(app, 'Login', login)
signup_lbl = gp.Label(app, '')

signup_btn = gp.Button(app, 'Signup', signup)
login_lbl = gp.Label(app, '')

app.set_grid(2, 1)
app.add(login_btn, 1, 1, align='center', valign='middle')
app.add(signup_lbl, 2, 1, align='center', valign='bottom')

app.set_grid(2, 1)
app.add(signup_btn, 1, 1, align='center', valign='bottom')
app.add(login_lbl, 2, 1, align='center', valign='middle')

app.run()