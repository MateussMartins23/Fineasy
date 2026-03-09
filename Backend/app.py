from flask import Flask, render_template,url_for,request,redirect
import DB
app = Flask(__name__)

@app.route("/")
def home():
    categorias=DB.listar_categorias()
    mes_aberto=DB.monstrar_mes_aberto()
    rows=DB.listar_movimentacoes()
    return render_template("index.html",categorias=categorias,mes_aberto=mes_aberto,rows=rows)

@app.route('/nova_mov',methods=['POST'])
def nova_mov():
    categoria=request.form['categoria']
    valor=request.form['valor']
    descricao=request.form['descricao']

    DB.criar_movimentacao(categoria,valor,descricao)

    
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
    
    