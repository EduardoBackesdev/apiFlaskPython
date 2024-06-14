from Controllers.Rotas import register
from Controllers.Rotas import serviceAndPrice


def register_routes(app):
    app.add_url_rule('/api/register', 'register',
                     register.register, methods=['POST'])
    app.add_url_rule('/api/services', 'serviceAndPrice',
                     serviceAndPrice.serviceAndPrice, methods=['GET'])
