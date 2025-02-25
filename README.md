
# Prueba Técnica

Este repositorio contiene el backend y el frontend para la prueba técnica. propuesta

## Backend

Desarrollado usando Python 3.11 y Django 5.1.6. Para la administración de versiones de lenguaje y de packages se usaron [pyenv](https://github.com/pyenv/pyenv) y [pip](https://pypi.org/project/pip/).

El backend de la aplicación está contenido en la carpeta **tasks_backend**.

### Inicialización del proyecto

1. `pyenv install`, automáticamente leerá el archivo **.python-version** y se intslará la versión especificada.
2. `python -m venv .venv`, creación del entorno virtual.
3. `source .venv/bin/activate`, activación del entorno virtual.
4. `pip install -r requirements.txt`, instalar los packages necesarios.

Para realizar cualquier operación por terminal en el back se debe tener activado el entorno virtual, `source .venv/bin/activate`.

### Base de datos y migraciones

1. `python manage.py migrate`, migrará los modelos de la aplicación y generará una base de datos en SQLite.
2. `python manage.py db_seeder`, poblará la base de datos con algunos elementos.

### Despliegue

1. `python manage.py ruserver`, despliega la aplicación, y hace accesibles los datos.

De forma opcional, se puede usar el comando `python manage.py createsuperuser` para crear un super usuario, el cual podrá acceder al panel de administrador nativo de Django.

- **localhost:8000/admin** abrirá el panel de administrador de Django.
- **localhost:8000/api** muestrá los endpoints disponibles para la API creada.

## Frontend

---
