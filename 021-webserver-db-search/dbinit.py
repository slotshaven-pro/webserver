# dbinit.py
import sqlite3
import sys
import csv
from pathlib import Path

# Save db in current folder
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db/beatles.db"
CSV_PATH = BASE_DIR / "db/dbdata.csv"
TABLE_NAME = 'album'

SCHEMA_SQL = f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    aid INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    pubyear TEXT NOT NULL
);
"""

def read_seed_rows_from_csv(csv_path: Path = CSV_PATH) -> list:
    seed_rows = []
    with open(csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            seed_rows.append((
                int(row['aid']),
                row['title'],
                int(row['pubyear'])
            ))
    return seed_rows

# Read seed rows from CSV


def init_db(rows, db_path: Path = DB_PATH, reset: bool = False):
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        if reset:
          conn.execute(f"DROP TABLE IF EXISTS {TABLE_NAME};")
        conn.executescript(SCHEMA_SQL)
        conn.executemany(
            f"INSERT OR IGNORE INTO {TABLE_NAME} (aid, title, pubyear) VALUES (?, ?, ?);",
            rows,
        )
        conn.commit()
        conn.close

def test_db(db_path: Path = DB_PATH):
    with sqlite3.connect(db_path) as conn:
        cur = conn.execute(f"SELECT title, pubyear FROM {TABLE_NAME};")
        data = cur.fetchall()
        # print(data)
        items = {'rows': [{'title': row[0], 'pubyear': row[1]} for row in data]}
        print(items)
    

if __name__ == "__main__":
    reset_flag = "--reset" in sys.argv
    rows = read_seed_rows_from_csv()
    print(rows)
    init_db(rows, reset=reset_flag)
    # print(f"Database initialiseret: {DB_PATH} (reset={reset_flag})")
    # test_db()
