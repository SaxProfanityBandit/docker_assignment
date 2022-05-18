#Imports
from flask import Flask, jsonify, make_response 
from flask_mysqldb import MySQL
from flask import request

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'docker'
#app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
app.config['JSON_AS_ASCII'] = False

mysql = MySQL(app)

@app.route('/')
def hello():
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM persons")
   data = cur.fetchall()
   mysql.connection.commit()
   cur.close()
   return data;
   #return 'Hello!'

@app.route('/users', methods=['GET', 'POST'])
def users():
   if request.method == "POST":
      details = request.form
      name = details['name']
      age = details['age']
      cur = mysql.connection.cursor()
      cur.execute("INSERT INTO persons(name, age) VALUES (%s, %s)", (name, age))
      mysql.connection.commit()
      cur.close()
      return 'Success!'
   elif request.method == "GET":
      cur = mysql.connection.cursor()
      cur.execute("SELECT * FROM persons")
      data = cur.fetchall()
      mysql.connection.commit()
      cur.close()
      return data;
   else:
      return "Whoops, something went wrong!"

if __name__ == '__main__':
    app.run(
       host="0.0.0.0",
       debug=True
)
