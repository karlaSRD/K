# -*- coding: utf-8 -*-
from flask import Flask

app=Flask(__name__)

@app.route("/sumar/<int:num1>/<int:num2>")
def sumar(num1, num2):
    resultado = num1 + num2
    return f"Resultado de la suma: {resultado} "
  
  @app.route("/restar/<int:num1>/<int:num2>")
def restar(num1, num2):
    resultado = num1 - num2
    return f"Resultado de la resta: {resultado}"

@app.route("/dividir/<int:num1>/<int:num2>")
def dividir(num1, num2):
resultado = num1 / num2
return f"Resultado de la división: {resultado}"

if __name__=="__main__":
  app.run()
