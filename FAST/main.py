from fastapi import FastAPI 
from DB.conexion import  engine, Base
from models.modelsDB import User 
from routers.usuario  import routerUsuario
from routers.auth import routerAuth


app = FastAPI(
    title="Mi primer API",
    description="Perla Moreno Hurtado",
    version="1.0.1"
)

app.include_router (routerUsuario)
app.include_router(routerAuth)
Base.metadata.create_all(bind=engine)



