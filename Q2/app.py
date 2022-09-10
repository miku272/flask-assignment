from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/faculty")
def faculty():
    return render_template("faculty.html")

@app.route("/student")
def student():
    return render_template("student.html")

@app.route("/dept")
def dept():
    return render_template("department.html")

if __name__ == "__main__":
    app.run(debug=True)