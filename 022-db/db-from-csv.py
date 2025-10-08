import sqlite3
import csv
from pathlib import Path

# Save db in current folder
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "artworks.db"
CSV_PATH = BASE_DIR / "csv/artworks.csv"
TABLE_NAME = 'art'

SCHEMA_SQL = f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist   TEXT NOT NULL,
    painting TEXT NOT NULL,
    year     INTEGER CHECK(year >= 0),
    genre    TEXT,
    image    TEXT,
    UNIQUE(artist, painting)
);
"""

def read_seed_rows_from_csv(csv_path: Path = CSV_PATH) -> list:
    seed_rows = []
    with open(csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            seed_rows.append((
                row['artist'],
                row['painting'],
                int(row['year']),
                row['genre'],
                row['image']
            ))
    return seed_rows

# Read seed rows from CSV
def init_db(rows, db_path: Path = DB_PATH):
    with sqlite3.connect(db_path) as conn:
        conn.execute(f"DROP TABLE IF EXISTS {TABLE_NAME};")
        conn.executescript(SCHEMA_SQL)
        conn.executemany(
            f"INSERT OR IGNORE INTO {TABLE_NAME} (artist, painting, year, genre, image) VALUES (?, ?, ?, ?, ?);",
            rows,
        )
        conn.commit()
        conn.close

# Test function that prints first row in database.
def test_db():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(f"SELECT painting, artist FROM {TABLE_NAME};")
        data = cur.fetchall()
        items = {'rows': [{'painting': row[0], 'artist': row[1]} for row in data]}
        print(items)

if __name__ == "__main__":
    rows = read_seed_rows_from_csv()
    init_db(rows)
    print(f"Database oprettet: {DB_PATH}")
    # test_db()