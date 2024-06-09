from flask import Flask, request
from Controllers import Routes

app = Flask(__name__)

Routes.register_routes(app)

app.run()
