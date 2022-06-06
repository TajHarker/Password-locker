import gooeypie as gp


def login(event):
    if pass3_inp.text == 'bestpassword':
        status_lbl.text = 'Access granted!'
    else:
        status_lbl.text = 'Access denied!'

app = gp.GooeyPieApp('Password Locker')
app.width = 600
app.height = 500

pass1_lbl = gp.Label(app, "")
pass1_inp = gp.Secret(app)
pass2_lbl = gp.Label(app, "")
pass2_inp = gp.Secret(app)
pass3_lbl = gp.Label(app, "")
pass3_inp = gp.Secret(app)
login_btn = gp.Button(app, 'Login', login)
status_lbl = gp.Label(app, '')

app.set_grid(3, 4)
app.add(pass1_lbl, 1, 2)
app.add(pass1_inp, 1, 3)
app.add(pass2_lbl, 1, 4)
app.add(pass2_inp, 2, 2)
app.add(pass3_lbl, 2, 3)
app.add(pass3_inp, 2, 4)
app.add(login_btn, 3, 3)
app.add(status_lbl, 3, 4)

# pass1_lbl.margin_top = 400
# pass1_lbl.margin_right = 20
# pass1_lbl.margin_bottom = 20
# pass1_lbl.margin_left = 'auto'

# pass2_lbl.margin_top = 40
# pass2_lbl.margin_right = 20
# pass2_lbl.margin_bottom = 20
# pass2_lbl.margin_left = 'auto'

# pass3_lbl.margin_top = 40
# pass3_lbl.margin_right = 20
# pass3_lbl.margin_bottom = 20
# pass3_lbl.margin_left = 'auto'

app.run()


