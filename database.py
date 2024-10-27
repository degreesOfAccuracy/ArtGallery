import sqlite3

DATABASE_PATH = "database.db"

def write_artist(artist_name: str, street: str, town: str, county: str, postcode: str):
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO artists (artist_name, street, town, county, postcode) VALUES (?, ?, ?, ?, ?)",
        (artist_name, street, town, county, postcode)
    )
    con.commit()

def write_artwork(artist_id: int, title: str, medium: str, price: float):
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO artworks (artist_id, title, medium, price) VALUES (?, ?, ?, ?)",
        (artist_id, title, medium, price)
    )
    con.commit()
