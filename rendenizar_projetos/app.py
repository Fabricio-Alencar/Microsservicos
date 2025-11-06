# projetos/routes.py
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from rendenizar_projetos import dao

# --- Router (equivalente ao Blueprint no Flask) ---
router = APIRouter(tags=["Projetos"])  


# --- Modelos ---
class Projeto(BaseModel):
    nome: str
    id_idealizador: int
    nivel: str
    categoria: str
    descricao: str
    status: str

class Tecnologia(BaseModel):
    nome: str
    id_projeto: int

class Repositorio(BaseModel):
    nome: str
    id_projeto: int

# --- Projetos ---
@router.get("/projetos")
def get_projetos():
    projetos = dao.listar_projetos()
    print("Projetos carregados:", projetos)  # <-- aqui imprime no console do servidor
    return {"projetos": projetos}

# Obter um único projeto
@router.get("/projetos/{id_projeto}")
def get_projeto(id_projeto: int):
    projeto = dao.buscar_projeto_por_id(id_projeto)
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    print("Projeto carregado:", projeto)
    return {"projeto": projeto}

# --- Tecnologias ---
@router.get("/tecnologias")
def get_tecnologias(id_projeto: int | None = Query(None)):
    return {"tecnologias": dao.listar_tecnologias(id_projeto)}

# --- Repositórios ---
@router.get("/repositorios")
def get_repositorios(id_projeto: int | None = Query(None)):
    return {"repositorios": dao.listar_repositorios(id_projeto)}
