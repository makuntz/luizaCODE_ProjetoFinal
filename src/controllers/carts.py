from pymongo import MongoClient
from fastapi import APIRouter, FastAPI
from src.regras.regras_cart import add_cart, insert_product
from src.schemas.cart import CartSchema


rota_carts = APIRouter(
    prefix="/api/cart",
    tags=["Carts"]
)


##acrescentar id_prod uto na rota, para verificar se produto existe
@rota_carts.post("/{email}")
async def cart_crud(email):
    return await add_cart(email)

@rota_carts.put("/{email}/{product_code}")
async def add_product_cart(email, product_code):
        return await insert_product(email, product_code)
    

    

   
   
    
        
         
    
   


