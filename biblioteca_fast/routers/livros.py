
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from biblioteca_fast.database.connection import get_db
from biblioteca_fast.schemas.livro_schema import LivroCreate, LivroResponse, LivroUpdate
from biblioteca_fast.services.livros_service import criar_livro, listar_livros, obter_livro_por_id, atualizar_livro, deletar_livro

router = APIRouter(prefix="/livros", tags=["Livros"])

@router.post("/",response_model=LivroResponse,status_code=status.HTTP_201_CREATED)
def api_criar_livro(livro: LivroCreate, db: Session = Depends(get_db)):
    return criar_livro(db, livro)

@router.get("/", response_model=List[LivroResponse])
def api_listar_livros(skip: int =0,limit:int = 100, db:Session = Depends(get_db)):
    return listar_livros(db, skip=skip, limit=limit)

@router.get("/{livro_id}",response_model=LivroResponse)
def api_obter_livro(livro_id: int, db:Session = Depends(get_db)):
    livro = obter_livro_por_id(db, livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro

@router.put("/{livro_id}", response_model=LivroResponse)
def api_atualizar_livro(livro_id: int, dados: LivroUpdate, db: Session = Depends(get_db)):
    livro = atualizar_livro(db, livro_id, dados.dict(exclude_unset=True))
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro

@router.delete("/{livro_id}", response_model=LivroResponse)
def api_deletar_livro(livro_id: int, db:Session = Depends(get_db)):
    livro = deletar_livro(db, livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro
