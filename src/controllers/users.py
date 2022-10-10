from fastapi import APIRouter
from src.regras.regras_user import add_user
from src.regras.regras_user import get_user
from src.schemas.user import UserSchema


rota_user = APIRouter(
    prefix="/api/user",
    tags=["Usuários"]
)


@rota_user.post("/")
async def create_user():
    return await add_user()

@rota_user.get("/{email}")
async def find_user(email: str):
    print("To entrando pela rota, email: ", email)
    user = await get_user(email)
    print("To indo pro retorno final, user: ", user)
    return user
