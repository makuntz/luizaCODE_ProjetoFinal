from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controllers.carts_rest_principal import rota_principal
from src.controllers.carts_rest import rota_cart

def config_rotas(app:FastAPI):
    app.include_router(rota_principal)
    app.include_router(rota_cart)


def configurar_api_rest(app: FastAPI):
    # Configurando o CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def creat_app_fastapi():
   
    app = FastAPI()

    
    configurar_api_rest(app)
    config_rotas(app)

    return app