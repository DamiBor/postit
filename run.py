import sqlite3
from flask import Flask, render_template

# Create and return a connection to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Flask application creation
app = Flask(__name__)

# Route for the index page of the app
@app.route('/')
def index():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM notes').fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

# Run the flask app if this file is executed as main
if __name__ == "__main__":
    app.run(debug=True)

