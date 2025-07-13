from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        # Placeholder logic – we'll validate via MongoDB next
        if email and password:
            return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/post-task", methods=["GET", "POST"])
def post_task():
    if request.method == "POST":
        # Placeholder for MongoDB task saving
        title = request.form["title"]
        category = request.form["category"]
        location = request.form["location"]
        budget = request.form["budget"]
        description = request.form["description"]
        print("Received task:", title, category, location, budget, description)
        return "Task submitted successfully!"
    return render_template("post_task.html")

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/tasks")
def tasks():
    return render_template("tasks.html")
