from pymongo import MongoClient
from fastapi import APIRouter, FastAPI
from src.regras.regras_cart import add_cart
from src.schemas.cart import CartSchema


rota_carts = APIRouter(
    prefix="/api/cart",
    tags=["Carts"]
)


##acrescentar id_prod uto na rota, para verificar se produto existe
@rota_carts.post("/{id_user}/{id_product}")
async def cart_crud():
    return await add_cart()
   
   
    
        
         
    
   


