from flask import Flask
import Models.conn as conn
connection = conn.connection


def serviceAndPrice():
    cur = connection.cursor()
    try:
        cur.execute('''select a.service, b.price from service a
                    inner join price b on (a.price = b.id_price)  ''')
        data = cur.fetchall()
        connection.commit()
        cur.close()
        connection.close()
        return data
    except:
        return {"msg": "Erro, tente mais tarde!"}
