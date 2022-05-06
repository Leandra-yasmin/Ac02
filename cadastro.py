from ast import Str
import re
from flask import Flask,jsonify,abort, render_template
from flask import make_response, request, url_for
from flaskext.mysql import MySQL


app = Flask(__name__)
#app.url_map.strict_slashes = False


mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Aviao10072019'
app.config['MYSQL_DATABASE_DB'] = 'ac2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')


@app.route('/cadastrar', methods=["GET","POST"])
def cadastrar():
    _name = request.form['nome']
    _email = request.form['email']
    _endereco = request.form['endereco']
    if _name and _email and _endereco:
        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "INSERT INTO aluno(nome, email, endereco) VALUES (%s, %s, %s)"
        value = (_name, _email, _endereco)
        cursor.execute(sql, value)
        conn.commit()

    
 
    return render_template('index.html')

@app.route('/listar', methods=['GET'])
def listar():
    dados = []
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = 'SELECT nome, email, endereco FROM aluno'
    cursor.execute(sql)
    for usuario in cursor.fetchall():
        dados.append(usuario)
    return render_template('listagem.html', dados=dados)



if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5000)