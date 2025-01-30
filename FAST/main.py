from fastapi import FastAPI

app = FastAPI()

#EndPoint promedio
@app.get("/")
def home():
    return {'hello': 'world FastAPI'}

#EndPoint promedio
@app.get("/promedio")
def promedio():
    return 10.5 

#EndPoint con parametro obligatorio
@app.get("/usuario/{id}")

def consultaUsuario(id : int):
    #caso ficticio de búsqueda en BD
    return {"Se encontro el usuario": id}