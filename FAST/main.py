from fastapi import FastAPI

app = FastAPI()

#ruta o EndPoints
@app.get("/")
def main():
    return {"Hello":"¡World FastAPI!"}