import sqlite3
import sys
from pathlib import Path

# Gem databasen i samme mappe som scriptet
BASE_DIR = Path(__file__).resolve().parent
# Modify database name
DB_PATH = BASE_DIR / "beatles.db"

# Modify table field names and datatypes
SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS Beatles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    album TEXT NOT NULL,
    year INTEGER CHECK(year >= 0),
    favorite mycolumn NOT NULL CHECK (favorite IN (0, 1))
);
"""

# Modify data for own use
SEED_ROWS = [
    (1, "With the Beatles",1963, 0),
    (2, "Please Please Me",1963, 0),
    (3, "Beatles for Sale",1964, 0),
    (4, "A Hard Day's Night",1964, 0),
    (5, "Help!",1965, 0),
    (6, "Rubber Soul",1965, 0),
    (7, "Revolver",1966, 0),
    (8, "Magical Mystery Tour",1967, 0),
    (9, "Sgt. Pepper's Lonely Hearts Club Band",1967, 0),
    (10, "The Beatles",1968, 0),
    (11, "Abbey Road",1969, 0),
    (12, "Yellow Submarine",1969, 0),
    (13, "Let It Be",1970, 0),
    (14, "Past Masters",1970, 0)
]

# Modify function as described
def init_db(db_path: Path = DB_PATH, reset: bool = False):
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        if reset:
            conn.execute("DROP TABLE IF EXISTS Beatles;") # Modify table name
        conn.executescript(SCHEMA_SQL)
        # Modify number and names of fields in INSERT query
        conn.executemany(
            "INSERT OR IGNORE INTO Beatles (id, album, year, favorite) VALUES (?, ?, ?, ?);",
            SEED_ROWS,
        )
        conn.commit()

if __name__ == "__main__":
    reset_flag = "--reset" in sys.argv
    init_db(reset=reset_flag)
    print(f"Beatles db oprettet: {DB_PATH} (reset={reset_flag})")