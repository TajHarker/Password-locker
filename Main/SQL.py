import sqlite3 
import os

path = os.path.dirname(os.path.abspath(__file__)) 
DBpath = os.path.join(path, 'Primary_database.db') #Connects to primary_database

def signup(key_array): #signup function that takes the array of 5 letter words
    conn = sqlite3.connect(DBpath) #Sets path of the database
    cursor = conn.cursor() #connects to sqllite
    cursor.execute('INSERT INTO Primary_Keys (Key_1, Key_2, Key_3) VALUES (?, ?, ?)', (key_array[0], key_array[1], key_array[2]))
    #Inserts the primary keys into the primary_keys database
    conn.commit() #commits the action
    cursor.close() #Disconnects from sqllite

def login(entry_1, entry_2, entry_3): #Takes the primary key inputs from the user and checks to see if they are valid
    connect = sqlite3.connect(DBpath)
    cursor = connect.cursor() 
    cursor.execute('SELECT Key_1, Key_2, Key_3 from Primary_Keys') #Takes the primary keys from the primary keys table
    Primary_Keys = cursor.fetchall() 
    cursor.close()

    fix_keys = [] #empty array
    i = 0
    while i < len(Primary_Keys): #Runs for every value in the primary keys database
        j = 0
        removekeys_clean = [] 
        while j < 3: #Makes sure that the keys can be read by being in the same array
            removekeys = Primary_Keys[i][j]
            removekeys_clean.append(removekeys)
            j = j + 1
        fix_keys.append(removekeys_clean)
    
        i = i + 1
    PrimaryKeyFound = False
    i = 0
    while PrimaryKeyFound == False and i < len(Primary_Keys): #Checks if the keys the user entered are the same as the ones stored in the database
        if (fix_keys[i][0].lower() == entry_1.lower() and fix_keys[i][1].lower() == entry_2.lower() and fix_keys[i][2].lower() == entry_3.lower()):
            PrimaryKeyFound = True
        i = i + 1  

    return PrimaryKeyFound

def encode(userID, password, randpassword):
    conn = sqlite3.connect(DBpath)
    cursor = conn.cursor() 

    cursor.execute('INSERT INTO EncDec (UserID, Encoded_Password, Decoded_Password) VALUES (?,?, ?)', (userID, randpassword, password))
    conn.commit()
    cursor.close()
    return(randpassword)

def passcheck(encpassword):
    connect = sqlite3.connect(DBpath)
    cursor = connect.cursor() 
    cursor.execute('SELECT Encoded_Password, Decoded_Password from EncDec')
    EncDec = cursor.fetchall()
    cursor.close()

    PassFound = False
    i = 0
    while PassFound == False and i < len(EncDec):
        if (EncDec[i][1].lower() == encpassword.lower()):
            PassFound = True
        i = i + 1  
    return PassFound

def randpassdisplay(UserID):
    connect = sqlite3.connect(DBpath)
    cursor = connect.cursor() 
    cursor.execute(('SELECT Encoded_Password FROM EncDec WHERE UserID = "{a}"').format(a = UserID))
    passdb = cursor.fetchall()
    cursor.close() 
    print(UserID)
    return passdb

def retrieve_userID(password1 , password2, password3):
    connect = sqlite3.connect(DBpath)
    cursor = connect.cursor()
    cursor.execute(('SELECT UserID FROM Primary_Keys WHERE Key_1 = "{a}" AND Key_2 = "{b}" AND Key_3 = "{c}"').format(a = password1, b = password2, c = password3))
    userID = cursor.fetchall()
    cursor.close()
    return(userID[0][0])

def decode(userID, encpassword):
    connect = sqlite3.connect(DBpath)
    cursor = connect.cursor() 
    cursor.execute(('SELECT Decoded_Password FROM EncDec WHERE UserID = {a} AND Encoded_Password = "{b}"').format(a = userID, b = encpassword))
    passdb = cursor.fetchall()
    cursor.close() 
    return passdb[0][0]








