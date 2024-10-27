import tkinter as tk
import database as db

# start a tkinter window
root = tk.Tk()
root.minsize(800, 600)

# configure rows and columns
for row_n in range(20):
    root.rowconfigure(row_n, weight = 1)
for col_n in range(15):
    root.columnconfigure(col_n, weight = 1)

title = tk.Label(root, text = "ArtDB", font = ("Calibri", 24), justify = "center")
title.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 20)

root.mainloop()

db.write_artist("Martin Leighton", "5 Park Place", "Peterborough", "Cambridgeshire", "PE32 5LP")
db.write_artwork(1, "African Giant", "Oil", 800)