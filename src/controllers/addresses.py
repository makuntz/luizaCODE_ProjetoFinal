from pymongo import MongoClient
from fastapi import APIRouter, FastAPI
from src.regras.regras_address import add_address
from src.schemas.cart import CartSchema


rota_address = APIRouter(
    prefix="/api/address",
    tags=["Addresses"]
)


@rota_address.post("/{id_user}")
async def address_crud():
    return await add_address()




    

