import sqlite3

DB_FILE = "database.db"
SQL_FILE = "schema.sql"

# Create and return a connection to the database with access to the column by name
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the databse content from the schema.sql file
def init_db():
    connection = get_db_connection()
    with open(SQL_FILE) as f:
        connection.executescript(f.read())
    connection.commit()
    connection.close()

# Fill the database with made up values for testing purposes
def fill_db_test():
    add_note("Tu devrais jouer à Ys 1")
    add_note("Bon outil pour le dessin : Krita")

# Add a new note in the database with given content
def add_note(content):
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("INSERT INTO notes (content) VALUES (?)", (content,))
    connection.commit()
    connection.close()

# Return all elements of the notes table as a list
def get_all_notes():
    connection = get_db_connection()
    notes = connection.execute('SELECT * FROM notes').fetchall()
    connection.close()
    return notes