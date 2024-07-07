from flask import request
import Models.Connection.conn as conn
connection = conn.connection


def register():
    dog_name = request.form.get('dog_name')
    tutor = request.form.get('tutor')
    address = request.form.get('address')
    number = request.form.get('number')
    connection.cursor()
    try:
        connection.cursor().execute(
            '''INSERT INTO CLIENTS (dog_name, tutor, address, number) 
            VALUES (%s, %s, %s, %s)''', (dog_name, tutor, address, number))
        connection.commit()
        connection.cursor().close()
        connection.close()
        return 'Cliente cadastrado com sucesso!'
    except Exception as a:
        e = str(a)
        print(e)
        return 'falha ao cadastrar, tente novamente!'
