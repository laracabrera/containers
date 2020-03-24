#!/usr/bin/python
# coding: latin-1

import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hola! Flask se esta ejecutando en {}".format(socket.gethostname())


if __name__ == '__main__':
    # Es necesario especificar el parametro host para que el servidor pueda recibir peticiones desde fuera del contenedor
    app.run(host='0.0.0.0')
