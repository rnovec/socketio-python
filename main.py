import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template

sio = socketio.Server()
app = Flask(__name__)


@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('index.hbs')

# with Namespaces
@sio.on('connect', namespace='/chat')
def connect(sid, environ):
    print("connect ", sid)

# send data to specific client
@sio.on('chat message', namespace='/chat')
def message(sid, data):
    sio.emit('reply', {'data': 'foobar'}, namespace='/chat', room=sid)
    print("message ", data)

# without Namespaces, send data to all clients
@sio.on('everybody')
def metrics(sid, metrics):
    from random import random
    sio.emit('metrics', { 'metrics': random() })
    print("message ", metrics)

# listen disconnections
@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
