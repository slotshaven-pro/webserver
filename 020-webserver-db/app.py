from flask import Flask, request, render_template
import sqlite3

# Import Flask and other necessary modules
app = Flask(__name__)
DB_ALBUM = "./db/beatles.db"
DB_USERS = "./db/users.db"


def get_db(db, query):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res


@app.route("/beatles")
def beatles_page():
    data = get_db(DB_ALBUM, "select * from album")
    return render_template("albums.html", title="Welcome", items=data)


# Define the main route for the application
@app.route("/")
def front_page():
    data = get_db(DB_USERS, "select * from users")
    return render_template("index.html", title="Welcome", users=data)


# Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
