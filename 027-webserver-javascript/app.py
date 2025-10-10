from flask import Flask, request, render_template, g
import sqlite3
from flask import current_app

# Import Flask and other necessary modules
app = Flask(__name__)
DB_USERS = "./db/users.db"

def get_db_albums():
    if "db" not in g:
        g.db = sqlite3.connect(DB_USERS)
        g.db.row_factory = sqlite3.Row  # optional, for dict-like rows
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

# Define the frontpage route for the application
@app.route("/")
def home_page():
    # count = None
    # count = count + 1 if count is not None else 0
    # print(count)
    current_app.logger.info("frontpage loaded")
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
    db = get_db_albums()
    # Perform a search in the database with the LIKE operator
    cur = db.execute("SELECT uname, password FROM user WHERE uname LIKE ?", ('%' + search_term + '%',))
    data = cur.fetchall()
    members = {"members": [dict(u) for u in data]}
    return render_template("search.html", title="Search Results", members=members)

# Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
