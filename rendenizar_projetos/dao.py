from database.connection import get_connection


# ============================================================
# 🔹 LISTAR TODOS OS PROJETOS DE UM IDEALIZADOR
# ============================================================
def listar_projetos(id_idealizador: int):
    conexao = get_connection()
    cursor = conexao.cursor()
    
    # 🔍 Filtra os projetos pelo id_idealizador
    cursor.execute("SELECT * FROM projetos WHERE id_idealizador = ?", (id_idealizador,))
    linhas = cursor.fetchall()
    
    conexao.close()

    # 🔄 Transforma cada linha em um dicionário
    return [
        {
            "id": l[0],
            "nome": l[1],
            "id_idealizador": l[2],
            "nivel": l[3],
            "categoria": l[4],
            "descricao": l[5],
            "status": l[6],
        }
        for l in linhas
    ]



# ============================================================
# 🔹 BUSCAR UM ÚNICO PROJETO POR ID
# ============================================================
def buscar_projeto_por_id(id_projeto: int):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM projetos WHERE id = ?", (id_projeto,))
    linha = cursor.fetchone()
    conexao.close()

    if linha:
        return {
            "id": linha[0],
            "nome": linha[1],
            "id_idealizador": linha[2],
            "nivel": linha[3],
            "categoria": linha[4],
            "descricao": linha[5],
            "status": linha[6],
        }
    return None


# ============================================================
# 🔹 LISTAR TECNOLOGIAS
# ============================================================
def listar_tecnologias(id_projeto=None):
    conexao = get_connection()
    cursor = conexao.cursor()
    if id_projeto:
        cursor.execute("SELECT * FROM tecnologias WHERE id_projeto=?", (id_projeto,))
    else:
        cursor.execute("SELECT * FROM tecnologias")
    linhas = cursor.fetchall()
    conexao.close()
    return [
        {"id": l[0], "nome": l[1], "id_projeto": l[2]}
        for l in linhas
    ]


# ============================================================
# 🔹 LISTAR REPOSITÓRIOS
# ============================================================
def listar_repositorios(id_projeto=None):
    conexao = get_connection()
    cursor = conexao.cursor()
    if id_projeto:
        cursor.execute("SELECT * FROM repositorios WHERE id_projeto=?", (id_projeto,))
    else:
        cursor.execute("SELECT * FROM repositorios")
    linhas = cursor.fetchall()
    conexao.close()
    return [
        {"id": l[0], "nome": l[1], "id_projeto": l[2]}
        for l in linhas
    ]
