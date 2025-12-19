from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha:str

class UsuarioLogin(BaseModel):
    email: EmailStr
    semha:str

class UsuarioOut(UsuarioBase):
    id: int
    ativo: bool

    class Config:
        from_attributes = True

