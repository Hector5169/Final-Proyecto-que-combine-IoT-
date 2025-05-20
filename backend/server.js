// backend/server.js
const express = require('express');
const fs = require('fs');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

const USERS_FILE = './data/usuarios.json';
const REVIEWS_FILE = './data/resenas.json';

// Helper para leer y guardar archivos JSON
function readJSON(path) {
    if (!fs.existsSync(path)) return [];
    return JSON.parse(fs.readFileSync(path));
}

function writeJSON(path, data) {
    fs.writeFileSync(path, JSON.stringify(data, null, 2));
}

// Ruta de login o registro automático
app.post('/api/login', (req, res) => {
    const { email, password } = req.body;
    let users = readJSON(USERS_FILE);
    let user = users.find(u => u.email === email);

    if (!user) {
        user = { email, password, compras: [] };
        users.push(user);
        writeJSON(USERS_FILE, users);
        return res.json({ success: true, nuevo: true });
    }

    if (user.password !== password) {
        return res.status(401).json({ success: false, error: 'Contraseña incorrecta' });
    }

    return res.json({ success: true, nuevo: false });
});

// Ruta para registrar una compra
app.post('/api/comprar', (req, res) => {
    const { email, producto } = req.body;
    let users = readJSON(USERS_FILE);
    const user = users.find(u => u.email === email);

    if (!user) return res.status(404).json({ success: false, error: 'Usuario no encontrado' });

    if (!user.compras.includes(producto)) {
        user.compras.push(producto);
        writeJSON(USERS_FILE, users);
    }

    res.json({ success: true });
});

// Ruta para dejar una reseña
app.post('/api/reseña', (req, res) => {
    const { producto, usuario, texto } = req.body;
    const reseñas = readJSON(REVIEWS_FILE);

    reseñas.push({ producto, usuario, texto });
    writeJSON(REVIEWS_FILE, reseñas);

    res.json({ success: true });
});

// Ruta para obtener reseñas de un producto
app.get('/api/reseñas/:producto', (req, res) => {
    const producto = req.params.producto;
    const reseñas = readJSON(REVIEWS_FILE);
    const filtradas = reseñas.filter(r => r.producto === producto);
    res.json(filtradas);
});

app.listen(PORT, () => {
    console.log(`Servidor iniciado en http://localhost:${PORT}`);
});