import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db" / "users.db"

SCHEMA_SQL = """
DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    uid   serial      primary key,
    uname varchar(32) unique not null,
    password varchar(32)  not null
);
"""

SEED_ROWS = [
    (1, "mkm1", "welcome"),
    (2, "mkm2", "welcome"),
    (3, "mkm3", "welcome"),
    (4, "mkm4", "welcome"),
    (5, "mkm5", "welcome"),
]

def init_db(db_path: Path = DB_PATH) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as conn:
        conn.executescript(SCHEMA_SQL)
        conn.executemany(
            "INSERT INTO users (uid, uname, password) VALUES (?, ?, ?);",
            SEED_ROWS,
        )
        conn.commit()


if __name__ == "__main__":
    init_db()
    print(f"Database oprettet: {DB_PATH}")
