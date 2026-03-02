from flask import Flask, render_template,url_for
import DB
app = Flask(__name__)

@app.route("/")
def home():
    categorias=DB.listar_categorias()
    return render_template("index.html",categorias=categorias)



if __name__ == "__main__":
    app.run(debug=True)
    
    