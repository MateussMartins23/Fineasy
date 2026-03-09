from flask import Flask, render_template,url_for
import DB
app = Flask(__name__)

@app.route("/")
def home():
    categorias=DB.listar_categorias()
    mes_aberto=DB.monstrar_mes_aberto()
    

    return render_template("index.html",categorias=categorias,mes_aberto=mes_aberto)



if __name__ == "__main__":
    app.run(debug=True)
    
    