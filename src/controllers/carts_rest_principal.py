from fastapi import APIRouter

#criando rota principal
rota_principal = APIRouter()

@rota_principal.get("/")
def principal():
    return "Seja bem vinda"
