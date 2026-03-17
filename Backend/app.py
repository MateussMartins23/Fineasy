from flask import Flask, render_template,url_for,request,redirect,jsonify
import DB
app = Flask(__name__)

@app.route("/")
def home():
    categorias=DB.listar_categorias()
    mes_aberto=DB.monstrar_mes_aberto()
    rows=DB.listar_movimentacoes()
    row_resumo=DB.resumo_mensal()
    
    return render_template("index.html",categorias=categorias,mes_aberto=mes_aberto,rows=rows,row_resumo=row_resumo)

@app.route('/nova_mov',methods=['POST'])
def nova_mov():
    categoria=request.form['categoria']
    valor=request.form['valor']
    descricao=request.form['descricao']

    DB.criar_movimentacao(categoria,valor,descricao)

    
    return redirect(url_for('home'))

@app.route('/delete_mov',methods=['POST'])
def del_mov():
    mov_id=request.form['id']
    DB.del_mov(mov_id)

    return redirect(url_for('home'))

@app.route("/dados")
def dados():
    row=DB.resumo_mensal()
    return jsonify([row['total_entradas'],row["total_saidas"],row['total_investimentos']])

if __name__ == "__main__":
    app.run(debug=True)
    
    