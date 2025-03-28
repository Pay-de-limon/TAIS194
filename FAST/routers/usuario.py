from fastapi import FastAPI, HTTPException, Depends
from typing import Optional, List
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel 
from modelsPydantic import modelUsuario, modelAuth
from genToken import createToken
from DB.conexion import Session, engine, Base
from models.modelsDB import User 

from middleware import BearerJWT
from fastapi.responses import JSONResponse
from fastapi import APIRouter

routerUsuario = APIRouter()

# Endpoint consulta usuarios
@routerUsuario.get("/todosUsuarios", tags=["Operaciones CRUD"])
def leer():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al guardar", "Error": str(e)})
    finally:
        db.close()

# Endpoint POST ACTUALIZADO
@routerUsuario.post('/usuarios/', response_model=modelUsuario, tags=["Operaciones CRUD"])
def guardar(usuario: modelUsuario):
    db = Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"message": "Usuario Guardado", "usuario": usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al guardar", "Error": str(e)})
    finally:
        db.close()

# Endpoint para actualizar
@routerUsuario.put("/usuarios/{id}", response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id: int, usuarioActualizado: modelUsuario):
    db = Session()
    try:
    
        usuario_db = db.query(User).filter(User.id == id).first()
        
        
        if not usuario_db:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        
        for key, value in usuarioActualizado.dict().items():
            setattr(usuario_db, key, value)
        
        db.commit()  
        return JSONResponse(status_code=200, content={"message": "Usuario actualizado", "usuario": usuarioActualizado.model_dump()})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al actualizar", "Error": str(e)})
    
    finally:
        db.close()

# Endpoint para eliminar
@routerUsuario.delete("/usuarios/{id}", tags=['Operaciones CRUD'])
def eliminar(id: int):
    db = Session()
    try:
    
        usuario_db = db.query(User).filter(User.id == id).first()
        
        
        if not usuario_db:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
    
        db.delete(usuario_db)
        db.commit() 
        
        return {"message": "Usuario eliminado"}
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al eliminar", "Error": str(e)})
    
    finally:
        db.close()

# Endpoint para buscar por ID
@routerUsuario.get('/usuario/{id}', tags=['Operaciones CRUD'])
def leeruno(id: int):
    db = Session()
    try:
        consulta1 = db.query(User).filter(User.id == id).first()
        if not consulta1:
            return JSONResponse(status_code=404, content={"Mensaje": "Usuario no encontrado"})
        
        return JSONResponse(content=jsonable_encoder(consulta1))
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "No fue posible consultar", "Error": str(e)})
    
    finally:
        db.close()
