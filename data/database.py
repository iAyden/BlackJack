import sqlite3

try: 
    with sqlite3.connect("blackjackdb.db") as conn:
        print("exito")
        pass
except sqlite3.OperationalError as e:
    print("Failed connecting to the database", e)