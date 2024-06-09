from flask import Flask, request
import conn
connection = conn.connection


def register():
    dog_name = request.form.get('dog_name')
    tutor = request.form.get('tutor')
    address = request.form.get('address')
    number = request.form.get('number')
    cur = connection.cursor()
    try:
        cur.execute(
            '''INSERT INTO REGISTER (dog_name, tutor, address, number) 
            VALUES (%s, %s, %s, %s)''', (dog_name, tutor, address, number))
        connection.commit()
        cur.close()
        connection.close()
        return 'Cliente cadastrado com sucesso!'
    except:
        return 'falha ao cadastrar, tente novamente!'
