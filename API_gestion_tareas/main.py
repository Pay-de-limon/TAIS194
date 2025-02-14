from fastapi import FastAPI,HTTPException
from typing import Optional
app = FastAPI(

    title ="PRACTICA NO.4",
    description= "Repaso",
    version = "1.0.1"
    
)

Tareas =[
    
    {
    "id": 1,
    "titulo": "Diseñar interfaz de usuario",
    "descripcion": "Crear el prototipo de una interfaz para la aplicación.",
    "vencimiento": "20-02-24",
    "estado": "completada",
    "materia": "Diseño de Interfaces"
},
    {
    "id": 2,
    "titulo": "Configurar máquina virtual",
    "descripcion": "Instalar y configurar una máquina virtual en VirtualBox",
    "vencimiento": "22-02-24",
    "estado": "pendiente",
    "materia": "Tecnologías de Virtualización"
},
    {
    "id": 3,
    "titulo": "Revisión de código",
    "descripcion": "Revisar y mejorar el código del proyecto de software",
    "vencimiento": "19-02-24",
    "estado": "completada",
    "materia": "Gestión de Software"
},
    {
    "id": 4,
    "titulo": "Plan de proyecto",
    "descripcion": "Desarrollar el plan de proyecto para la asignatura de Administración de Proyectos",
    "vencimiento": "25-02-24",
    "estado": "pendiente",
    "materia": "Administración de Proyectos"
},
    {
    "id": 5,
    "titulo": "Practicar conversación",
    "descripcion": "Realizar una práctica de conversación en inglés con un compañero de clase",
    "vencimiento": "18-02-24",
    "estado": "pendiente",
    "materia": "Inglés"
},
    {
    "id": 6,
    "titulo": "Examen parcial",
    "descripcion": "Estudiar para el examen parcial de Tecnologías de Virtualización",
    "vencimiento": "24-02-24",
    "estado": "pendiente",
    "materia": "Tecnologías de Virtualización"
}
]
#EndPoint consulta tarea
@app.get("/todasTareas", tags= ["Operaciones CRUD"])
def leer():
    return {'Tareas Registradas': Tareas}

#Ruta o EndPoint POST
@app.post('/Tareas/', tags=["Operaciones CRUD"])
def guardar(usuario: dict):
    for trs in Tareas:
        if trs["id"] == tareas["id"]:
            raise HTTPException(status_code=400, detail="La tarea ya existe")  # Sirve para marcar error
    Tareas.append(tareas)
    return Tareas
#Endpoint para actualizar
@app.put("/usuarios/{id}", tags=['Operaciones CRUD'])
def actualizar(id:int, TareaActualizada:dict):
    for index,trs in enumerate(Tareas):
        if trs["id"]==id:
            Tareas[index].update(TareaActualizada)
            return Tareas[index]
    raise HTTPException(status_code=400, detail="La tarea no existe")

#Endpoint para eliminar
@app.delete("/Tareas/{id}", tags=['Operaciones CRUD'])
def eliminar(id: int):
    for index, trs in enumerate(Tareas):
        if trs["id"] == id:
            del Tareas[index]  
            return {"message": "Tarea Eliminada"}
    raise HTTPException(status_code=400, detail="La tarea no existe")

@app.get('/Tareas/{id}', tags=["Operaciones CRUD"])
def buscar_por_id(id: int):
    for trs in Tareas:
        if trs["id"] == id:
            return trs
    raise HTTPException(status_code=404, detail="No se encontro tareas")


