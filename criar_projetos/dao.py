from database.connection import get_connection

def criar_projeto(nome, id_idealizador, nivel, categoria, descricao, status):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO projetos (nome, id_idealizador, nivel, categoria, descricao, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, id_idealizador, nivel, categoria, descricao, status))
    conexao.commit()
    projeto_id = cursor.lastrowid
    conexao.close()
    return {
        "id": projeto_id,
        "nome": nome,
        "id_idealizador": id_idealizador,
        "nivel": nivel,
        "categoria": categoria,
        "descricao": descricao,
        "status": status
    }

def adicionar_tecnologia(nome, id_projeto):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO tecnologias (nome, id_projeto) VALUES (?, ?)",
        (nome, id_projeto)
    )
    conexao.commit()
    tech_id = cursor.lastrowid
    conexao.close()
    return {"id": tech_id, "nome": nome, "id_projeto": id_projeto}

def adicionar_repositorio(nome, id_projeto):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO repositorios (nome, id_projeto) VALUES (?, ?)",
        (nome, id_projeto)
    )
    conexao.commit()
    repo_id = cursor.lastrowid
    conexao.close()
    return {"id": repo_id, "nome": nome, "id_projeto": id_projeto}
