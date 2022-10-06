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



@app.post("/cart")
async def cart_crud(cart: CartSchema):
    # option = input("Entre com a opção de CRUD: ")
    
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
    
    cart =   {
    #     "user": '123456',
        "price": 1796.4,
        "paid": False,
    #     "create": datetime.datetime.now()
    #     #"address": 'address_is_true'
                  
    } 
   
    
    
    
    info_cart_insert = await create_cart(
        cart_collection,
        cart
        
    )        
    
    print(info_cart_insert)
    

    await disconnect_db()
    return cart


@app.get("/cart")
def teste_post(cart):
    return cart