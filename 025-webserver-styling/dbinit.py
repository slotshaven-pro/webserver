# dbinit.py
import sqlite3
import sys
from pathlib import Path

# Gem databasen i samme mappe som scriptet
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "artworks.db"

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS artworks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist   TEXT NOT NULL,
    painting TEXT NOT NULL,
    year     INTEGER CHECK(year >= 0),
    genre    TEXT,
    UNIQUE(artist, painting)
);
"""

SEED_ROWS = [
    ("Pablo Picasso",  "Les Demoiselles d'Avignon", 1907, "Cubism"),
    ("Jackson Pollock","No. 5, 1948",               1948, "Abstract Expressionism"),
    ("Henri Matisse",  "Woman with a Hat",          1905, "Fauvism"),
]

def init_db(db_path: Path = DB_PATH, reset: bool = False):
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        if reset:
            conn.execute("DROP TABLE IF EXISTS artworks;")
        conn.executescript(SCHEMA_SQL)
        conn.executemany(
            "INSERT OR IGNORE INTO artworks (artist, painting, year, genre) VALUES (?, ?, ?, ?);",
            SEED_ROWS,
        )
        conn.commit()

if __name__ == "__main__":
    reset_flag = "--reset" in sys.argv
    init_db(reset=reset_flag)
    print(f"Database initialiseret: {DB_PATH} (reset={reset_flag})")