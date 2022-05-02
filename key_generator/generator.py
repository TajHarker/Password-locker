import random

def menu():
    login = True
    while login == True:
        pass

def primary_generator():
    i = 0
    while i < 3:
        lines = open("Password_locker/key_generator/words.txt").readlines() 
        myword = random.choice(lines)
        print(myword)
        i += 1

primary_generator()
