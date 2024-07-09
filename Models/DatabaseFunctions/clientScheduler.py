from flask import request
import Models.Connection.conn as conn
connection = conn.connection


def clientScheduler():
    cur = connection.cursor()
    tutor = request.form.get("tutor")
    clientes = []
    try:
        cur.execute(
            '''select dog_name, tutor, address, number from clients where tutor = %s''', (tutor,))
        data = cur.fetchall()
        for i in data:
            clientes_dict = {'dog_name': i[0], 'tutor': i[1], 'address':i[2], 'number':i[3]}
            clientes.append(clientes_dict)
        cur.close()     
        connection.close()
        return clientes
    except Exception as a:
        e = str(a)
        print(e)
        return {"msg": "Erro ao buscar agendamento"}
