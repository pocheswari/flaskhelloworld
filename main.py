from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hellow,Welcome to my page!"

if __name__ == "__main__":
    app.run(debug=True)
