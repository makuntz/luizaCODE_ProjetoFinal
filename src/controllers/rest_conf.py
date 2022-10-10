from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controllers.products import rota_produtos
from src.controllers.principal_rest import rota_principal
from src.controllers.carts import rota_carts
from src.controllers.addresses import rota_address
from src.controllers.users import rota_user


def configurar_rotas(app: FastAPI):
    # Publicando as rotas para o FastAPI.
    app.include_router(rota_principal)
    app.include_router(rota_produtos)
    app.include_router(rota_carts)
    app.include_router(rota_address)
    app.include_router(rota_user)

def configurar_api_rest(app: FastAPI):
    # Configurando o CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def criar_aplicacao_fastapi():
    # Crio a aplicação FastAPI
    app = FastAPI(
        # Título da aplicação. Será usado como título do Swagger.
        title="Carrinho de Roupas",
        version="01")

    # Configuro a aplicação FastAPI
    configurar_api_rest(app)
    # ... e configuro suas rotas
    configurar_rotas(app)

    return app
