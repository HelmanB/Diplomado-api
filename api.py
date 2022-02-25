from fastapi import FastAPI
from classes import ModelInput, ModelOutput, APIModelBackEnd
from metodos import metodos  as m

app = FastAPI(title="API", version="1.0.0")


@app.get("/datos")
def getDatos(): 
    data = m.prepararDatos();
    return data

@app.get("/departamentos")
def getDepartamentos(): 
    data = m.departamentos()
    return data

@app.get("/desercion_transicion")
def getDT(): 
    data = m.desercion_transicion()
    return data

@app.get("/desercion_primaria")
def getDP(): 
    data = m.desercion_primaria()
    return data

@app.get("/desercion_secundaria")
def getDS(): 
    data = m.desercion_secundaria()
    return data

@app.get("/desercion_media")
def getMedia(): 
    data = m.desercion_media()
    return data
