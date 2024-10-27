import tkinter as tk
import database.interface as db

class Table():
    def __init__(self, root, headers: list[str], col_spans: list[int], height: int, grid_row_start: int, grid_col_start: int):
        self.root = root # the tk canvas to attach widgets onto
        self.col_spans = col_spans # a list containing the column span for each header
        self.width = len(headers) # the number of columns
        self.height = height # the number of rows displayed at once
        self.scrolled_rows = 0 # the index of the first row displayed
        self.grid_row_start = grid_row_start # the grid row at which the table will start at
        self.grid_col_start = grid_col_start # the grid column at which the table will start at
        self.rows = [] # a list that will contain lists of labels representing each row
        self.headers = [] # a list of 
        for header in headers:
            self.headers.append(tk.Label(self.root,
                text = header,
                font = ("Calibri", 20, "bold"),
                bg = "white",
                fg = "black"
            ))

    def populate(self, rows):
        "Replace the current rows"
        if any([len(row) != self.width for row in rows]):
            raise Exception(f"Row was not the expected width of {self.width}") 
        else:
            self.rows = []
            for i, row in enumerate(rows):
                row_labels = []
                background = "#eeeeee" if i % 2 == 0 else "#dddddd"
                for cell in row:
                    row_labels.append(tk.Label(self.root,
                        text = cell,
                        font = ("Calibri", 15),
                        bg = background,
                        fg = "black"
                    ))
                self.rows.append(row_labels)

    def draw_headers(self):
        "Uses the grid geometry manager to draw the table headers to the screen"
        cursor_col = self.grid_col_start
        for i, header in enumerate(self.headers):
            header.grid(
                row = self.grid_row_start,
                column = cursor_col,
                columnspan = self.col_spans[i],
                sticky = "nsew"
            )
            cursor_col += self.col_spans[i]

    def draw_content(self):
        "Uses the grid geometry manager to draw the current range of rows to the screen"
        for row in self.rows:
            for cell in row:
                cell.grid_forget()
        for i, row in enumerate(self.rows[self.scrolled_rows:self.scrolled_rows+self.height]):
            cursor_col = self.grid_col_start
            for j, cell in enumerate(row):
                cell.grid(
                    row = self.grid_row_start + i + 1,
                    column = cursor_col,
                    columnspan = self.col_spans[j],
                    sticky = "nsew"
                )
                cursor_col += self.col_spans[j]
    
    def draw(self):
        "Calls functions draw_content and draw_headers"
        self.draw_headers()
        self.draw_content()
    
    # functions to scroll through the table
    def scroll_up(self):
        if self.scrolled_rows >= self.height:
            self.scrolled_rows -= self.height
            self.draw_content()
    def scroll_down(self):
        if self.scrolled_rows < len(self.rows) - self.height:
            self.scrolled_rows += self.height
            self.draw_content()

# start a tkinter window
root = tk.Tk()
root.config(bg = "white")
root.minsize(800, 600)
root.title("Oscar's Art Gallery Challenge")

# configure rows and columns
for row_n in range(16):
    root.rowconfigure(row_n, weight = 0)
for col_n in range(17):
    root.columnconfigure(col_n, weight = 1)

current_row = 0

# create title at top of window
title = tk.Label(root,
    text = "ArtDB",
    font = ("Calibri", 24),
    bg = "white",
    fg = "black"
)
title.grid(row = current_row, column = 0, sticky = "nsew", columnspan = 17)
current_row += 1

# create subtitle for artists table
artists_subtitle = tk.Label(root,
    text = "Artists",
    font = ("Calibri", 20),
    bg = "white",
    fg = "black"
)
artists_subtitle.grid(row = current_row, column = 1, columnspan = 16, sticky = "nsw")
current_row += 1

# create table for the artists database
artists_table = Table(root, ["Name", "Street", "Town", "County", "Postcode"], [3,3,3,3,3], 5, current_row, 1)

# create scroll buttons for the artists database
artists_scroll_up = tk.Button(root,
    text = "Scroll Up",
    font = ("Calibri", 15),
    command = artists_table.scroll_up,
    bg = "white",
    fg = "black"
)
artists_scroll_up.grid(row = current_row, column = 0, columnspan = 3, sticky = "nsew")
artists_scroll_down = tk.Button(root,
    text = "Scroll Down",
    font = ("Calibri", 15),
    command = artists_table.scroll_down,
    bg = "white",
    fg = "black"
)
artists_scroll_down.grid(row = current_row, column = 3, columnspan = 3, sticky = "nsew")
current_row += 1

# populatea and draw the artists table
artists_table.populate(db.read_artists())
artists_table.draw()
current_row += 6

# create subtitle for artworks database
artworks_subtitle = tk.Label(root,
    text = "Artworks",
    font = ("Calibri", 20),
    bg = "white",
    fg = "black"
)
artworks_subtitle.grid(row = current_row, column = 1, columnspan = 16, sticky = "nsw")
current_row += 1

# create table for the artworks database
artworks_table = Table(root, ["Artist", "Title", "Medium", "Price"], [3,3,3,3], 5, current_row, 1)

# create scroll buttons for the artworks database
artists_scroll_up = tk.Button(root,
    text = "Scroll Up",
    font = ("Calibri", 15),
    command = artworks_table.scroll_up,
    bg = "white",
    fg = "black"
)
artists_scroll_up.grid(row = current_row, column = 0, columnspan = 3, sticky = "nsew")
artists_scroll_down = tk.Button(root,
    text = "Scroll Down",
    font = ("Calibri", 15),
    command = artworks_table.scroll_down,
    bg = "white",
    fg = "black"
)
artists_scroll_down.grid(row = current_row, column = 3, columnspan = 3, sticky = "nsew")
current_row += 1

# populate and draw the artworks table
artworks_table.populate(db.read_artworks())
artworks_table.draw()
current_row += 6

print(current_row)

root.mainloop()