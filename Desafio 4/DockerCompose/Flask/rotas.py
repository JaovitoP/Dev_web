from app import *
from db import adicionar_contato, selecionar_usuarios

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/quemsomos.html')
def quemsomos():
    return render_template('quemsomos.html')


@app.route('/contato.html', methods=["POST", "GET"])
def contato():
    if request.method == "POST":
        email = request.form["email"]
        assunto = request.form["assunto"]
        descricao = request.form["descricao"]

        adicionar_contato(email=email, assunto=assunto, descricao=descricao)

        return "Sucesso"
    return render_template('contato.html')

@app.route("/users.html")
def users():
    userDetails = selecionar_usuarios()
    return render_template("users.html", userDetails=userDetails)
