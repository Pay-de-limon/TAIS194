from pydantic import BaseModel, Field, EmailStr

class modelUsuario(BaseModel):

    name : str = Field(..., min_length=1, max_length=50, description="Solo letras y espacios, minimo 1 y maximo 50")
    age : int = Field(..., ge=0, le=120, description="LA edad debe ser igual o mayor que cero y menor o igual de 120")
    email : EmailStr = Field(..., description="Formato de correo incorrecto, ejemplo: user@example.com")
    
class modelAuth(BaseModel):
    correo : EmailStr
    passwd : str = Field(..., min_length=8, strip_whitespace=True, description="La contraseña es de al menos 8 caracteres")
    
    
    