import tkinter
from GUI import gui
import sqlite3


# root = tkinter.Tk()
# gui.init_gui(root)
# root.mainloop()

with sqlite3.connect('../TestScores.db') as db:
    cursor = db.cursor()

cursor.execute("""SELECT *
                FROM scores""")

for r in cursor.fetchall():
    print(r)