# Socket.IO Python 3 Server

## Dependencies (virtualenv needed)
```bash
$ virtualenv venv --python=python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Run server

``` bash
$ python main.py
```

## Cliente side (Vuejs)

`socket.js`
```js
import io from 'socket.io-client'
const socket = io(`http://localhost:5000`)

const webSocket = {
  install (Vue) {
    Vue.prototype.$socket = socket
  }
}

export default webSocket
```

`main.js`
```js
import Vue from 'vue'
import socket from './socket.js'

Vue.use(socket)
```

`MyComponent.vue`
```js
// Somewhere, method, hook, etc...
/**
 * Without namespace
 * Bidirectional
 * Real-time
 * */
setInterval(() => {
  this.$socket.emit('everybody', { says: 'Hi, everybody!' })
}, 5000)
this.$socket.on('metrics', (io) => console.log(io))

// With namespace
const sio = io('http://localhost:5000/chat')
sio.emit('chat message', { data: 'Hello world' })
sio.on('reply', (io) => console.log(io))

```
## Docs
[Github example](https://github.com/miguelgrinberg/python-socketio)

[python-socketio](https://python-socketio.readthedocs.io/en/latest/index.html)

[AIOHTTP](https://aiohttp.readthedocs.io/en/stable/)