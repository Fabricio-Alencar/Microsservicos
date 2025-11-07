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
@router.get("/projetos/{id_idealizador}")
def get_projetos(id_idealizador: int):
    projetos = dao.listar_projetos(id_idealizador)
    print(f"🧠 Projetos carregados (idealizador={id_idealizador}):", projetos)
    return {"projetos": projetos or []}





# Obter um único projeto
@router.get("/projeto/{id_projeto}")
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
