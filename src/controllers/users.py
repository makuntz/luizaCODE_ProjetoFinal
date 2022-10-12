from fastapi import APIRouter
from src.regras.regras_user import add_user, get_user, get_everybody
from src.schemas.user import UserSchema


rota_user = APIRouter(
    prefix="/api/user",
    tags=["Usuários"]
)


@rota_user.post("/")
async def create_user(user: UserSchema):
    return await add_user(user)


@rota_user.get("/{email}")
async def find_user(email):
    print(email)
    return await get_user(email)

@rota_user.get("/")
async def trazer_todos():
    return await get_everybody()