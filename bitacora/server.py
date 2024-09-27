
from flask import Flask, render_template, request
from database.db import *

app=Flask(__name__, template_folder="template")

#@app.route('/')
@app.route('/register_page')
def register_page():
    return render_template("register.html")

@app.route('/register_user', methods=["post"])
def register_user():
    data = request.form
    code, name, lastname, project, hours, date = data["code"], data["name"], data["lastname"], data["project"], data["hours"], data["date"]
    print(code, name, lastname, project, hours, date)
    insert(code, name, lastname, project, hours, date)
    return "User added"


if __name__=="__main__":
    host = "127.0.0.1"
    port="5000"
    app.run(host,port,True)
