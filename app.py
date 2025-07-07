from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'clinic'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        doctor = request.form['doctor']
        date = request.form['date']
        time = request.form['time']
        reason = request.form['reason']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO appointments (name, email, phone, doctor, date, time, reason) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (name, email, phone, doctor, date, time, reason))
        mysql.connection.commit()
        cur.close()
        return redirect('/success')

@app.route('/success')
def success():
    return "<h2>✅ Appointment Booked Successfully!</h2><p><a href='/'>Back to Home</a></p>"

if __name__ == '__main__':
    app.run(debug=True)
