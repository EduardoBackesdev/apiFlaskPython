from Controllers.Rotas import register
from Controllers.Rotas import serviceAndPrice
from Controllers.Rotas import scheduler
from Controllers.Rotas import clientScheduler


def register_routes(app):
    app.add_url_rule('/api/register', 'register',
                     register.register, methods=['POST'])
    app.add_url_rule('/api/services', 'serviceAndPrice',
                     serviceAndPrice.serviceAndPrice, methods=['GET'])
    app.add_url_rule('/api/scheduler', 'scheduler',
                     scheduler.scheduler, methods=['POST'])
    app.add_url_rule('/api/clientscheduler/<tutor>', 'clientscheduler',
                     clientScheduler.clientScheduler, methods=['GET'])
