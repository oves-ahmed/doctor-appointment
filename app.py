from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'user',     # Create a user in MySQL and replace here
    'password': 'password',  # Replace with your MySQL password
    'database': 'clinic'
}

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

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = """
                INSERT INTO appointments (name, email, phone, doctor, date, time, reason)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, email, phone, doctor, date, time, reason))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/success')
        except mysql.connector.Error as err:
            return f"<h3>Database Error:</h3><p>{err}</p>"

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
