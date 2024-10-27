import tkinter as tk
import database.interface as db

class Table():
    def __init__(self, headers: list[str], height: int):
        self.headers = headers
        self.width = len(headers)
        self.height = height
        self.rows = []

    def populate(self, rows: list[tuple]):
        "Replace the current rows"
        if any([len(row) != self.width for row in rows]):
            raise Exception(f"Row was not the expected width of {self.width}") 
        else:
            self.rows = rows

    def append(self, row: tuple):
        "Add to the end of the current rows"
        if len(row) != self.width:
            raise Exception(f"Row was not the expected width of {self.width}") 
        else:
            self.rows.append(row)
    
    def empty(self):
        "Remove every row"
        self.rows = []

    def pop(self, index = -1):
        "Remove and return the row at a specified index, defaults to -1"
        return self.rows.pop(index)

# start a tkinter window
root = tk.Tk()
root.minsize(800, 600)
root.title("Oscar's Art Gallery Challenge")

# configure rows and columns
for row_n in range(20):
    root.rowconfigure(row_n, weight = 1)
for col_n in range(15):
    root.columnconfigure(col_n, weight = 1)

# create title at top of window
title = tk.Label(root, text = "ArtDB", font = ("Calibri", 24), justify = "center")
title.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 20)

artists_table = Table(["Name", "Street", "Town", "County", "Postcode"], 10)
artists_table.populate(db.read_artists())

root.mainloop()
