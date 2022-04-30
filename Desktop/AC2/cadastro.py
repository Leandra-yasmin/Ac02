import os
from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL


app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'aviao'
app.config['MYSQL_DATABASE_DB'] = 'ac2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/index.html', methods=['POST', 'GET'])
def cadastrar():  
        nome = request.form['nome']
        email = request.form['email']
        endereco = request.form['endereco']

        if nome and email and endereco:
            conn = mysql.connect()
            cursor = conn.cursor()

        
            sql = "INSERT INTO tb_users(nome, email, endereco) VALUES (%s, %s, %s)"
            value = (nome, email, endereco)

   
            cursor.execute(sql, value)
            conn.commit()

        return render_template('index.html')


@app.route('/listar', methods=['POST', 'GET'])
def index():
   
    conn = mysql.connect()
    cursor = conn.cursor()


    query = 'SELECT nome, email, endereco FROM tb_users'
    cursor.execute(query)


    data = cursor.fetchall()


    return render_template('listagem.html', data=data)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)