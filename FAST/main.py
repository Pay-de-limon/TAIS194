from fastapi import FastAPI,HTTPException
from typing import Optional, List
from pydantic import BaseModel
app = FastAPI(

    title ="Mi primer API",
    description= "Perla Moreno Hurtado",
    version = "1.0.1"
)

class modelUsuario(BaseModel):
    id:int 
    nombre:str
    edad:int
    correo:str
    
    
    
    
    
usuarios =[
    {"id":1, "nombre": "Pedro juan", "edad":30,"correo":"pedrojuan10@gmail.com"},
    {"id":2, "nombre": "Panchita", "edad":25, "correo":"panchita35@gmail.com"},
    {"id":3, "nombre": "Patricia", "edad":39, "correo":"patiher@gmail.com"},
    {"id":4, "nombre": "Perla", "edad":20, "correo":"perlam02@gmail.com"}
]

#EndPoint home
@app.get("/", tags= ["Inicio"])
def home():
    return {'hello': 'world FastAPI'}


#EndPoint consulta usuarios
@app.get("/todosUsuarios",response_model= List[modelUsuario], tags= ["Operaciones CRUD"])
def leer():
    return usuarios

#EndPoint POST
@app.post('/usuarios/', response_model=modelUsuario, tags = ["Operaciones CRUD"])
def guardar(usuario:modelUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail = "El usuario ya existe") 
    usuarios.append(usuario)
    return usuario

#Endpoint para actualizar
@app.put("/usuarios/{id}", response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado:modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios[index]= usuarioActualizado.model_dump()
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

