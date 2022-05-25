import gooeypie as gp
import random

app = gp.GooeyPieApp('Password Locker')
app.width = 600
app.height = 500

def encdec(event):
    app = gp.GooeyPieApp('Password Locker')
    app.width = 600
    app.height = 500

    app.run()

def menu(event):
    app.destroy()

def login(event):
    app = gp.GooeyPieApp("Password Locker")
    app.width = 600
    app.height = 500

    pass1_inp = gp.Secret(app)
    pass2_inp = gp.Secret(app)
    pass3_inp = gp.Secret(app)
    login_btn = gp.Button(app, 'Login', login)
    
    app.set_grid(4, 3)
    app.add(pass1_inp, 1, 2, align='center', valign='middle')
    app.add(pass2_inp, 2, 2, align='center', valign='middle')
    app.add(pass3_inp, 3, 2, align='center', valign='middle')
    app.add(login_btn, 4, 2, align='center', valign='middle')

    if pass3_inp.text == '':
        pass
    else:
        pass

    app.run()

def signup(event):
    app = gp.GooeyPieApp('Password Locker')
    app.width = 600
    app.height = 500

    i = 0
    array = []
    while i < 3:
        lines = open("Password-locker/gooeypie/words.txt").readlines() 
        myword = random.choice(lines)
        myword = str(myword)
        array.append(myword)
        i += 1
    passgen_btn = gp.Button(app, 'Generate password', signup)
    passgen_lbl = gp.Label(app, '')
    array = (array[0] + array[1] + array[2])
    
    passgen_lbl.fontsize = 20
    passgen_lbl.align = 'center'
    passgen_lbl = str('Your primary keys are:') + (array)
    menu_btn = gp.Button(app, 'Menu', menu)
    app.set_grid(3, 3)
    app.add(menu_btn, 3, 2, align='center', valign='middle')
    app.add(passgen_btn, 1, 2, align='center', valign='middle')
    app.add(passgen_lbl, 2, 2, align='center', valign='middle')
   
    app.run()
    
login_btn = gp.Button(app, 'Login', login)
signup_btn = gp.Button(app, 'Signup', signup)

app.set_grid(2, 1)
app.add(login_btn, 1, 1, align='center', valign='middle')
app.add(signup_btn, 2, 1, align='center', valign='middle')

app.run()