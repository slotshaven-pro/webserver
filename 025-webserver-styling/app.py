from flask import Flask, request, render_template
from pathlib import Path
import sqlite3

# Import Flask and other necessary modules
app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
DB_ALBUM = str((BASE_DIR / "db" / "beatles.db").resolve())

def get_db(db, query, params=()):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, params)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res

# Define the frontpage route for the application
@app.route("/")
def home_page():
    return render_template("frontpage.html", title="Welcome", members=[])

# Define the route for the search page
@app.route("/search", methods=["GET", "POST"])
def search_page():
    # POST request: do search
    if request.method == "POST":
        search_term = request.form.get("search_term", "")
        return db_search(search_term)
    # GET request: show search form
    return render_template("search.html", title="Search Page", members=[])

# About page
@app.route("/about")
def about_page():
  return render_template("default.html", title="About")

# Tech Stack
@app.route("/techstack")
def techstack_page():
  return render_template("default.html", title="Tech Stack")

def db_search(search_term):
    # Perform a search in the database with the LIKE operator
    data = get_db(
        DB_ALBUM,
        "SELECT title, yyear FROM album WHERE title LIKE ?",
        ('%' + search_term + '%',),
    )
    members = {"members": [dict(u) for u in data]}
    return render_template("search.html", title="Search Results", members=members)

# Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
