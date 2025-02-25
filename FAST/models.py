from pydantic import BaseModel, Field

class modelUsuario(BaseModel):
    id:int = Field(...,gt=0,description="Id siempre debe ser positivo")
    nombre:str= Field(..., min_length=1, max_length=85, description="solo letras y espacios min 1 max 85")
    edad:int= Field(...,gt=0,le=120, description="Edad siempre tiene que ser mayor a cero")
    correo:str= Field(...,description="Ingrese un Email valido", pattern=r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,6}$')
    
