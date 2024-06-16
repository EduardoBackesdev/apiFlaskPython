from flask import request
import Models.conn as conn
connection = conn.connection


def register():
    dog_name = request.form.get('dog_name')
    tutor = request.form.get('tutor')
    address = request.form.get('address')
    number = request.form.get('number')
    connection.cursor()
    try:
        connection.execute(
            '''INSERT INTO REGISTER (dog_name, tutor, address, number) 
            VALUES (%s, %s, %s, %s)''', (dog_name, tutor, address, number))
        connection.commit()
        connection.close()
        return 'Cliente cadastrado com sucesso!'
    except:
        return 'falha ao cadastrar, tente novamente!'
