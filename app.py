from flask import Flask, render_template, request, redirect, url_for, flash, g
import sqlite3

DATABASE = 'database.db'

app = Flask(__name__)
app.secret_key = 'many random bytes'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route("/")
def index():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template("index.html", users=users)

@app.route("/insert", methods=["POST"])
def insert():
    if request.method == "POST":
        flash("Record was successfully added!")
        name = request.form["name"]
        id = request.form["id"]
        points = request.form["points"]
        cur = get_db().cursor()
        cur.execute(f"INSERT INTO users (name, id, points) VALUES ('{name}', {id}, {points})")
        get_db().commit()
        cur.close()
        return redirect(url_for("index"))
    
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search = request.form["search"]
        cur = get_db().cursor()
        cur.execute(f"SELECT * FROM users WHERE name LIKE '%{search}%'")
        users = cur.fetchall()
        cur.close()
        return render_template("index.html", users=users)
    
@app.route("/delete/<string:id_data>", methods=["GET"])
def delete(id_data):
    flash("Record was successfully deleted!")
    cur = get_db().cursor()
    cur.execute(f"DELETE FROM users WHERE id={id_data}")
    get_db().commit()
    cur.close()
    return redirect(url_for("index"))

@app.route("/update", methods=["GET", "POST"])
def update():
    flash("Record was successfully updated!")
    if request.method == "POST":
        id = request.form["id"]
        new_name = request.form["name"]
        new_points = request.form["points"]
        cur = get_db().cursor()
        cur.execute(f"UPDATE users SET name='{new_name}', points={new_points} WHERE id={id}")
        get_db().commit()
        cur.close()
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

