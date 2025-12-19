
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from biblioteca_fast.database.connection import Base

class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True,index=True)
    titulo = Column(String(255),nullable=False)
    autor = Column(String(255), nullable=False)
    isbn = Column(String(50), unique=True, index=True, nullable=False)
    ano = Column(Integer, nullable=True)
    categoria = Column(String(100), nullable=True)
    disponivel = Column(Boolean, default=True)
    emprestimos = relationship("Emprestimo", back_populates="livro")