# Proyecto Web Full Stack - Trabajo Grupal #3

## Tecnologías utilizadas

* Backend: FastAPI + SQLAlchemy + SQLite (o MySQL)
* Frontend: HTML, CSS, JavaScript Vanilla (Fetch API)
* Base de datos: SQLite (por defecto) o MySQL

## Pasos para ejecutar

### Backend

1. Instalar dependencias:

```bash
pip install -r requirements.txt
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


