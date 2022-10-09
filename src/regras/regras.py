
from fastapi import FastAPI
from pymongo import MongoClient
from src.server.database import connect_db, db, disconnect_db
from src.server.database import iniciar_cliente_mongo
from bson.objectid import ObjectId
import datetime
from src.models.cart import create_cart


##funcao de busca ja esta pronta em models.cart
# from src.models.cart import get_cart



cliente_mongo = iniciar_cliente_mongo()


async def add_cart(user):
    ##verificar se é necessário conectar com o banco para chamar a funcar get_cart()
    await connect_db()
    
    
    ##essa variavel deve conter funcao de busca no banco
    cart = { 
                "user": "123456",
                "price": 111.22,
                "paid": False,
                # "create": datetime.datetime.now()
            }
    
    if cart["user"] != user:
            cart_collection = db.cart_collection

            await create_cart(
                cart_collection,
                dict(cart)
            )
    else:
        print('falhouuu')
    
    
    
    await disconnect_db()
    
    return cart


    # id_usuario = await get_cart()
    # id_usuario = ObjectId('6341b6b839a1a952f9f4eeca')
    
    
    
    
    
#     await disconnect_db