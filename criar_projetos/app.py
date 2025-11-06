from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from criar_projetos import dao  # ajuste conforme sua pasta/DAO

# --- Router ---
router = APIRouter(tags=["Projetos"])  

# --- Modelos Pydantic ---
class Projeto(BaseModel):
    nome: str
    id_idealizador: int
    nivel: str
    categoria: str
    status: str
    descricao: str  # necessário para o JS enviar

class Tecnologia(BaseModel):
    nome: str
    id_projeto: int

class Repositorio(BaseModel):
    nome: str
    id_projeto: int

# --- Projetos ---
@router.post("/projetos")
def create_projeto(projeto: Projeto):
    novo = dao.criar_projeto(
        projeto.nome,
        projeto.id_idealizador,
        projeto.nivel,
        projeto.categoria,
        projeto.descricao,
        projeto.status
    )
    return {"projeto": novo}

# --- Tecnologias ---
@router.post("/tecnologias")
def create_tecnologia(tech: Tecnologia):
    novo = dao.adicionar_tecnologia(tech.nome, tech.id_projeto)
    return {"tecnologia": novo}

# --- Repositórios ---
@router.post("/repositorios")
def create_repositorio(repo: Repositorio):
    novo = dao.adicionar_repositorio(repo.nome, repo.id_projeto)
    return {"repositorio": novo}
