from pymongo import MongoClient
# from bson.objectid import ObjectId
from decimal import Decimal
import datetime
from fastapi import FastAPI
from src.regras.regras import add_cart
from src.schemas.cart import CartSchema
from src.server.database import iniciar_cliente_mongo
# from src.server.database import connect_db, db, disconnect_db

# from src.models.cart import create_cart
# from src.regras.regras import add_cart

cliente_mongo = iniciar_cliente_mongo()
app = FastAPI()


@app.get("/")
def rota_principal():
    return "Seja bem-vinda"

##acrescentar id_prod uto na rota, para verificar se produto existe
@app.post("/cart/{user}")
async def cart_crud(user):
    return await add_cart(user)
    # await connect_db()
    
    # cart_collection = db.cart_collection
    
    # ##essa variavel deve conter funcao de busca no banco
    # cart = { 
    #             "user": "123456",
    #             "price": 111.22,
    #             "paid": False,
    #             "create": datetime.datetime.now()
    #         }
   
    # if cart["user"] != user:
    #         await create_cart(
    #             cart_collection,
    #             dict(cart)
    #         )
    # else:
    #     print('falhouuu')
    
    
    
    # await disconnect_db()
    
    # return cart

 
    
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
      
   
    
        
         
    
   


