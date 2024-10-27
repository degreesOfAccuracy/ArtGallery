import interface as db

db.execute_script("database/drop_tables.sql")
db.execute_script("database/create_tables.sql")

starting_artists = [
    ("Martin Leighton", "5 Park Place", "Peterborough", "Cambridgeshire", "PE32 5LP"),
    ("Eva Czarniecka", "77 Warner Close", "Chelmsford", "Essex", "CM22 5FT"),
    ("Roxy Parkin", "90 Hindhead Road", "", "London", "SE12 6WM"),
    ("Nigel Farnworth", "41 Whitby Road", "Huntly", "Aberdeenshire", "AB54 5PN"),
    ("Teresa Tanner", "70 Guild Street", "", "London", "NW7 1SP")
]

starting_artworks = [
    (5, "Woman with black Labrador", "Oil", 220),
    (5, "Bees & thistles", "Watercolour", 85),
    (2, "A stroll to Westminster", "Ink", 190),
    (1, "African giant", "Oil", 800),
    (3, "Water daemon", "Acrylic", 1700),
    (4, "A seagull", "Watercolour", 35),
    (1, "Three friends", "Oil", 1800),
    (2, "Summer breeze 1", "Acrylic", 1350),
    (4, "Mr Hamster", "Watercolour", 35),
    (1, "Pulput Rock, Dorset", "Oil", 600),
    (5, "Trawler Dungeness Beach", "Oil", 195),
    (2, "Dance in the snow", "Oil", 250),
    (4, "St Tropez port", "Ink", 45),
    (3, "Pirate assassin", "Acrylic", 420),
    (1, "Morning walk", "Oil", 800),
    (4, "A baby barn swallow", "Watercolour", 35),
    (4, "The old working mills", "Ink", 395)
]

for x in starting_artists:
    artist_name = x[0]
    street = x[1]
    town = x[2]
    county = x[3]
    postcode = x[4]
    db.write_artist(artist_name, street, town, county, postcode)

for y in starting_artworks:
    artist_id = y[0]
    title = y[1]
    medium = y[2]
    price = y[3]
    db.write_artwork(artist_id, title, medium, price)