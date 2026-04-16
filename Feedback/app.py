from flask import Flask, render_template, request, redirect, url_for
from repository.feedback_repository import save_feedback

app = Flask(name)

@app.route("/", methods=["GET"])
def feedback_page():
    return render_template("feedback.html")

@app.route("/submit", methods=["POST"])
def submit_feedback():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    save_feedback(name, email, message)
    return redirect(url_for("success_page"))

@app.route("/success")
def success_page():
    return render_template("success.html")

if name == "main":
    app.run(debug=True)