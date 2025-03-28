
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel 
from genToken import createToken
from DB.conexion import Session, engine, Base
from models.modelsDB import User 
from modelsPydantic import modelUsuario, modelAuth
from middleware import BearerJWT
from fastapi.responses import JSONResponse
from fastapi import APIRouter




routerAuth = APIRouter()

# Endpoint home
@routerAuth.get("/", tags=["Inicio"])
def home():
    return {'hello': 'world FastAPI'}

# Endpoint para generar Token
@routerAuth.post("/auth", tags=['Autentificacion'])
def modelAuth(credenciales: modelAuth):
    if credenciales.correo == "perla@gmail.com" and credenciales.passwd == "12345678":
        token: str = createToken(credenciales.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:   
        return {"Aviso:": "Usuario no Autorizado"}