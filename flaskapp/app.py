#Imports
from flask import Flask, jsonify, make_response 
from flask_mysqldb import MySQL
from flask import request

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'docker'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
app.config['JSON_AS_ASCII'] = False

mysql = MySQL(app)




@app.route('/')
def hello():
   return 'Hello!'

if __name__ == '__main__':
    app.run()