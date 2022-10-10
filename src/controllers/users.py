from fastapi import APIRouter
from src.regras.regras_user import add_user
from src.schemas.user import UserSchema


rota_user = APIRouter(
    prefix="/api/user",
    tags=["Usuários"]
)


@rota_user.post("/")
async def create_user():
    return await add_user