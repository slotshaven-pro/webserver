from flask import Flask, request, render_template
import sqlite3

# Import Flask and other necessary modules
app = Flask(__name__)
DB_ALBUM = "./db/beatles.db"

def get_db(db, query, params=()):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, params)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res

# Define the main route for the application
@app.route("/", methods=["GET", "POST"])
def search_page():
    # POST request: do search
    if request.method == "POST":
        search_term = request.form.get("search_term", "")
        return db_search(search_term)
    # GET request: show search form
    return render_template("search.html", title="Welcome", members=[])

def db_search(search_term):
    # Perform a search in the database with the LIKE operator
    data = get_db(
        DB_ALBUM,
        "SELECT title, pubyear FROM album WHERE title LIKE ?",
        ('%' + search_term + '%',),
    )
    members = {"members": [dict(u) for u in data]}
    return render_template("search.html", title="Search Results", members=members)

# Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
