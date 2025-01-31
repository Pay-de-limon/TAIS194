from fastapi import FastAPI
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

#EndPoint promedio
@app.get("/promedio", tags=['Mi calificación'])
def promedio():
    return 10.5 

#EndPoint con parametro opcional
@app.get("/usuario2/{id}", tags=['Endponit parametro 0bligatorio'])
def consultaUsuario2(id: Optional[int]=None):
    if id  is not None: #validar si viene el ID
        for usuario in usuarios:
            if usuario["id"] == id:
                return{"mensaje": "usuario encntrado","El usuario es": usuario}
            
        return {"mensaje": f"No se encontro el id: {id}"}    
    
    return{"mensaje": "No se proporciono un Id"}

def consultaUsuario(id : int):
    #caso ficticio de búsqueda en BD
    return {"Se encontro el usuario": id}


#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}