from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    with app.app_context():
        from . import routes
        socketio.init_app(app)
        return app
