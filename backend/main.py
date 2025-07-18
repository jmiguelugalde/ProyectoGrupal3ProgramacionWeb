from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware

# Configuración de la base de datos
DATABASE_URL = "sqlite:///./formularios.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Modelo de datos
class Formulario(Base):
    __tablename__ = "formularios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    correo = Column(String(100))
    intereses = Column(String(200))
    descripcion = Column(Text)

Base.metadata.create_all(bind=engine)

# Modelo para FastAPI
class FormularioSchema(BaseModel):
    nombre: str
    correo: str
    intereses: str
    descripcion: str

# Instancia de FastAPI
app = FastAPI()

# Configurar CORS para permitir el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta para obtener todos los formularios
@app.get("/formularios/")
def get_formularios():
    db = SessionLocal()
    formularios = db.query(Formulario).all()
    db.close()
    return formularios

# Ruta para crear un nuevo formulario
@app.post("/formularios/")
def create_formulario(formulario: FormularioSchema):
    db = SessionLocal()
    nuevo = Formulario(
        nombre=formulario.nombre,
        correo=formulario.correo,
        intereses=formulario.intereses,
        descripcion=formulario.descripcion
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    db.close()
    return nuevo
