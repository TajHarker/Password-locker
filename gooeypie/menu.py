import gooeypie as gp
import login

def login(event):
    login_lbl.text = 'Hello Gooey Pie!'

    #login

def signup(event):
    signup_lbl.text = 'Hello Gooey Pie!'

app = gp.GooeyPieApp('Password Locker')
app.width = 600
app.height = 500

login_btn = gp.Button(app, 'Login', login)
signup_lbl = gp.Label(app, '')

signup_btn = gp.Button(app, 'Signup', signup)
login_lbl = gp.Label(app, '')

app.set_grid(2, 1)
app.add(login_btn, 1, 1, align='center', valign='middle')
app.add(signup_lbl, 2, 1, align='center', valign='middle')

app.set_grid(2, 1)
app.add(signup_btn, 1, 1, align='center', valign='bottom')
app.add(login_lbl, 2, 1, align='center', valign='middle')

app.run()