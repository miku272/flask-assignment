from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student_bio_data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class StudBio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    mob = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(2000), nullable=False)

    def __repr__(self) -> str:
        return f"{self.id} - {self.fname} - {self.lname} - {self.mob} - {self.addr}"


@app.route("/", methods=["GET", "POST"])
def stud_bio():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        mob = request.form["mob"]
        addr = request.form["addr"]

        bio = StudBio(fname=fname, lname=lname, mob=mob, addr=addr)

        db.session.add(bio)
        db.session.commit()

    allbio = StudBio.query.all()

    # return "<h1>Hello World!</h1>"
    return render_template("index.html", allbio=allbio, length=len(allbio))

@app.route("/delete", methods=["GET"])
def delete():
    id = request.args.get("id")

    bio = StudBio.query.filter_by(id=id).first()

    db.session.delete(bio)
    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
