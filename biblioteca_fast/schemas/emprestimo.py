from pydantic import BaseModel
from datetime import date

class EmprestimoCreate(BaseModel):
    usuario_id: int
    livro_id: int
    data_emprestimo: date
    data_devolucao: date | None = None


class EmprestimoOut(BaseModel):
    id: int
    usuario_id: int
    livro_id: int
    data_emprestimo: date
    data_devolucao: date | None

    class Config:
        from_attributes = True