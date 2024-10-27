CREATE TABLE artists (
    id INTEGER PRIMARY KEY NOT NULL,
    artist_name TEXT UNIQUE NOT NULL,
    street TEXT NOT NULL,
    town TEXT NOT NULL,
    county TEXT NOT NULL,
    postcode text NOT NULL
);

CREATE TABLE artworks (
    id INTEGER PRIMARY KEY NOT NULL,
    artist_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    medium TEXT NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
);