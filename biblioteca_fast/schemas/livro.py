from pydantic import BaseModel

class LivroBase(BaseModel):
    titulo: str
    autor: str
    isbn:str
    ano: int | None = None
    categoria: str | None = None

class LivroCreate(LivroBase):
    pass

class LivroUpdate(BaseModel):
    titulo: str | None = None
    autor: str | None = None
    ano: int | None = None
    categoria: str | None = None


class LivroOut(LivroBase):
    id : int
    disponivel : bool

    class Config:
        from_attributes = True
