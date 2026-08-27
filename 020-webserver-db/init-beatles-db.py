import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db" / "beatles.db"

SCHEMA_SQL = """
DROP TABLE IF EXISTS album;

CREATE TABLE album
(
    ano   serial      primary key,
    title varchar(99) unique not null,
    yyear int         not null
);
"""

SEED_ROWS = [
    (1, "With the Beatles", 1963),
    (2, "Please Please Me", 1963),
    (3, "Beatles for Sale", 1964),
    (4, "A Hard Day's Night", 1964),
    (5, "Help!", 1965),
    (6, "Rubber Soul", 1965),
    (7, "Revolver", 1966),
    (8, "Magical Mystery Tour", 1967),
    (9, "Sgt. Pepper's Lonely Hearts Club Band", 1967),
    (10, "The Beatles", 1968),
    (11, "Abbey Road", 1969),
    (12, "Yellow Submarine", 1969),
    (13, "Let It Be", 1970),
    (14, "Past Masters", 1970),
]


def init_db(db_path: Path = DB_PATH) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as conn:
        conn.executescript(SCHEMA_SQL)
        conn.executemany(
            "INSERT INTO album (ano, title, yyear) VALUES (?, ?, ?);",
            SEED_ROWS,
        )
        conn.commit()


if __name__ == "__main__":
    init_db()
    print(f"Database oprettet: {DB_PATH}")
