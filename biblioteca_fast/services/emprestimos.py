from sqlalchemy.orm import Session
from datetime import datetime
from biblioteca_fast.database import models
from biblioteca_fast.schemas.emprestimo_schema import EmprestimoCreate
from typing import Optional

def criar_emprestimo(db: Session, emp:EmprestimoCreate) -> Optional[models]:
    usuario = db.get(models.Usuario, emp.usuario_id)
    livro = db.get(models.Livro, emp.livro_id)
    if not usuario or not livro or not livro.disponivel:
        return None
    emprestimo = models.Emprestimo(
        usuario_id = emp.usuario_id,
        livro_id = emp.livro_id,
        data_devolucao_prevista=emp.data_devolucao_prevista,
        status="emprestado"
    )
    livro.disponivel = False
    db.add(emprestimo)
    db.commit()
    db.refresh(emprestimo)
    return emprestimo

def listar_emprestimos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Emprestimo).offset(skip).limit(limit).all()

def obter_emprestimo_por_id(db: Session, emprestimo_id: int) -> Optional[models.Emprestimo]:
    return db.get(models.Emprestimo, emprestimo_id)

def devolver_livro(db:Session,emprestimo_id: int) -> Optional[models.Usuario]
    emprestimo = db.get(models.Emprestimo, emprestimo_id)
    if not emprestimo or emprestimo.status == "devolvido":
        return None
    emprestimo.data_devolucao_real = datetime.utcnow()
    emprestimo.status = "devolvido"
    livro = db.get(models.Livro, emprestimo.livro_id)
    if livro:
        livro.disponivel = True
    db.commit()
    db.refresh(emprestimo)
    return emprestimo

def deletar_emprestimo(db: Session, emprestimo_id: int):
    emprestimo = db.get(models.Emprestimo, emprestimo_id)
    if not emprestimo:
        return None
    livro = db.get(models.Livro, emprestimo.livro_id)
    if livro:
        livro.disponivel = True
    db.delete(emprestimo)
    db.commit()
    return emprestimo