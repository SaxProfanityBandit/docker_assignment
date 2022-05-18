#Imports
from flask import Flask, jsonify, make_response 
from flask_mysqldb import MySQL
from flask import request

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'sax'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask'
app.config['JSON_AS_ASCII'] = False

mysql = MySQL(app)

@app.route('/')
def hello():
   index = """
   <html>
   <h1>Available routes</h1><br>
   <li><a href='/users'>Users (GET)</a></li>
   <li><a href='/users'>Users (POST), recommend using REST client to send data.</a></li>
   </html>"""
   return index

@app.route('/users', methods=['GET', 'POST'])
def users():
   if request.method == "POST":
      details = request.json
      name = details['name']
      age = details['age']
      cur = mysql.connection.cursor()
      cur.execute("INSERT INTO persons(Name, Age) VALUES (%s, %s)", (name, age))
      mysql.connection.commit()
      cur.close()
      return 'Success!'
   elif request.method == "GET":
      cur = mysql.connection.cursor()
      cur.execute("SELECT * FROM persons")
      mysql.connection.commit()
      data = cur.fetchall()
      cur.close()
      return jsonify(data);
   else:
      return "Whoops, something went wrong!"

if __name__ == '__main__':
    app.run(
       host="0.0.0.0",
       debug=True
)
