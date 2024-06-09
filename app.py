from flask import Flask, request
import psycopg2
app = Flask(__name__)


connection = psycopg2.connect(
    database='python_Project',
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
)


@app.route("/api/newdog", methods=['POST'])
def HelloWorld():
    dogName = request.form.get('dogName')
    cur = connection.cursor()
    cur.execute(
        '''INSERT INTO DOGS (id, name) VALUES (%s, %s)''', (id, dogName))
    connection.commit()
    cur.close()
    connection.close()
    return 'Dog cadastrado com Sucesso!'


app.run()
