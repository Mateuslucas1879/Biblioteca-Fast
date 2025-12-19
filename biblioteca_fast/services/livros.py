from sqlalchemy.orm import Session
from biblioteca_fast.database import models
from biblioteca_fast.schemas.livro_schema import LivroCreate
from typing import Optional

def criar_livro(db: Session, livro_in: LivroCreate) -> models.Livro:
    livro = models.Livro(**livro_in.dict())
    db.add(livro)
    db.commit()
    db.refresh(livro)
    return livro

def listar_livros(db:Session, skip: int = 0, limit: int =100):
    return db.query(models.Livro).offset(skip).limit(limit).all()


def obter_livro_por_id(db:Session, livro_id: int) -> Optional[models.Livro]:
    return db.get(models.Livro, livro_id)


def atualizar_livro(db: Session, livro_id: int, dados: dict):
    livro = db.get(models.Livro, livro_id)
    if not livro:
        return None
    for k, v in dados.items():
        if hasattr(livro, k):
            setattr(livro, k, v)
    db.commit()
    db.refresh(livro)
    return livro


def deletar_livro(db: Session, livro_id: int):
    livro = db.get(models.Livro, livro_id)
    if not livro:
        return None
    db.delete(livro)
    db.commit()
    return livro