import gooeypie as gp

def generate_password(event):
    passgen_lbl.text = 'house, apple, thorn'
    
app = gp.GooeyPieApp('Password Locker')
app.width = 600
app.height = 500

passgen_btn = gp.Button(app, 'Generate password' , generate_password)
passgen_lbl = gp.Label(app, '')

app.set_grid(2, 1)
app.add(passgen_btn, 1, 1, align='center', valign='bottom')
app.add(passgen_lbl, 2, 1, align='center', valign='middle')

app.run()
