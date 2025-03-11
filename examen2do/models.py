
    
class modelVehiculo(BaseModel):
    año : int = Field(..., min_length=1, max_length=4, description="Solo letras y espacios, minimo 1 y maximo 50")
    
    