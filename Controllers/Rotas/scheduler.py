from flask import Flask, request
import Models.conn as conn
connection = conn.connection


def scheduler():
    tutor = request.form.get('tutor')
    service = request.form.get('service')
    hour = request.form.get('hour')
    cur = connection.cursor()

    if hour < '08:00':
        return {"msg": "Serviço fechado, abriremos as 08:00"}
    elif hour > '14:00':
        return "Serviço fechado, abriremos amanhã as 08:00"
    else:
        cur.execute('''''')
