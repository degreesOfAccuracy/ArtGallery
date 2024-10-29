import sqlite3

DATABASE_PATH = "database/database.db"

def execute_script(script_path):
    "Executes a script of SQL commands"
    with open(script_path) as script_file:
        script = script_file.read()
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.executescript(script)
    con.commit()

def write_artist(artist_name: str, street: str, town: str, county: str, postcode: str):
    "Adds an artist to the artists table"
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO artists (artist_name, street, town, county, postcode) VALUES (?, ?, ?, ?, ?)",
        (artist_name, street, town, county, postcode)
    )
    con.commit()

def read_artists(cols = "id, artist_name, street, town, county, postcode"):
    "Reads the specified columns from all the rows in the artists table"
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(f"SELECT {cols} FROM artists")
    return cur.fetchall()

def write_artwork(artist_id: int, title: str, medium: str, price: float):
    "Adds an artwork to the artwork table"
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO artworks (artist_id, title, medium, price) VALUES (?, ?, ?, ?)",
        (artist_id, title, medium, price)
    )
    con.commit()

def read_artworks(cols = "artist_id, title, medium, price"):
    "Reads the specified columns from all the rows in the artworks table"
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(f"SELECT {cols} FROM artworks")
    artworks = [list(tup) for tup in cur.fetchall()]
    # get the artist names, then add them ids to the row at index 1
    cur.execute("SELECT id, artist_name FROM artists")
    artist_names = dict(cur.fetchall())
    for i in range(len(artworks)):
        artist_id = artworks[i][0]
        artworks[i] = [artworks[i][0]] + [artist_names[artist_id]] + artworks[i][1:]
    return artworks
