# Proyecto Web Full Stack - Trabajo Grupal #3

## Tecnologías utilizadas

* Backend: FastAPI + SQLAlchemy + SQLite (o MySQL)
* Frontend: HTML, CSS, JavaScript Vanilla (Fetch API)
* Base de datos: SQLite (por defecto) o MySQL
* Control de versiones: Git y GitHub

## Estructura del proyecto

```
Trabajo3Grupo/
├── backend/
│   ├── main.py
│   ├── formularios.db (generado automáticamente)
│   ├── Script Sql Mysql.sql
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│
├── .gitignore
├── README.md
```

## Pasos para ejecutar

### Backend

1. Instalar dependencias:

```bash
pip install fastapi uvicorn sqlalchemy
```

2. Ejecutar el servidor:

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

3. Verificar en navegador:

```
http://localhost:8000/docs
```

### Frontend

1. Desde la carpeta frontend:

```bash
cd frontend
python -m http.server 5500
```

2. Acceder en el navegador:

```
http://localhost:5500/index.html
```

### Git

1. Agregar todo y hacer commit:

```bash
git add .
git commit -m "Estructura final backend y frontend funcionando"
```

2. Subir a GitHub:

```bash
git push
```

## Notas

* Configurar CORS y variables de entorno si se despliega en producción.
* Cambiar SQLite a MySQL si se requiere más robustez.
* Recordar agregar un archivo .gitignore con:

```
__pycache__/
*.db
.env
```

