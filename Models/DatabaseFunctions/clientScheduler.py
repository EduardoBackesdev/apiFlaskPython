from flask import request
import Models.Connection.conn as conn
connection = conn.connection


def clientScheduler(tutor):
    connection.cursor()
    try:
        connection.execute(
            '''select * from register where tutor = %s ''', (tutor))
        data = connection.fetchall()
        connection.commit()
        connection.close()
        return data
    except:
        return {"msg": "Erro ao buscar agendamento"}
