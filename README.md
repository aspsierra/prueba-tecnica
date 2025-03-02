
# Prueba Técnica

Este repositorio contiene el backend y el frontend para la prueba técnica propuesta

## Docker

El proyecto está preparado para usarse con docker en modo desarrollo, para crear los contenedores ejecutar:

- `docker compose up --build`, compilar el contenedor y levantarlos. Durante este paso se 
solicitará por consola crear un super usuario para poder acceder al panel de administrador de 
Django

- `docker compose down` para parar los contenedores. En caso de querer volver a levantarlos: 
`docker compose up --build`

Las rutas para la aplicación serán las mismas que sin usar docker:

- **localhost:8000/admin** abrirá el panel de administrador de Django.
- **localhost:8000/api** muestrá los endpoints disponibles para la API creada.+
- **localhost:5173/**, ruta del frontend.

## Backend

Desarrollado usando Python 3.11 y Django 5.1.6. Para la administración de versiones de lenguaje y de packages se usaron [pyenv](https://github.com/pyenv/pyenv) y [pip](https://pypi.org/project/pip/).

Para la autenticación de usuarios se usa un token JWT. También se da la opción de usar la autenticación usando el SSO de Github.

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

- `python manage.py runserver`, despliega la aplicación, y hace accesibles los datos.

De forma opcional, se puede usar el comando `python manage.py createsuperuser` para crear un super usuario, el cual podrá acceder al panel de administrador nativo de Django.

- **localhost:8000/admin** abrirá el panel de administrador de Django.
- **localhost:8000/api** muestrá los endpoints disponibles para la API creada.

### Tests unitarios de la API

Se crearon unos cuantos tests para la api *tasks_backend/tasks_app/tests*. para ejecutarlos, usar el siguiente comando:

- `python manage.py test tasks_app/tests/`

## Frontend

Desarrollado usando Vue.js 3.5 y Vite 6.1. Para el estilo y apartado visual de la aplicación se usó [Tailwind 3.4](https://v3.tailwindcss.com/) y la biblioteca de componentes [DaisyUI](https://daisyui.com/). Además, se usa [NVM](https://github.com/nvm-sh/nvm) como gestor de la versión de Node.js del proyecto. Para los iconos, se usó la libería [Iconify](https://iconify.design/).

El backend de la aplicación está contenido en la carpeta **tasks_frontend**.

### Inicialización del frontend

1. `nvm install`, instalará la version de Node definida en el archivo **.nvmrc**.
2. `npm install`, instalar los packages necesarios para la aplicación.

### Despliegue y acceso

- `npm run dev`, despliega la aplicación en modo desarrollo.
- **localhost:5173/** es la ruta que usa la aplicación

## Permisos

La aplicación distingue entre dos tipos de usuarios, usuario común (sin registrar) y administradores (usuarios registrados y super usuarios).

- Los usuarios Comunes solo pueden ver la lista de tareas y los detalles de una tarea seleccionada, pero no pueden interactuar con ellas de ninguna forma.
- Los administradores tienen capacidad para modificar, crear y eliminar cualquier tarea.

---
