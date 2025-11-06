# crud.py
from database.connection import get_connection

# ============================================================
# 🔹 PROJETOS
# ============================================================

def editar_projeto(id_projeto, nome=None, nivel=None, categoria=None, descricao=None, status=None):
    conexao = get_connection()
    cursor = conexao.cursor()
    
    # Busca projeto atual
    cursor.execute("SELECT * FROM projetos WHERE id=?", (id_projeto,))
    projeto = cursor.fetchone()
    if not projeto:
        conexao.close()
        return None

    # Atualiza somente os campos fornecidos
    novo_nome = nome or projeto[1]
    novo_nivel = nivel or projeto[3]
    nova_categoria = categoria or projeto[4]
    nova_descricao = descricao or projeto[5]
    novo_status = status or projeto[6]

    cursor.execute(
        "UPDATE projetos SET nome=?, nivel=?, categoria=?, descricao=?, status=? WHERE id=?",
        (novo_nome, novo_nivel, nova_categoria, nova_descricao, novo_status, id_projeto)
    )
    conexao.commit()
    conexao.close()
    return {
        "id": id_projeto,
        "nome": novo_nome,
        "id_idealizador": projeto[2],
        "nivel": novo_nivel,
        "categoria": nova_categoria,
        "descricao": nova_descricao,
        "status": novo_status
    }

def excluir_projeto(id_projeto):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM projetos WHERE id=?", (id_projeto,))
    conexao.commit()
    conexao.close()
    return True


# ============================================================
# 🔹 TECNOLOGIAS
# ============================================================

def editar_tecnologia(id_tecnologia, nome=None):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tecnologias WHERE id=?", (id_tecnologia,))
    tec = cursor.fetchone()
    if not tec:
        conexao.close()
        return None
    novo_nome = nome or tec[1]
    cursor.execute("UPDATE tecnologias SET nome=? WHERE id=?", (novo_nome, id_tecnologia))
    conexao.commit()
    conexao.close()
    return {"id": id_tecnologia, "nome": novo_nome, "id_projeto": tec[2]}

def excluir_tecnologia(id_tecnologia):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tecnologias WHERE id=?", (id_tecnologia,))
    conexao.commit()
    conexao.close()
    return True


# ============================================================
# 🔹 REPOSITÓRIOS
# ============================================================

def editar_repositorio(id_repositorio, nome=None):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM repositorios WHERE id=?", (id_repositorio,))
    repo = cursor.fetchone()
    if not repo:
        conexao.close()
        return None
    novo_nome = nome or repo[1]
    cursor.execute("UPDATE repositorios SET nome=? WHERE id=?", (novo_nome, id_repositorio))
    conexao.commit()
    conexao.close()
    return {"id": id_repositorio, "nome": novo_nome, "id_projeto": repo[2]}

def excluir_repositorio(id_repositorio):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM repositorios WHERE id=?", (id_repositorio,))
    conexao.commit()
    conexao.close()
    return True
