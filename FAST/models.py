from pydantic import BaseModel, Field

class modelUsuario(BaseModel):
    id:int = Field(...,gt=0,description="Id siempre debe ser positivo")
    nombre:str= Field(..., min_length=1, max_length=85, description="solo letras y espacios min 1 max 85")
    edad:int= Field(...,gt=0,le=120, description="Edad siempre tiene que ser mayor a cero")
    correo:str= Field(...,description="Ingrese un Email valido", pattern=r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,6}$')
    
class modelUsuario(BaseModel):
    mail:EmailStr = Field(...,description="Correo válido")
    passw:str = Field(...,min_length=8, strip_whitespace= True ,description=" solo letras sin espacios min 8")
    