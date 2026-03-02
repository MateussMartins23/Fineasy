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

def criar_movimentacao(categoria_nome,valor, descricao, data=None):
    con = get_connection()
    cur = con.cursor()
    
    #Obtendo os Ids
    mes_id=obter_mes_atual()
    categoria_id=get_categoria_id(categoria_nome)
    
    
    try:
        if data:
            cur.execute("INSERT INTO movimentacao (mes_id,categoria_id,valor,data,descricao) VALUES (?,?,?,?,?,?)",(mes_id,categoria_id,valor,data,descricao))
        else:
            cur.execute("INSERT INTO movimentacao (mes_id,categoria_id,valor,descricao) VALUES (?,?,?,?,?,?)",(mes_id,categoria_id,valor,descricao))
    except:
        print("Erro ao Criar movimentação.")
            

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
    

def obter_mes_atual():

    con = sqlite3.connect("fin.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")

    hoje = datetime.now()
    mes = hoje.month
    ano = hoje.year

    # Verifica se já existe mês ABERTO
    cur.execute("""
        SELECT id FROM mes
        WHERE mes = ? AND ano = ? AND status = 'ABERTO'
    """, (mes, ano))

    row = cur.fetchone()

    if row:
        con.close()
        return row["id"]
    # Se não existir, cria
    cur.execute("""
        INSERT INTO mes (mes, ano, status)
        VALUES (?, ?, 'ABERTO')
    """, (mes, ano))

    con.commit()
    mes_id = cur.lastrowid
    con.close()

    return mes_id


    
    
    #FECHANDO QUALQUER OUTRO MES ABERTO

############################################## TESTES ##############################################

