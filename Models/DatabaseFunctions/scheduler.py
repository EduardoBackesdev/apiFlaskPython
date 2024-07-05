from flask import Flask, request
import Models.Connection.conn as conn
connection = conn.connection
# inserir os dados com o valor do ID referente a foreign key, depois fazer o select com inner join
# mandar os valores corretos pelo frontend!


def scheduler():
    tutor = request.form.get('tutor')
    service = request.form.get('service')
    hour = request.form.get('hour')
    day = request.form.get('day')
    connection.cursor()

    if hour < '08:00':
        return {"msg": "Serviço fechado, abriremos as 08:00"}
    elif hour > '16:00':
        return {"msg": "Serviço fechado, abriremos amanhã as 08:00"}
    else:
        try:
            connection.execute('''INSERT INTO SCHEDULER(tutor, service, hour, day) values 
                    (%s,%s,%s,%s)''', (tutor, service, hour, day))
            connection.commit()
            connection.close()
            return {"msg": "Horario marcado com sucesso!"}
        except:
            return {"msg": "Erro ao marcar horario!"}
