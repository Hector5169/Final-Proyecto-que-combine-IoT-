# Ejecuta esto una vez en tu terminal Python
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

productos = [
    ('Zapatos deportivos', 15, 'Juan Pedro', 'img/curso1.jpg'),
    ('Audífonos Bluetooth', 50, 'María López', 'img/curso2.jpg'),
    ('Smartwatch Pro', 120, 'Carlos Méndez', 'img/curso3.jpg'),
    ('Camiseta dry-fit', 25, 'Ana Torres', 'img/curso4.jpg'),
    ('Mochila casual', 45, 'Luis Fernández', 'img/curso5.jpg'),
    ('Lentes de sol', 30, 'Sofía Rivas', 'img/curso1.jpg'),
    ('Teclado mecánico', 80, 'Miguel Ángel', 'img/curso2.jpg'),
    ('Mouse gamer', 40, 'Daniela Cruz', 'img/curso3.jpg'),
    ('Monitor 24”', 200, 'Ricardo Sánchez', 'img/curso4.jpg'),
    ('Silla ergonómica', 150, 'Verónica Ruiz', 'img/curso5.jpg'),
    ('Router WiFi 6', 70, 'Jorge Castillo', 'img/curso1.jpg'),
    ('Cámara web HD', 60, 'Laura Martínez', 'img/curso2.jpg'),
]

c.executemany('INSERT INTO productos (nombre, precio, vendedor, imagen) VALUES (?, ?, ?, ?)', productos)
conn.commit()
conn.close()
