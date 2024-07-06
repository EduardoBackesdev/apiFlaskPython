from Controllers.HTTP_Routes import postRegister
def register_routes(app):
    app.add_rule("/register", "register", postRegister.postRegister, methods=["POST"])