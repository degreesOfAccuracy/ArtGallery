import tkinter as tk

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
        self.headers = [] # a list that will contain the labels represeting each header
        for header in headers:
            self.headers.append(tk.Label(self.root,
                text = header,
                font = ("SF Pro", 20, "bold"),
            ))

    def populate(self, rows):
        "Replace the current rows"
        if any([len(row) != self.width for row in rows]):
            raise Exception(f"Row was not the expected width of {self.width}") 
        else:
            self.rows = []
            for i, row in enumerate(rows):
                row_labels = []
                background = "#222222" if i % 2 == 0 else "#333333"
                for cell in row:
                    row_labels.append(tk.Label(self.root,
                        text = cell,
                        font = ("SF Pro", 15),
                        bg = background
                    ))
                self.rows.append(row_labels)

    def draw_headers(self):
        "Uses the grid geometry manager to draw the table headers to the screen"
        self.erase(rows = False)
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
        self.erase(headers = False)
        for i, row in enumerate(self.rows[self.scrolled_rows : self.scrolled_rows + self.height - 1]):
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

    def erase(self, headers = True, rows = True):
        "grid_forgets the specified groups of labels in the table"
        if headers:
            for header in self.headers:
                header.grid_forget()
        if rows:
            for row in self.rows:
                for cell in row:
                    cell.grid_forget()
    
    # functions to scroll through the table
    def scroll_up(self, amount: int):
        "Scrolls up by the specified amount if possible, otherwise the maximum amount"
        if self.scrolled_rows >= amount:
            self.scrolled_rows -= amount
        else:
            self.scrolled_rows = 0
        self.draw_content()
    def scroll_down(self, amount: int):
        "Scrolls down by the specified amount if possible, otherwise the maximum amount"
        if self.scrolled_rows < len(self.rows) - self.height + 1 - amount:
            self.scrolled_rows += amount
        else:
            self.scrolled_rows = max(len(self.rows) - self.height + 1, 0) # make sure scrolled_rows isn't negative
        self.draw_content()