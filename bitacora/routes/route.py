from flask import render_template, request, jsonify
from server import app
from database.db import *
from controllers.admin_s3 import *

#@app.route('/')
#def home_page():
#    return render_template("home.html")

#@app.route('/')
@app.route('/register_page')
def register_page():
    return render_template("register.html")

@app.route('/consult_page')
def consult_page():
    return render_template("consult.html")

@app.route('/register_user', methods=["post"])
def register_user():
    data = request.form
    file = request.files
    code, name, lastname, project, hours, date = data["code"], data["name"], data["lastname"], data["project"], data["hours"], data["date"]
    print(code, name, lastname, project, hours, date)
    photo = file["photo"]
    photo_path = save_file(code,photo)
    session_s3 = connectionS3()
    upload_file_s3(session_s3, photo_path)
    print(photo.filename)
    #insert(code, name, lastname, project, hours, date)
    return "User added"

#@app.route('/consult_user')
#def consult_user():
#    result = consult() #   print(result)
#    return "usuario consultado"

@app.route('/consult_user', methods=["post"])
def consult_user():
    code = request.get_json()
    #print("ahora si" + code)
    result = consult(code)
    print (result)
    #return "usuario consultado"
    resp_data = {
        'name':result[0][1],
       'lastname':result[0][2],
       'project':result[0][3],
       'hour':result[0][4],
       'date':result[0][5]
    }
    return jsonify(resp_data)

    