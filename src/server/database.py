from os import environ
from motor.motor_asyncio import AsyncIOMotorClient
from src.config import configuracao
import asyncio

class DataBase:
    client: AsyncIOMotorClient = None
    database_uri = environ.get("DATABASE_URI")
    users_collection = None
    address_collection = None
    product_collection = None
    cart_collection = None

db = DataBase()

async def connect_db():
    # conexao mongo, com no máximo 10 conexões async
    db.client = AsyncIOMotorClient(
        db.database_uri,
        maxPoolSize=10,
        minPoolSize=10,
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    db.users_collection = db.client.shopping_clothes.users
    db.address_collection = db.client.shopping_clothes.addresses
    db.product_collection = db.client.shopping_clothes.products
    db.cart_collection = db.client.shopping_clothes.carts
    
    
async def disconnect_db():
    db.client.close()
    
def iniciar_cliente_mongo() -> AsyncIOMotorClient:
    cliente_mongo = AsyncIOMotorClient(configuracao.bd_url)
    cliente_mongo.get_io_loop = asyncio.get_event_loop
    return cliente_mongo
    
