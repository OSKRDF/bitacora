from flask import Flask
from controllers.admin_s3 import *

app = Flask(__name__, template_folder="template")
from routes.route import *


if __name__=="__main__":
    host = "172.31.2.229"
    port="80"
    app.run(host,port,True)