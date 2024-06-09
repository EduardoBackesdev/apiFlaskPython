from Controllers.Rotas import register


def register_routes(app):
    app.add_url_rule('/api/register', 'register',
                     register.register, methods=['POST'])
