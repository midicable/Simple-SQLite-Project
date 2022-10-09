import tkinter
from tkinter import ttk
from Logic import logic

def init_gui(root):
    root.title('TestScores')

    mainframe = ttk.Frame(root, padding='25 25 30 40')
    mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    name = tkinter.StringVar()
    name_entry = ttk.Entry(mainframe, width=26, textvariable=name)
    name_entry.grid(column=1, row=0, columnspan=2, sticky=tkinter.W)

    grade = tkinter.StringVar()
    grade_entry = ttk.Entry(mainframe, width=26, textvariable=grade)
    grade_entry.grid(column=1, row=1, columnspan=2, sticky=tkinter.W)

    name_label = ttk.Label(mainframe, text="Enter student's name:")
    name_label.grid(column=0, row=0, sticky=(tkinter.W, tkinter.E))

    score_label = ttk.Label(mainframe, text="Enter student's grade:")
    score_label.grid(column=0, row=1, sticky=(tkinter.W, tkinter.E))

    add_button = ttk.Button(mainframe, text="Add", command=lambda: logic.add_record_to_db(name, grade, name_entry, grade_entry))
    add_button.grid(column=1, row=2, sticky=tkinter.W)

    clear_button = ttk.Button(mainframe, text="Clear", command=lambda: logic.clear_fields(name_entry, grade_entry))
    clear_button.grid(column=2, row=2, sticky=tkinter.W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=10)

    name_entry.focus()