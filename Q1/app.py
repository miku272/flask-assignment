from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    args = request.args

    name = args.get("name", default="")
    roll = args.get("roll", default=0)

    return f"<h1>Welcome {name}! Your roll no. is {roll}.</h1>"

if __name__ == "__main__":
    app.run(debug=True)