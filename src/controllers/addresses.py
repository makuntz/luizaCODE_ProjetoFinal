from pymongo import MongoClient
from fastapi import APIRouter, FastAPI
from src.regras.regras_address import creating_address, search_address
from src.schemas.cart import CartSchema


rota_address = APIRouter(
    prefix="/api/address",
    tags=["Addresses"]
)


@rota_address.post("/{email}")
async def address_inserted(email):
    return await creating_address(email)

@rota_address.get("/{email}")
async def address_researched(email):
    return await search_address(email)







    

