#criando aplicação FastAPI global para que cada um chame a partir do que for criar
from src.controllers.carts_rest_conf import creat_app_fastapi

#esse app será o chamado pelo uvicorn
app = creat_app_fastapi()
