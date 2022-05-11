import gooeypie as gp

def login(event):
    login_lbl.text = 'Hello Gooey Pie!'

def signup(event):
    signup_lbl.text = 'Hello Gooey Pie!'

app = gp.GooeyPieApp('Password Locker')
app.width = 600
app.height = 500

login_btn = gp.Button(app, 'Login', login)
login_lbl = gp.Label(app, '')

signup_btn = gp.Button(app, 'Signup', signup)
signup_lbl = gp.Label(app, '')

app.set_grid(2, 1)
app.add(login_btn, 1, 1, align='center', valign='middle')
app.add(login_lbl, 2, 1, align='center', valign='bottom')

app.set_grid(2, 1)
app.add(signup_btn, 1, 1, align='center', valign='bottom')
app.add(signup_lbl, 2, 1, align='center', valign='middle')

app.run()