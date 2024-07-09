from flask import Flask, json
import Models.Connection.conn as conn
connection = conn.connection


def serviceAndPrice():
    services = []
    try:
        cur = connection.cursor() 
        cur.execute('''select service, price from service''')
        data = cur.fetchall()
        for i in data:
            service_dict = {'service': i[0], 'price': i[1]}
            services.append(service_dict)
        cur.close()
        connection.close() 
        return services
    except Exception as a:
        e = str(a)
        return e