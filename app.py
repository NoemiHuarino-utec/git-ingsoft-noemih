from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/')

def hello():

    return '<h1>Hello, Ana y Noemi :D</h1>'

def sumar(param1, param2):
    resultado = param1 + param2
    return resultado

resultado = sumar(10, 20)
print("Resultado de la suma es: ")
print(resultado)