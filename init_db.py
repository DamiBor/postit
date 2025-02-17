import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO notes (content) VALUES (?)",
            ('Tu devrais jouer à Ys 1',)
            )

cur.execute("INSERT INTO notes ( content) VALUES (?)",
            ('Bon outil pour le dessin : Krita',)
            )

connection.commit()
connection.close()