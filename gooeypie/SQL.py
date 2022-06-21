import sqlite3
import os

path = os.path.dirname(os.path.abspath(__file__))
DBpath = os.path.join(path, 'Primary_database.db')

def signup(key_array):  
    conn = sqlite3.connect(DBpath)
    cursor = conn.cursor() 

    cursor.execute('INSERT INTO Primary_Keys (Key_1, Key_2, Key_3) VALUES (?, ?, ?)', (key_array[0], key_array[1], key_array[2]))
    conn.commit()
    cursor.close()

def login(entry_1, entry_2, entry_3):
    connect = sqlite3.connect(DBpath)
    cursor = connect.cursor() 
    cursor.execute('SELECT Key_1, Key_2, Key_3 from Primary_Keys')
    Primary_Keys = cursor.fetchall()
    cursor.close()

    fix_keys = []
    i = 0
    while i < len(Primary_Keys):
        j = 0
        removekeys_clean = []
        while j < 3:
            removekeys = Primary_Keys[i][j].strip("\n")
            removekeys_clean.append(removekeys)
            j = j + 1
        fix_keys.append(removekeys_clean)
    
        i = i + 1
    PrimaryKeyFound = False
    i = 0
    while PrimaryKeyFound == False and i < len(Primary_Keys):
        if (fix_keys[i][0].lower() == entry_1.lower() and fix_keys[i][1].lower() == entry_2.lower() and fix_keys[i][2].lower() == entry_3.lower()):
            PrimaryKeyFound = True
        i = i + 1  

    return PrimaryKeyFound



