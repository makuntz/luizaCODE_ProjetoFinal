# # from fastapi import FastAPI
# from motor.motor_asyncio import AsyncIOMotorClient
# import asyncio
# from src.config import configuracao
# from fastapi import FastAPI
# from src.server.database import iniciar_cliente_mongo


# app = FastAPI()

# cliente_mongo = iniciar_cliente_mongo()


# def iniciar_cliente_mongo() -> AsyncIOMotorClient:
#     cliente_mongo = AsyncIOMotorClient(configuracao.bd_url)
#     cliente_mongo.get_io_loop = asyncio.get_event_loop
#     return cliente_mongo


# @app.get("/")
# def rota_principal():
#     return "Seja bem-vinda"