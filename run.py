from flask import Flask, render_template
from db import get_db_connection, get_all_notes

# Flask application creation
app = Flask(__name__)

# Route for the index page of the app
@app.route('/')
def index():
    conn = get_db_connection()
    notes = get_all_notes()
    return render_template('index.html', notes=notes)

# Run the flask app if this file is executed as main
if __name__ == "__main__":
    app.run(debug=True)

