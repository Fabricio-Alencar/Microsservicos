# projetos/routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from gerenciar_projetos import dao

# --- Router ---
router = APIRouter(tags=["Projetos"])


# --- Modelos Pydantic ---
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


# ============================================================
# 🔹 PROJETOS (edição e exclusão)
# ============================================================

@router.put("/projetos/{id_projeto}")
def editar_projeto(id_projeto: int, projeto: Projeto):
    atualizado = dao.editar_projeto(
        id_projeto,
        nome=projeto.nome,
        nivel=projeto.nivel,
        categoria=projeto.categoria,
        descricao=projeto.descricao,
        status=projeto.status
    )
    if not atualizado:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return {"projeto": atualizado}


@router.delete("/projetos/{id_projeto}")
def deletar_projeto(id_projeto: int):
    sucesso = dao.excluir_projeto(id_projeto)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return {"mensagem": "Projeto excluído com sucesso"}


# ============================================================
# 🔹 TECNOLOGIAS (edição e exclusão)
# ============================================================

@router.put("/tecnologias/{id_tecnologia}")
def editar_tecnologia(id_tecnologia: int, tec: Tecnologia):
    atualizado = dao.editar_tecnologia(id_tecnologia, nome=tec.nome)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Tecnologia não encontrada")
    return {"tecnologia": atualizado}


@router.delete("/tecnologias/{id_tecnologia}")
def deletar_tecnologia(id_tecnologia: int):
    sucesso = dao.excluir_tecnologia(id_tecnologia)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Tecnologia não encontrada")
    return {"mensagem": "Tecnologia excluída com sucesso"}


# ============================================================
# 🔹 REPOSITÓRIOS (edição e exclusão)
# ============================================================

@router.put("/repositorios/{id_repositorio}")
def editar_repositorio(id_repositorio: int, repo: Repositorio):
    atualizado = dao.editar_repositorio(id_repositorio, nome=repo.nome)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Repositório não encontrado")
    return {"repositorio": atualizado}


@router.delete("/repositorios/{id_repositorio}")
def deletar_repositorio(id_repositorio: int):
    sucesso = dao.excluir_repositorio(id_repositorio)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Repositório não encontrado")
    return {"mensagem": "Repositório excluído com sucesso"}
