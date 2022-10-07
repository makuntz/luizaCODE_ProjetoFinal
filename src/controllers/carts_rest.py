from fastapi import APIRouter
from src.server.database import get_collection
from src.schemas.cart import CartSchema




#criando rota 
rota_cart = APIRouter()


@rota_cart.post("/cart/")
async def creat_cart(cart: CartSchema):
    await get_collection("cart_collection").insert_cart(cart)
    return cart