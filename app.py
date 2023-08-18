from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/')

def hello():
    return '<h1>Hello, Universe, esto es Feature1!</h1>'

def multiplicar(param1, param2):
    return param1 * param2

param1 = 10
param2 = 20
resultado = multiplicar(param1, param2)
print("La multiplicación de 10 y 20 es:", resultado)

