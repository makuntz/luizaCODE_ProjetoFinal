from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def rota_principal():
    return "Seja bem-vinda"
