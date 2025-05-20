from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from flask import Flask, render_template, request, redirect, url_for, session, g, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'secreto123'  # para sesiones

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Inicializar la DB desde schema.sql
def init_db():
    with app.app_context():
        db = get_db()
        with open('schema.sql', 'r') as f:
            db.executescript(f.read())
        db.commit()

# Rutas básicas

@app.route('/')
def index():
    db = get_db()
    productos = db.execute('SELECT * FROM productos').fetchall()
    return render_template('index.html', productos=productos, usuario=session.get('username'))

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    db = get_db()
    try:
        db.execute('INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)', (username, password))
        db.commit()
        return redirect(url_for('index'))
    except:
        return 'Usuario ya existe'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db = get_db()
    user = db.execute('SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?', (username, password)).fetchone()
    if user:
        session['user_id'] = user['id']
        session['username'] = user['usuario']
        return redirect(url_for('index'))
    else:
        return 'Credenciales inválidas'

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Ruta para ver el producto y reseñas
@app.route('/producto/<int:producto_id>', endpoint='producto')
def producto(producto_id):
    db = get_db()

    # Obtener info producto
    producto = db.execute(
        'SELECT * FROM productos WHERE id = ?', (producto_id,)
    ).fetchone()

    if producto is None:
        return "Producto no encontrado", 404

    # Obtener reseñas del producto (con nombre usuario)
    reseñas = db.execute('''
        SELECT r.comentario, r.calificacion, u.usuario
        FROM resenas r JOIN usuarios u ON r.usuario_id = u.id
        WHERE r.producto_id = ?
        ORDER BY r.id DESC
    ''', (producto_id,)).fetchall()

    # Datos de usuario logueado (si hay)
    user = None
    if 'user_id' in session:
        user = db.execute('SELECT * FROM usuarios WHERE id = ?', (session['user_id'],)).fetchone()

    return render_template(
        'producto.html',
        producto=producto,
        reseñas=reseñas,
        usuario=user['usuario'] if user else None  # 👈 pasamos solo el nombre de usuario
    )



@app.route('/producto/<int:producto_id>/agregar_resena', methods=['POST'])
def agregar_resena(producto_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    comentario = request.form.get('comentario')
    calificacion = request.form.get('calificacion')

    if not comentario or not calificacion:
        flash("Por favor completa todos los campos.")
        return redirect(url_for('producto', producto_id=producto_id))

    db = get_db()
    db.execute(
        'INSERT INTO resenas (usuario_id, producto_id, comentario, calificacion) VALUES (?, ?, ?, ?)',
        (session['user_id'], producto_id, comentario, calificacion)
    )
    db.commit()
    flash("Reseña agregada con éxito.")
    return redirect(url_for('producto', producto_id=producto_id))


if __name__ == '__main__':
    for rule in app.url_map.iter_rules():
        print(rule.endpoint, rule)

    app.run(debug=True)