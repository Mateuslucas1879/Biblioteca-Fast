from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from biblioteca_fast.database.connection import engine, Base
from biblioteca_fast.routers import usuarios, livros, emprestimos

def create_app() -> FastAPI:
    Base.metadata.create_all(bind=engine)
    app = FastAPI(
        title="Biblioteca FastAPI",
        version="1.0.0",
        description="Sistema profissional de gerenciamento de biblioteca."
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])
    app.include_router(livros.router, prefix="/livros", tags=["livros"])
    app.include_router(emprestimos.router, prefix="/emprestimos", tags=["emprestimos"])
    return app

app = create_app()
