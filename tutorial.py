from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "test"
app.permanent_session_lifetime = timedelta(minutes = 1)

@app.route("/")
def index():
    # return "<p>Hello WOrld</p>"
    return render_template("index.html", content = ['ricky', 'rhea', 'wifey'])

@app.route("/home")
def home():
    # return "<p>Hello WOrld</p>"
    return render_template("home.html")

@app.route("/admin/")
def admin():
    return redirect(url_for("user",name="Admin!"))

@app.route("/login/", methods=["GET","POST"])
def login():
    if(request.method == "POST"):
        session.permanent = True
        user = request.form["name"]
        session['user'] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/user")
def user():
        if "user" in session:
            user = session['user']
            return f"Hello {user}!"
        else:
           return redirect(url_for("login"))
    
    # return render_template("index.html", content=name, r=2)


if __name__ == "__main__":
    app.run(debug=True)