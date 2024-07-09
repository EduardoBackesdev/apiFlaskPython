from Controllers.HTTP_Routes import postRegister, getServiceAndPrice, getClientScheduler

def register_routes(app):
    app.add_url_rule("/register", "register", postRegister.postRegister, methods=["POST"])
    app.add_url_rule("/services", "services", getServiceAndPrice.getServiceAndPrice(), methods=["GET"])
    app.add_url_rule("/scheduler", "scheduler", getClientScheduler.getClientScheduler, methods=["GET"])