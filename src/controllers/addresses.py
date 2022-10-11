from pymongo import MongoClient
from fastapi import APIRouter, FastAPI
from src.regras.regras_address import adding_address, deleting_address, search_address
from src.schemas.cart import CartSchema


rota_address = APIRouter(
    prefix="/api/address",
    tags=["Addresses"]
)


@rota_address.post("/{id_user}")
async def address_inserted():
    return await adding_address()

@rota_address.get("/{email}")
async def address_researched():
    return await search_address()


##opcional
@rota_address.delete("/{}")
async def address_deleted():
    return deleting_address




    

