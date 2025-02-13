from fastapi import FastAPI,HTTPException
from typing import Optional
app = FastAPI(

    title ="Mi primer API",
    description= "Perla Moreno Hurtado",
    version = "1.0.1"
)

usuarios =[
    {"id":1, "nombre": "Pedro juan", "edad":30},
    {"id":2, "nombre": "Panchita", "edad":25},
    {"id":3, "nombre": "Patricia", "edad":39},
    {"id":4, "nombre": "Perla", "edad":20}
]

#EndPoint home
@app.get("/", tags= ["Inicio"])
def home():
    return {'hello': 'world FastAPI'}


#EndPoint consulta usuarios
@app.get("/todosUsuarios", tags= ["Operaciones CRUD"])
def leer():
    return {'Usuarios Registrados': usuarios}

#Ruta o EndPoint POST
@app.post('/usuarios/', tags = ["Operaciones CRUD"])
def guardar(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail = "El usuario ya existe") #Sirve para marcar error
    usuarios.append(usuario)
    return usuario

#Endpoint para actualizar
@app.put("/usuarios/{id}", tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")

#Endpoint para eliminar
@app.delete("/usuarios/{id}", tags=['Operaciones CRUD'])
def eliminar(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            del usuarios[index]  
            return {"message": "Usuario eliminado"}
    raise HTTPException(status_code=400, detail="El usuario no existe")

