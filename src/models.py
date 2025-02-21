# Importamos las bibliotecas necesarias
import os  # Importa el módulo os para interactuar con el sistema operativo (aunque no se usa en este script)
import sys  # Importa el módulo sys para manipular parámetros de entrada/salida (aunque tampoco se usa en este script)
from sqlalchemy.orm import declarative_base, relationship  # Importa la clase base y relación de SQLAlchemy
from sqlalchemy import create_engine, String, Integer, ForeignKey, Column  # Importa tipos de datos y funciones de SQLAlchemy
from eralchemy2 import render_er  # Importa la función render_er para generar un diagrama visual de la base de datos

# Define la clase base para todos los modelos
Base = declarative_base()

# Definición del modelo de la tabla "user"
class User(Base):
    __tablename__ = 'user'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)  # Define la columna 'id' como clave primaria
    username = Column(String, unique=True, nullable=False)  # Define la columna 'username' como única y no nula
    firstname = Column(String, nullable=False)  # Define la columna 'firstname' como no nula
    lastname = Column(String, nullable=False)  # Define la columna 'lastname' como no nula
    email = Column(String, unique=True, nullable=False)  # Define la columna 'email' como única y no nula

    # Establece una relación con la tabla 'Favorito', indicando que un usuario puede tener varios favoritos
    favoritos = relationship("Favorito", backref="usuario")

# Definición del modelo de la tabla "planeta"
class Planeta(Base):
    __tablename__ = 'planeta'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)  # Define la columna 'id' como clave primaria
    nombre = Column(String, unique=True, nullable=False)  # Define la columna 'nombre' como única y no nula
    clima = Column(String, nullable=False)  # Define la columna 'clima' como no nula
    terreno = Column(String, nullable=False)  # Define la columna 'terreno' como no nula

    # Establece una relación con la tabla 'Favorito', indicando que un planeta puede ser marcado como favorito
    favoritos = relationship("Favorito", backref="planeta")

# Definición del modelo de la tabla "personaje"
class Personaje(Base):
    __tablename__ = 'personaje'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)  # Define la columna 'id' como clave primaria
    nombre = Column(String, unique=True, nullable=False)  # Define la columna 'nombre' como única y no nula
    especie = Column(String, nullable=False)  # Define la columna 'especie' como no nula
    altura = Column(String, nullable=False)  # Define la columna 'altura' como no nula

    # Establece una relación con la tabla 'Favorito', indicando que un personaje puede ser marcado como favorito
    favoritos = relationship("Favorito", backref="personaje")

# Definición del modelo de la tabla intermedia "favorito" (relación muchos a muchos)
class Favorito(Base):
    __tablename__ = 'favorito'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)  # Define la columna 'id' como clave primaria
    usuario_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # Clave foránea a la tabla 'user', no nula
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)  # Clave foránea a la tabla 'planeta', puede ser nula
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)  # Clave foránea a la tabla 'personaje', puede ser nula

# Generación del diagrama de la base de datos
try:
    result = render_er(Base, 'diagram.png')  # Llama a 'render_er' para generar el diagrama y guardarlo como 'diagram.png'
    print("Success! Check the diagram.png file")  # Si todo sale bien, imprime el mensaje de éxito
except Exception as e:
    print("There was a problem generating the diagram")  # Si ocurre un error, muestra un mensaje de error
    raise e  # Lanza nuevamente el error para depuración
