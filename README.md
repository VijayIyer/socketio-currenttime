## Purpose - playing around with flask-socketio
### Web Sockets can be used for 2 way communication between server and client, thus making it possible to get live updates in the client without user action. 

### Details
A simple flask app which updates current time at regular intervals

To run the app, open a terminal and create a conda environment or virtualenv
1. conda create -n socketio-currenttime-env python=3.9
2. virtualenv venv

Then install required packages using `pip install -r requirements.txt`

Then launch app using `flask run --debugger --reload`
Open a browser and type in the url - e.g. http://127.0.0.1:5000

![image](https://user-images.githubusercontent.com/20140754/213925843-2e5be9c1-a3a8-4e99-a0a7-c998b4863001.png)

Another flask-socketio app which is easy to understand but covers more features - https://github.com/miguelgrinberg/Flask-SocketIO-Chat
