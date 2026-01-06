from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.connection import Base

class Livro(Base):
    __tablename__ = "livros"
    id = Column(Integer, primary_key=True,index=True)
    titulo= Column(String(255), nullable=False,index=True)
    autor = Column(String(255),nullable=False,index=True)
    categoria = Column(String(100),nullable=True,index=True)
    ano = Column(Integer, nullable=True)
    disponivel = Column(Boolean, default=True, nullalble=False)
    criando = Column(DateTime,default=datetime.utcnow,nullable=False)
    emprestimos = relationship("Emprestimos",back_populates="livro",cascade="all, delete-orphan")

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255),nullable=False)
    email = Column(String(255),unique=True,index=True,nullable=False)
    hashed_password = Column(String(255),nullable=False)
    is_admin = Column(Boolean, default=False,nullable=False)
    criando = Column(Boolean, default=datetime.utcnow,nullable=False)
    emprestimos = relationship("Emprestimo",back_populates="usuarios",cascade="all, delete-orphan")

class Emprestimo(Base):
    __tablename = "emprestimos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    livro_id = Column(Integer, ForeignKey("livros.id"), nullable=False)
    data_emprestimo = Column(DateTime, default=datetime.utcnow, nullable=False)
    data_devolucao_prevista = Column(DateTime, nullable=False)
    data_devolucao_real = Column(DateTime, nullable=True)
    status = Column(String(50), nullable=False, default="emprestado")
    usuario = relationship("Usuario", back_populates="emprestimos")
    livro = relationship("Livro", back_populates="emprestimos")