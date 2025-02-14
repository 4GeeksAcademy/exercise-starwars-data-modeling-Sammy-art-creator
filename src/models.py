import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, Integer, ForeignKey, Column
from eralchemy2 import render_er

# Define la base para los modelos de SQLAlchemy, permitiendo la creación de tablas.
Base = declarative_base()

# Define la tabla de usuarios, que almacenará la información de cada usuario registrado.
class Usuario(Base):
    __tablename__ = 'usuario'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    fecha_suscripcion: Mapped[str] = mapped_column(String, nullable=False)
    favoritos = relationship("Favorito", back_populates="usuario")
    posts = relationship("Post", back_populates="usuario")
    comentarios = relationship("Comentario", back_populates="usuario")

# Define la tabla de planetas, que almacenará información sobre los planetas de Star Wars.
class Planeta(Base):
    __tablename__ = 'planeta'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    clima: Mapped[str] = mapped_column(String, nullable=False)
    terreno: Mapped[str] = mapped_column(String, nullable=False)
    favoritos = relationship("Favorito", back_populates="planeta")

# Define la tabla de personajes, que almacenará información sobre los personajes de Star Wars.
class Personaje(Base):
    __tablename__ = 'personaje'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    especie: Mapped[str] = mapped_column(String, nullable=False)
    altura: Mapped[str] = mapped_column(String, nullable=False)
    favoritos = relationship("Favorito", back_populates="personaje")

# Tabla intermedia para almacenar los favoritos de cada usuario, permitiendo la relación con planetas y personajes.
class Favorito(Base):
    __tablename__ = 'favorito'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    planeta_id: Mapped[int] = mapped_column(ForeignKey("planeta.id"), nullable=True)
    personaje_id: Mapped[int] = mapped_column(ForeignKey("personaje.id"), nullable=True)
    usuario = relationship("Usuario", back_populates="favoritos")
    planeta = relationship("Planeta", back_populates="favoritos")
    personaje = relationship("Personaje", back_populates="favoritos")

# Define la tabla de publicaciones (posts), donde los usuarios pueden compartir contenido.
class Post(Base):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    contenido: Mapped[str] = mapped_column(String, nullable=False)
    usuario = relationship("Usuario", back_populates="posts")
    comentarios = relationship("Comentario", back_populates="post")
    media = relationship("Media", back_populates="post")

# Define la tabla de comentarios, que permite a los usuarios comentar en los posts.
class Comentario(Base):
    __tablename__ = 'comentario'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    comentario_text: Mapped[str] = mapped_column(String, nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    usuario = relationship("Usuario", back_populates="comentarios")
    post = relationship("Post", back_populates="comentarios")

# Define la tabla de medios, que almacena imágenes o videos relacionados con los posts.
class Media(Base):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    url: Mapped[str] = mapped_column(String, nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post = relationship("Post", back_populates="media")

# Genera un diagrama de la base de datos a partir de los modelos definidos.
render_er(Base, 'diagram.png')
