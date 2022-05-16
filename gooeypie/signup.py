import gooeypie as gp
import random

def generate_password(event):
    i = 0
    array = []
    while i < 3:
        lines = open("Password-locker/gooeypie/words.txt").readlines() 
        myword = random.choice(lines)
        myword = str(myword)
        array.append(myword)
        i += 1
    passgen_lbl.text = print('Your three passwords are') + array[0] + array[1] + array[2]
    
app = gp.GooeyPieApp('Password Locker')
app.width = 600
app.height = 500

passgen_btn = gp.Button(app, 'Generate password' , generate_password)
passgen_lbl = gp.Label(app, '')

app.set_grid(2, 1)
app.add(passgen_btn, 1, 1, align='center', valign='bottom')
app.add(passgen_lbl, 2, 1, align='center', valign='middle')

app.run()
