from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/homepage")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)