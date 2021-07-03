from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'database-niro.caomyyms75ok.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'niro'
app.config['MYSQL_PASSWORD'] = 'niro321'
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['firstname']
        lastName = details['lastname']
        age = details['age']
        hobby = details['hobby']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO details(firstName, lastName, age, hobby) VALUES (%s, %s, %s, %s)", (firstName, lastName, age, hobby))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/users')
def users():
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM details")

        if resultValue > 0:
                usersDetails = cur.fetchall()
                return render_template('users.html',usersDetails=usersDetails)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
