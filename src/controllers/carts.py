from pymongo import MongoClient
from bson.objectid import ObjectId
from decimal import Decimal
import datetime
from fastapi import FastAPI, Request
import asyncio
from src.schemas.cart import CartSchema

app = FastAPI()


from src.models.cart import (
    create_cart
)

# from src.models.user import (
#     get_user_by_email
# )

from src.server.database import connect_db, db, disconnect_db



@app.get("/")
def rota_principal():
    return "Seja bem-vinda"


async def cart_crud():
    
    await connect_db()
    cart_collection = db.cart_collection
    # users_collection = db.users_collection
    # address_collection = db.address_collection   
    
     
    #email = "lu_domagalu@gmail.com"
    # user = await get_user_by_email(
    #     users_collection,
    #     email
    # )
    
    # address_is_true = await address_collection.find_one({"address.is_delivery": True})
    
    # cart =   {
    # #     "user": '123456',
    #     "price": 111.22,
    #     "paid": False
    # #     "create": datetime.datetime.now()
    # #     #"address": 'address_is_true'
                  
    # } 
      
    @app.post("/cart")
    async def criar_teste(cart: CartSchema):
        await create_cart(
            cart_collection,
            cart = {
                "user": '123456',
                "price": 111.22,
                "paid": False,
                "create": datetime.datetime.now()
            } 
        )        
    print("deu certooo")
    criar_teste()

    await disconnect_db()
   


