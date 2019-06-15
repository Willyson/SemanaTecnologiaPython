from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")


@app.route('/paginaCadastroUsuario')
def paginaCadastroUsuario():
    return render_template("cadastro.html")


@app.route('/cadastraUsuario')
def cadastraUsuario():
    return "Página python que cadastra usuário"


if __name__ == '__main__':
    app.run(debug=True)