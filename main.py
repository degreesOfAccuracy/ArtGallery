import tkinter as tk
import database.interface as db
from library.widgets import Table

GRID_WIDTH = 7

# start a tkinter window
root = tk.Tk()
root.minsize(800, 600)
root.title("Oscar's Art Gallery Challenge")

# configure each column to have equal weights
for x in range(GRID_WIDTH):
    root.columnconfigure(x, weight = 1)

# configure each row with weights
root.rowconfigure(0, weight = 2)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 10)

# create title at top of window
title = tk.Label(root,
    text = "ArtDB",
    font = ("SF Pro", 32, "bold")
)
title.grid(row = 0, column = 0, columnspan = GRID_WIDTH)

# create controls for the table display
#
# dropdown to select artists or artworks
selected_table = tk.StringVar()
selected_table.set("Select a table")
table_dropdown = tk.OptionMenu(root, selected_table, *["Artists", "Artworks"])
table_dropdown.grid(row = 1, column = 0)
#
# refresh button to load the table from the database
def refresh():
    if selected_table.get() == "Artists":
        artworks_table.erase()
        artists_table.populate(db.read_artists())
        artists_table.draw()
    elif selected_table.get() == "Artworks":
        artists_table.erase()
        artworks_table.populate(db.read_artworks())
        artworks_table.draw()
refresh_button = tk.Button(root, text = "Refresh", command = refresh)
refresh_button.grid(row = 1, column = 1)
#
# entry and label for scroll amount
scroll_amount_label = tk.Label(root, text = "Scroll amount")
scroll_amount_label.grid(row = 1, column = 2, sticky = "e")
scroll_amount_entry = tk.Entry(root, width = 2)
scroll_amount_entry.grid(row = 1, column = 3, sticky = "w")
#
# buttons for scroll up and scroll down
def scroll_up():
    try:
        amount = int(scroll_amount_entry.get())
    except ValueError:
        amount = 1
    if selected_table.get() == "Artists":
        artists_table.scroll_up(amount)
    elif selected_table.get() == "Artworks":
        artworks_table.scroll_up(amount)
def scroll_down():
    try:
        amount = int(scroll_amount_entry.get())
    except ValueError:
        amount = 1
    if selected_table.get() == "Artists":
        artists_table.scroll_down(amount)
    elif selected_table.get() == "Artworks":
        artworks_table.scroll_down(amount)
scroll_up_button = tk.Button(root, text = "Scroll Up", command = scroll_up)
scroll_up_button.grid(row = 1, column = 4)
scroll_down_button = tk.Button(root, text = "Scroll Down", command = scroll_down)
scroll_down_button.grid(row = 1, column = 5)

# create a button to open a write window
def write():
    # toplevel widget opens a new window
    top = tk.Toplevel()
    top.minsize(300, 300)
    top.title("Write to Database")

    # configure the 2 columns and title row
    top.columnconfigure(0, weight = 1)
    top.columnconfigure(1, weight = 3)
    top.rowconfigure(0, weight = 2)

    if selected_table.get() == "Artists":
        # configure the remaining rows
        for x in range(1, 7):
            top.rowconfigure(x, weight = 1)

        # add a title
        title = tk.Label(
            top,
            text = "Add an artist to the database",
            font = ("SF Pro", 16, "bold")
        )
        title.grid(row = 0, column = 0, columnspan = 2)

        # add labels down the left
        name_label = tk.Label(top, text = "Name")
        name_label.grid(row = 1, column = 0, sticky = "e")
        street_label = tk.Label(top, text = "Street")
        street_label.grid(row = 2, column = 0, sticky = "e")
        town_label = tk.Label(top, text = "Town")
        town_label.grid(row = 3, column = 0, sticky = "e")
        county_label = tk.Label(top, text = "County")
        county_label.grid(row = 4, column = 0, sticky = "e")
        postcode_label = tk.Label(top, text = "Postcode")
        postcode_label.grid(row = 5, column = 0, sticky = "e")

        # add entries down the right
        name_entry = tk.Entry(top)
        name_entry.grid(row = 1, column = 1, sticky = "ew")
        street_entry = tk.Entry(top)
        street_entry.grid(row = 2, column = 1, sticky = "ew")
        town_entry = tk.Entry(top)
        town_entry.grid(row = 3, column = 1, sticky = "ew")
        county_entry = tk.Entry(top)
        county_entry.grid(row = 4, column = 1, sticky = "ew")
        postcode_entry = tk.Entry(top)
        postcode_entry.grid(row = 5, column = 1, sticky = "ew")

        # add submit button
        def submit():
            db.write_artist(
                name_entry.get(),
                street_entry.get(),
                town_entry.get(),
                county_entry.get(),
                postcode_entry.get()
            )
            top.destroy()
        submit_button = tk.Button(top, text = "Submit", command = submit)
        submit_button.grid(row = 6, column = 0, columnspan = 2)

    elif selected_table.get() == "Artworks":
        # configure the remaining rows
        for x in range(1, 6):
            top.rowconfigure(x, weight = 1)
        
        # add a title
        title = tk.Label(
            top,
            text = "Add an artwork to the database",
            font = ("SF Pro", 16, "bold")
        )
        title.grid(row = 0, column = 0, columnspan = 2)

        # add labels down the left
        id_label = tk.Label(top, text = "Artist ID")
        id_label.grid(row = 1, column = 0, sticky = "e")
        title_label = tk.Label(top, text = "Title")
        title_label.grid(row = 2, column = 0, sticky = "e")
        medium_label = tk.Label(top, text = "Medium")
        medium_label.grid(row = 3, column = 0, sticky = "e")
        price_label = tk.Label(top, text = "Price")
        price_label.grid(row = 4, column = 0, sticky = "e")

        # add entries down the right
        id_entry = tk.Entry(top)
        id_entry.grid(row = 1, column = 1, sticky = "ew")
        title_entry = tk.Entry(top)
        title_entry.grid(row = 2, column = 1, sticky = "ew")
        medium_entry = tk.Entry(top)
        medium_entry.grid(row = 3, column = 1, sticky = "ew")
        price_entry = tk.Entry(top)
        price_entry.grid(row = 4, column = 1, sticky = "ew")

        # add a submit button
        def submit():
            db.write_artwork(
                int(id_entry.get()),
                title_entry.get(),
                medium_entry.get(),
                float(price_entry.get())
            )
            top.destroy()
        submit_button = tk.Button(top, text = "Submit", command = submit)
        submit_button.grid(row = 5, column = 0, columnspan = 2)

    else:
        top.destroy()
    top.mainloop()
write_button = tk.Button(root, text = "Write to DB", command = write)
write_button.grid(row = 1, column = 6)

# create a frame for the table
table_frame = tk.Frame(root)
table_frame.grid(row = 2, column = 0, columnspan = GRID_WIDTH, sticky = "nsew")
# configure the columns in the frame
for x in range(16):
    table_frame.columnconfigure(x, weight = 1)
for x in range(10):
    table_frame.rowconfigure(x, weight = 1)

# create table object for each table
artists_table = Table(
    table_frame,
    ["ID", "Name", "Street", "Town", "County", "Postcode"],
    [1,3,3,3,3,3],
    10,
    0,
    0
)
artworks_table = Table(
    table_frame,
    ["ID", "Artist", "Title", "Medium", "Price"],
    [1,4,4,4,3],
    10,
    0,
    0
)

root.mainloop()