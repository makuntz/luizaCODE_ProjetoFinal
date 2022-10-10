
from src.models.persistencia_bd import obter_colecao
from bson.objectid import ObjectId
import datetime
from src.models.user import create_user


COLECAO_USER = obter_colecao("users") 


async def add_user():
    
    user = { 
                "name": "Bruna",
                "email": "bruna@email.com",
                "password": "senha123",
                "is_active": True
            }

    await create_user(
        COLECAO_USER,
        dict(user)
    )
    
    print('DEU CERTOOOO')
    
    