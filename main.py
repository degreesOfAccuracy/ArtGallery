import tkinter as tk
import database.interface as db

class Table():
    def __init__(self, root, headers: list[str], col_spans: list[int], height: int, row_start: int, col_start: int):
        self.root = root
        self.headers = headers
        self.col_spans = col_spans
        self.width = len(headers)
        self.height = height
        self.scrolled_rows = 0
        self.rows = []
        self.row_start = row_start
        self.col_start = col_start

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

    def draw(self):
        "Creates the needed tkinter labels, then adds them to the root using the grid manager"
        # create the header labels
        header_labels = []
        for header in self.headers:
            header_labels.append(tk.Label(self.root,
                text = header,
                font = ("Calibri", 20, "bold"),
                bg = "white",
                fg = "black"
            ))
        # create the labels for the data in each row
        rows_labels = []
        for i, row in enumerate(self.rows[self.scrolled_rows:self.scrolled_rows + self.height]):
            cells_labels = []
            background = "#eeeeee" if i % 2 == 0 else "#dddddd"
            for cell in row:
                cells_labels.append(tk.Label(self.root,
                    text = cell,
                    font = ("Calibri", 15),
                    bg = background,
                    fg = "black"
                ))
            rows_labels.append(cells_labels)
        # grid the headers
        cursor_col = self.col_start
        for i, header in enumerate(header_labels):
            header.grid(
                row = self.row_start,
                column = cursor_col,
                columnspan = self.col_spans[i],
                sticky = "nsew"
            )
            cursor_col += self.col_spans[i]
        # grid the cells
        for i, row in enumerate(rows_labels):
            cursor_col = self.col_start
            for j, cell in enumerate(row):
                cell.grid(
                    row = self.row_start + i + 1,
                    column = cursor_col,
                    columnspan = self.col_spans[j],
                    sticky = "nsew"
                )
                cursor_col += self.col_spans[j]
    
    # functions to scroll through the table
    def scroll_up(self):
        if self.scrolled_rows >= self.height:
            self.scrolled_rows -= self.height
            self.draw()
    def scroll_down(self):
        if self.scrolled_rows <= len(self.rows) - self.height:
            self.scrolled_rows += self.height
            self.draw()

# start a tkinter window
root = tk.Tk()
root.config(bg = "white")
root.minsize(800, 600)
root.title("Oscar's Art Gallery Challenge")

# configure rows and columns
for row_n in range(50):
    root.rowconfigure(row_n, weight = 1)
for col_n in range(17):
    root.columnconfigure(col_n, weight = 1)

# create title at top of window
title = tk.Label(root,
    text = "ArtDB",
    font = ("Calibri", 24),
    bg = "white",
    fg = "black"
)
title.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 20)

# create table for the artists database
artists_table = Table(root, ["Name", "Street", "Town", "County", "Postcode"], [3,3,3,3,3], 3, 2, 1)
artists_table.populate(db.read_artists())
artists_table.draw()

# create scroll buttons for the artists database
artists_scroll_up = tk.Button(root,
    text = "Scroll Up",
    font = ("Calibri", 15),
    command = artists_table.scroll_up,
    bg = "white",
    fg = "black"
)
artists_scroll_up.grid(row = 1, column = 0)
artists_scroll_down = tk.Button(root,
    text = "Scroll Down",
    font = ("Calibri", 15),
    command = artists_table.scroll_down,
    bg = "white",
    fg = "black"
)
artists_scroll_down.grid(row = 1, column = 1)

root.mainloop()
