import sqlite3
from datetime import datetime

def get_connection():
    con = sqlite3.connect("./Backend/fin.db")
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON;")
    return con

def init_DB():
    con = get_connection()
    cur = con.cursor()
    
    try:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS mes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mes INTEGER NOT NULL,
            ano INTEGER NOT NULL,
            status TEXT NOT NULL,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(mes, ano)
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS categoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS movimentacao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mes_id INTEGER NOT NULL,
            categoria_id INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            valor REAL NOT NULL,
            data DATE NOT NULL,
            descricao TEXT,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (mes_id) REFERENCES mes(id),
            FOREIGN KEY (categoria_id) REFERENCES categoria(id)
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS resumo_mensal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mes_id INTEGER NOT NULL UNIQUE,
            total_entradas REAL,
            total_saidas REAL,
            total_investimento REAL,
            saldo REAL,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (mes_id) REFERENCES mes(id)
        );
        """)
    except con.DatabaseError as erro:
        print("Erro ao inicializar o banco de dados:", erro)
    finally:
        if con:
            con.close()
    

################################ CRIAR MOVIMENTAÇÂO #####################################
from datetime import date

def criar_movimentacao(categoria_nome, valor, descricao, data=None):
    con = get_connection()
    cur = con.cursor()

    mes_id = obter_mes_atual()
    categoria_id = get_categoria_id(categoria_nome)
    tipo = get_tipo(categoria_id)
    if data is None:
        data = date.today()

    try:
        cur.execute(
            "INSERT INTO movimentacao (mes_id,categoria_id,tipo,valor,data,descricao) VALUES (?,?,?,?,?,?)",
            (mes_id,categoria_id,tipo,valor,data,descricao)
        )

        con.commit()

    except Exception as e:
        print("Erro ao criar movimentação:", e)

    finally:
        con.close()

def listar_movimentacoes():
    con=get_connection()
    con.row_factory = sqlite3.Row
    cur=con.cursor()

    try:
        cur.execute("""SELECT id,tipo,descricao,data,valor FROM movimentacao""")
        rows=cur.fetchall()

        return rows
    
    except Exception as e:
        print("Erro ao buscar as movimentações", e)
    finally:
        con.close()


def del_mov(mov_id):
    con=get_connection()
    cur=con.cursor()

    try:
        cur.execute('''DELETE FROM movimentacao WHERE id=?''',(mov_id,))

        con.commit()
    except Exception as e:
        print("Erro ao deletar movimentação",e)
        
    finally:
        con.close()





#*****************************CATEGORIA*****************************#
def get_categoria_id(categoria):
    con = get_connection()
    cur = con.cursor()
    
    cur.execute('''SELECT id FROM categoria
                   WHERE nome=? ''',(categoria,))
    row=cur.fetchone()
    return row[0] if row else None
    
def criar_categoria(nome,tipo):
    con=get_connection()
    cur=con.cursor()
    
    try:
        cur.execute("INSERT INTO categoria (nome,tipo) VALUES (?,?)",(nome,tipo,))
        con.commit()
    except Exception as e:
        print("Erro",e)
    finally:
        con.close()
def get_tipo(categoria_id):
    con=get_connection()    
    cur=con.cursor()
    
    try:    
        cur.execute("SELECT tipo FROM categoria WHERE id=?",(categoria_id,))
        row=cur.fetchone()
        return row[0] if row else None
    except Exception as e:
        print("Erro ao buscar o tipo da categoria", e)
        return None
    finally:
        con.close()
    
      

def listar_categorias():
    entradas=[]
    saidas=[]
    investimentos=[]
    
    con = get_connection()
    cur = con.cursor()
    
    categorias = []
    
    try:
        cur.execute("""
        SELECT nome, tipo 
        FROM categoria
        """)
    
        rows = cur.fetchall()
    #MELHORAR O MÉTODO DE IMPRESSÃO DPS
        for row in rows:
            categorias.append(row['nome'])

                  
        return categorias
    except Exception as e: 
        print("Erro", e)
        
    finally:
        con.close()

    
#Manejamento dos MESES
def iniciar_meses(ano):
    con = get_connection()
    cur = con.cursor()
    
    for mes in range(1,13):
        try:
            cur.execute("INSERT INTO mes (mes,ano,status) VALUES(?,?,?)",(mes,ano,'FECHADO'))
        except:
            pass
        
    con.commit()
    con.close()
    
    
def obter_nome_mes(numero):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", 
        "Maio", "Junho", "Julho", "Agosto", 
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    # Verificamos se o número está no intervalo de 1 a 12
    if numero>=1 and numero<=12:
        return meses[numero - 1] # -1 porque listas começam no índice 0
    else:
        return "Mês inválido"

# Exemplo de uso:
# # Saída: Maio

def obter_mes_atual():
    con = sqlite3.connect("./Backend/fin.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    hoje = datetime.now()
    mes = hoje.month
    ano = hoje.year

    # procura o mês
    cur.execute(
        "SELECT id, status FROM mes WHERE mes=? AND ano=?",
        (mes, ano)
    )
    row = cur.fetchone()
    if row:
        # se estiver fechado, abre
        if row["status"] == "FECHADO":
            cur.execute(
                "UPDATE mes SET status='ABERTO' WHERE id=?",
                (row["id"],)
            )
            con.commit()

        con.close()
        return row["id"]
    # se não existir cria
    cur.execute(
        "INSERT INTO mes (mes, ano, status) VALUES (?, ?, 'ABERTO')",
        (mes, ano)
    )
    con.commit()
    mes_id = cur.lastrowid
    con.close()

    return mes_id


def abrir_mes(mes, ano):
    con = get_connection()
    cur = con.cursor()
    con.row_factory = sqlite3.Row
    try:
        cur.execute(
            '''UPDATE mes 
               SET status = ?
               WHERE mes = ? AND ano = ?''',
            ('ABERTO', mes, ano)
        )
        con.commit()

    except Exception as e:
        print("Erro ao abrir o mês:", e)

    finally:
        con.close()
    
def monstrar_mes_aberto():
    con=get_connection()
    cur=con.cursor()


    cur.execute('''SELECT mes FROM mes WHERE status='ABERTO' ''')
    nome=cur.fetchall()
    obter_nome_mes(nome[0]["mes"])

    return obter_nome_mes(nome[0]["mes"])

#############################################MOVIMENTAÇÕES#########################################

############################################# TESTES ##############################################


def limpar_categorias():
    con=get_connection()
    cur=con.cursor()
    
    try:
        for categoria in listar_categorias():
            cur.execute('''DELETE FROM categoria WHERE nome=?''',(categoria,))
            con.commit()
    except Exception as e:
        print("erro ao remover categoria",e)
    finally:
        con.close()
        
def resumo_mensal():
    con = get_connection()    
    cur = con.cursor()

    cur.execute('''
        SELECT 
        SUM(CASE WHEN tipo='entrada' THEN valor ELSE 0 END) AS total_entradas,
        SUM(CASE WHEN tipo='saida' THEN valor ELSE 0 END) AS total_saidas,
        SUM(CASE WHEN tipo='investimento' THEN valor ELSE 0 END) AS total_investimentos,

        SUM(CASE WHEN tipo='entrada' THEN valor ELSE 0 END) -
        (
            SUM(CASE WHEN tipo='saida' THEN valor ELSE 0 END) +
            SUM(CASE WHEN tipo='investimento' THEN valor ELSE 0 END)
        ) AS saldo_final
        
        FROM movimentacao
        WHERE mes_id=?
    ''', (obter_mes_atual(),))

    row = cur.fetchone()

    return row

