from fastapi import FastAPI, HTTPException, Depends
from typing import List
from pydantic import BaseModel


app = FastAPI()


class ModelVehiculo(BaseModel):
    id: int
    modelo: str
    marca: str
    año: int


vehiculos = [
    {"id": 1, "modelo": "Corolla", "placa": "FGSIAS", "año": 2020},
    {"id": 2, "modelo": "Civic", "placa": "DHWFS", "año": 2021},
    {"id": 3, "modelo": "Sentra", "placa": "Nissan", "año": 2019}
]





@app.get("/todosVehiculos", tags= ["Operaciones CRUD"])
def leer():
    return {'Vehiculos Registrados': vehiculos}



@app.post('/vehiculos/', response_model=ModelVehiculo, tags=["Operaciones CRUD"])
def guardar_vehiculo(vehiculo: ModelVehiculo):
    for v in vehiculos:
        if v["id"] == vehiculo.id:
            raise HTTPException(status_code=400, detail="El vehículo ya existe")
    vehiculos.append(vehiculo.dict())
    return vehiculo


@app.put("/vehiculos/{id}", response_model=ModelVehiculo, tags=["Operaciones CRUD"])
def actualizar_vehiculo(id: int, vehiculo_actualizado: ModelVehiculo):
    for index, v in enumerate(vehiculos):
        if v["id"] == id:
            vehiculos[index] = vehiculo_actualizado.dict()
            return vehiculos[index]
    raise HTTPException(status_code=400, detail="El vehículo no existe")