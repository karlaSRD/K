# -*- coding: utf-8 -*-
pandas
openpyxl
import pandas as pd
from flask import Flask

app=Flask(__name__)

base=pd.read_excel("Coreanos.xlsx")

@app.router("/")
def Principal():
  return "Esta es una API sobre actores, actrices y cantantes coreanos"

@app.router("Por_Edad/<Edad>")
def  PorEdad(Edad):
  Edad=int(Edad)
  fila=base[base["Edad"]==Edad]
  respuesta=f"Los corean@s de {Edad} años son  {fila.loc[:,'Edad']}"
  return respuesta

@app.router("/Por_Genero/<Genero>")
  def PorGenero(Genero):
    resultados=base[base["Genero"]==Genero]
    resultados=str (resultados)
    return resultados

@app.router("/Por_Profesion/<Profesion>")
  def PorProfesion(Profesion):
    resultados=base[base["Profesion"]==Profesion]
    resultados=str (resultados)
    return resultados

@app.router("/Por_Rango_Edad/<Edad1>/<Edad2>")
def  PorRangoEdad(Edad1,Edad2):
    Edad1=int(Edad1)
    Edad2=int(Edad2)
    Actores_por_rango=base[(base["Edad"]>Edad1) & (base["Edad"]<Edad2)]
    resultados=f"Los actores con edades entre {Edad1} y {Edad2} años son: {fila.loc [:,'Actores_por_rango']}"
    return resultados

if__name__=="__main__":
  app.run()
