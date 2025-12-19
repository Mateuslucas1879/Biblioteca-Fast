
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from biblioteca_fast.database.connection import Base

class Emprestimos(Base):
    __tablename__ = "emprestimos"
    id = Column(Integer, primary_key=True,index=True)
    usuario_id = Column(Integer,ForeignKey("usuarios.id"), nullable=False)
    livro_id = Column(Integer, ForeignKey("livros.id"),nullable=False)
    data_emprestimo = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=True)
    usuario = relationship("Usuario",back_populates="emprestimos")
    livro = relationship("Livro", back_populates="emprestimos")

