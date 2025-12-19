
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from biblioteca_fast.database.connection import Base

class Usuario(Base):
    __tablename__ = "Usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255),nullable=False)
    email = Column(String(255),unique=True,index=True,nullable=False)
    senha_hash = Column(String(255),nullable=False)
    ativo = Column(Boolean,default=True)
    emprestimos = relationship("Emprestimos",back_populates="usuario")

