#Imports
from flask import Flask, jsonify, make_response
import mysql.connector
#from datetime import datetime
from flask import request

app = Flask(__name__)

db = mysql.connector.connect(
    host='127.0.0.1',
    user='warehouse_admin',
    passwd='devops',
    db='warehouse',
)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello():
   return 'Hello!'

if __name__ == '__main__':
    app.run()