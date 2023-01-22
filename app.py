from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')                          # Decorator to catch an event called "my event":
def connect(message):  
    now = datetime.now()
    emit('my response', {'data': ' '.join(list(map(str, [now.year,now.month, now.day, now.hour, now.minute, now.second])))})  

@socketio.on('updateTime')                          # Decorator to catch an event called "my event":
def my_event(message):  
    now = datetime.now()            # test_message() is the event callback function.
    emit('my response', {'data': ' '.join(list(map(str, [now.year,now.month, now.day, now.hour, now.minute, now.second])))})      # Trigger a new event called "my response" 
                                                  # that can be caught by another callback later in the program.

if __name__ == "__main__":
	socketio.run(app)
