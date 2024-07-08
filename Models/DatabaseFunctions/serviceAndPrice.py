from flask import Flask, json
import Models.Connection.conn as conn
connection = conn.connection


def serviceAndPrice():
    connection.cursor()
    try:
        connection.cursor().execute('''select service, price from service''')
        data = connection.cursor().fetchall() 
        res = [{"service": row[0], "price": row[1]} for row in data]     
        connection.cursor().close()
        connection.close() 
        return json(res)
    except Exception as a:
        e = str(a)
        return e