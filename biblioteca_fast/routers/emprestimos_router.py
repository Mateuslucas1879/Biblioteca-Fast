
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from biblioteca_fast.database.connection import get_db
from biblioteca_fast.schemas.emprestimo_schema import EmprestimoCreate, EmprestimoReturn
from biblioteca_fast.services.emprestimos_service import criar_emprestimo, listar_emprestimos, obter_emprestimo_por_id, devolver_livro, deletar_emprestimo


router = APIRouter(prefix="/emprestimos", tags=["Emprestimos"])

@router.post("/", response_model=EmprestimoReturn, status_code=status.HTTP_201_CREATED)
def api_criar_emprestimo(payload: EmprestimoCreate, db:Session = Depends(get_db)):
    emprestimo = criar_emprestimo(db, payload)
    if not emprestimo:
        raise HTTPException(status_code=400, detail="Não foi possível criar empréstimo")
    return emprestimo


@router.get("/", response_model=List[EmprestimoReturn])
def api_listar_emprestimos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return listar_emprestimos(db, skip=skip, limit=limit)

@router.get("/{emprestimo_id}", response_model=EmprestimoReturn)
def api_obter_emprestimo(emprestimo_id: int, db: Session = Depends(get_db)):
    emprestimo = obter_emprestimo_por_id(db, emprestimo_id)
    if not emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
    return emprestimo

@router.post("/{emprestimo_id}/devolver", response_model=EmprestimoReturn)
def api_devolver_emprestimo(emprestimo_id: int, db: Session = Depends(get_db)):
    emprestimo = devolver_livro(db, emprestimo_id)
    if not emprestimo:
        raise HTTPException(status_code=400, detail="Operação de devolução falhou")
    return emprestimo


@router.delete("/{emprestimo_id}", response_model=EmprestimoReturn)
def api_deletar_emprestimo(emprestimo_id: int, db: Session = Depends(get_db)):
    emprestimo = deletar_emprestimo(db, emprestimo_id)
    if not emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
    return emprestimo