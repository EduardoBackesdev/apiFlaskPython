from flask import request
import Models.conn as conn
connection = conn.connection


def clientScheduler():
    tutor = request.args.get('tutor')
    connection.cursor()
    try:
        connection.execute(
            '''select a.tutor, b.dog_name, a.service, 
            a."hour", a."day" from scheduler a
            inner join register b on (a.tutor = b.tutor)
            where a.tutor = {tutor}''')
        connection.commit()
        connection.close()
        return {"msg": "Sucesso ao buscar agendamento"}
    except:
        return {"msg": "Erro ao buscar agendamento"}
