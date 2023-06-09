from flask import Flask, render_template, request, url_for, jsonify
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


# conexão com o banco de dados
app.config['MYSQL_Host'] = 'localhost' # 127.0.0.1
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'dev951753'
app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL(app)


@app.route("/")
def index():
  return render_template('index.html')

@app.route("/index.html")
def home():
  return render_template('index.html')

@app.route("/contato.html")
def contato():
  return render_template('contato.html')

@app.route("/quemsomos.html")
def quemsomos():
  return render_template('quemsomos.html')

@app.route('/contatos', methods=['GET', 'POST'])
def contatos():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
       
        mysql.connection.commit()
        
        cur.close()

        return 'sucesso'
    return render_template('contatos.html')


# rota usuários para listar todos os usuário no banco de dados.
@app.route('/users.html')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contatos")

    if users > 0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails)
