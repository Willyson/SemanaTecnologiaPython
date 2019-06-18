## ======================
## = Importações do Python
## ======================
from flask import Flask, render_template


app = Flask(__name__)

## ==============================
## = Página inicial da aplicação
## ==============================
@app.route('/')
def index():
    return render_template("login.html")





## ===========================================================================================================
## = Rendenizar a página de cadastro de usuário quando a aplicação for direcionada para paginaCadastroUsuario
## ===========================================================================================================
@app.route('/paginaCadastroUsuario')
def paginaCadastroUsuario():
    return render_template("cadastro.html")






## ========================================
## = Conecta ao banco e realiza o cadastro
## ========================================

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






## =============================
## = Botão de sair da aplicação
## =============================
@app.route('/sair')
def sair():
    return index()






## ===================
## = Consulta Usuário
## ===================
@app.route('/consultaUsuario')
def consultaUsuario():
    return render_template("consultaUsuario.html")




## =================================
## = Inicia a aplicação com o debug
## =================================
if __name__ == '__main__':
    app.run(debug=True)