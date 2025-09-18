from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Definer parameter 'name' som overføres til template
    name = request.args.get("name", "jens") 
    return render_template("index.html", name=name, title="Simple Flask Server")

# Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
