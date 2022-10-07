from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection

from src.configuracoes import config 

#utilizando um cliente mongo global




def start_client_mongo() -> AsyncIOMotorClient:
    #conectar ao BD
    client_mongo = AsyncIOMotorClient(config.DATABASE_URI)
    return client_mongo


#"ativando" o client mongo
client_mongo = start_client_mongo()


# criando funcões auxiliares para trabalhar com cada código que possui um BD


#essa função irá obter o database padrão que está na str de conexão 
def get_db() -> AsyncIOMotorDatabase:
    return client_mongo.get_default_database()


#obtem a coleção que desejamos a partir da base de dados padrão
def get_collection(collection_name:str) -> AsyncIOMotorCollection:
    db = get_db()
    collection = db[collection_name]
    return collection
    









# class DataBase:
#     client: AsyncIOMotorClient = None
#     database_uri = environ.get("DATABASE_URI")
#     users_collection = None
#     address_collection = None
#     product_collection = None
#     cart_collection = None

# db = DataBase()

# async def connect_db():
#     # conexao mongo, com no máximo 10 conexões async
#     db.client = AsyncIOMotorClient(
#         db.database_uri,
#         maxPoolSize=10,
#         minPoolSize=10,
#         tls=True,
#         tlsAllowInvalidCertificates=True
#     )
#     db.users_collection = db.client.shopping_clothes.users
#     db.address_collection = db.client.shopping_clothes.address
#     db.product_collection = db.client.shopping_clothes.products
#     db.cart_collection = db.client.shopping_clothes.cart

# async def disconnect_db():
#     db.client.close()