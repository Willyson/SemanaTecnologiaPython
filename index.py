from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")


@app.route('/paginaCadastroUsuario')
def paginaCadastroUsuario():
    return render_template("cadastro.html")


@app.route('/cadastraUsuario', methods=['POST'])
def cadastraUsuario():
    return "Página python que cadastra usuário"



## =====================
## = Validação do login 
## =====================

@app.route('/validaLogin', methods=['POST'])
def validaLogin():
    return homePage()


## ==========
## = Login 
## ==========

@app.route('/homePage')
def homePage():
    return render_template("home.html")


## ========
## = Sair 
## =======

@app.route('/sair')
def sair():
    return index()


## ===================
## = Consulta Usuário
## ===================

@app.route('/consultaUsuario')
def consultaUsuario():
    return render_template("consultaUsuario.html")




if __name__ == '__main__':
    app.run(debug=True)