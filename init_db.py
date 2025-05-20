# init_db.py
import sqlite3

# Conecta o crea el archivo database.db
conn = sqlite3.connect('database.db')

# Carga el contenido de schema.sql
with open('schema.sql') as f:
    conn.executescript(f.read())

print("Base de datos creada correctamente.")

conn.close()
