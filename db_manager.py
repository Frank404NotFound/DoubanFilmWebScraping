import sqlite3 as sq

conn = sq.connect('db/data.db')

#conn.execute('CREATE TABLE movies (id INTEGER PRIMARY KEY NOT NULL, img_url TEXT, name TEXT, rate REAL, num_comm INTERGER)')
conn.execute('CREATE TABLE comments (movie_id INTEGER NOT NULL, content TEXT NOT NULL, user_id TEXT NOT NULL)')


conn.close()
