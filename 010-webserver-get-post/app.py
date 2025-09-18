from flask import Flask, request, render_template

# Import Flask and other necessary modules
app = Flask(__name__)

# Define the main route for the application
@app.route("/")
def front_page():
    return render_template("index.html", title="Welcome")


# Define routes for GET
@app.route("/get-page")
def get_page():
    get_input = request.args.get("get_input", "10")
    calculated_fib = fibonacci_number(int(get_input))
    return render_template("http-get.html", get_input=get_input, calculated_fib=calculated_fib)

# Define the route for POST requests
@app.route("/post-page", methods=["GET", "POST"])
def post_page():
  if request.method == "POST":
    post_input = request.form.get("post_input", "10")
  else:
    # Default value for GET request
    post_input = "10"
  calculated_fib = fibonacci_number(int(post_input))
  return render_template("http-post.html", post_param=post_input, calculated_fib=calculated_fib)

# Function to calculate Fibonacci number2
def fibonacci_number(n):
    if n <= 0:
      return 0
    elif n == 1:
      return 1
    else:
      a, b = 0, 1
      for _ in range(2, n + 1):
        a, b = b, a + b
      return b

# Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
