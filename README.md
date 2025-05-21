# Proyecto Final

**Autores:**  
- Eduardo Quetzal Delgado Pimentel  
- Rodríguez González Kevin Oswaldo  
- Héctor de Jesús Palomar Cebrero  

**Universidad de Guadalajara – CUCEI**  
**Materia:** Programación para Internet

---

## Descripción

Este proyecto es una plataforma de comercio electrónico enfocada en cursos en línea, desarrollada con **Flask (Python)** como backend, **SQLite** como base de datos y tecnologías como **HTML5, CSS3 y JavaScript** para el frontend. La plataforma permite a los usuarios:

- Registrarse e iniciar sesión de forma segura.
- Navegar por un catálogo de cursos.
- Añadir cursos a un carrito de compras.
- Dejar reseñas usando un Micro Controlador de Producto (MCP) implementado en JavaScript.
- Persistencia de reseñas usando `localStorage`.
- Integración futura con tecnologías **IoT** e **Inteligencia Artificial (IA)** para mejorar la experiencia del usuario.

---

## Características

- **Autenticación de usuarios**  
- **Catálogo de cursos** con precios, descripciones e imágenes  
- **Carrito de compras persistente**  
- **Sistema de reseñas interactivo**  
- **Arquitectura cliente-servidor escalable**  
- **Interfaz moderna y responsiva**  
- **Base sólida para integraciones futuras (IA, IoT)**

---

## Estructura del Proyecto

---

## Requisitos

- Python 3.8+
- Flask (`pip install flask`)
- SQLite3 (incluido con Python)

---

## Cómo ejecutar el proyecto

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio

# 2. Instalar dependencias
pip install flask

# 3. Inicializar la base de datos
sqlite3 database.db < schema.sql

# 4. Ejecutar el servidor
python app.py


