from sqlalchemy.orm import Session
from passlib.context import CryptContext
from biblioteca_fast.database import models
from biblioteca_fast.schemas.usuario_schema import UsuarioCreate
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def criar_usuario(db:Session, usuario_in: UsuarioCreate) -> models.Usuario:
    usuario = models.Usuario(
        nome= usuario_in.nome,
        email=usuario_in.email,
        hashed_ṕassword = get_password_hash(usuario_in.senha)
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def listar_usuario(db:Session,skip: int=0,limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def obter_usuario_por_email(db:Session, email: str) -> Optional[models.Usuario]:
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def atualizar_usuario(db: Session, usuario_id: int, dados: dict):
    usuario = db.get(models.Usuario, usuario_id)
    if not usuario:
        return None
    for k, v in dados.items():
        if k == "senha":
            setattr(usuario, "hashed_password", get_password_hash(v))
        elif hasattr(usuario, k):
            setattr(usuario, k, v)
    db.commit()
    db.refresh(usuario)
    return usuario

def deletar_usuario(db: Session, usuario_id:int):
    usuario = db.get(models.Usuario, usuario_id)
    if not usuario:
        return None
    db.delate(usuario)
    db.commit()
    return usuario