from flask import Flask
import Models.Connection.conn as conn
connection = conn.connection


def serviceAndPrice():
    try:
        connection.cursor().execute('''select a.service, b.price from service''')
        data = connection.cursor().fetchall()
        a = print (data)
        connection.commit()
        connection.cursor().close()
        connection.close()
        dados = []
        for row in data:
            dados.append(dict(row))   
        print(dados)
        return dados
    except:
        return {"msg": "Erro, tente mais tarde!"}


serviceAndPrice()