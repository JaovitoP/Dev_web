import mysql.connector

config = {
        'user': 'root',
        'password': 'root',
        'host': 'mysql',
        'port': '3306',
        'database': 'db'
    }

db = mysql.connector.connect(**config)

def adicionar_contato(email, assunto, descricao):
    """Adiciona um contato a base de dados
    """
    cursor = db.cursor(buffered=True)
    cursor.execute(f"INSERT INTO contatos(email, assunto, descricao) VALUES ('{email}', '{assunto}', '{descricao}')")

    db.commit()

    cursor.close()

def selecionar_usuarios():
    cursor = db.cursor(buffered=True)
    users = cursor.execute("SELECT * FROM contatos")
    userDetails = cursor.fetchall()
    return userDetails