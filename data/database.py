import sqlite3

try: 
    with sqlite3.connect("blackjack") as conn:
        pass
except sqlite3.OperationalError as e:
    print("Failed connecting to the database", e)