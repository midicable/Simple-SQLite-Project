import tkinter
import sqlite3


def add_record_to_db(_name, _grade, _name_entry, _grade_entry):
    name = _name.get()
    grade = float(_grade.get())
    _name_entry.delete(0, tkinter.END)
    _grade_entry.delete(0, tkinter.END)

    with sqlite3.connect('../TestScores.db') as db:
        cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS scores(
           name TEXT PRIMARY KEY,
           grade TEXT NOT NULL);""")

    cursor.execute("""INSERT INTO scores(name,grade) 
        VALUES(?,?);""", [name, grade])
    db.commit()

    db.close()



def clear_fields(name_entry, grade_entry):
    name_entry.delete(0, tkinter.END)
    grade_entry.delete(0, tkinter.END)