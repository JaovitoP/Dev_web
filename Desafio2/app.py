
from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)

