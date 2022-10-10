
import email
from src.models.persistencia_bd import obter_colecao
from bson.objectid import ObjectId
import datetime
from src.models.user import create_user, get_user_by_email


COLECAO_USER = obter_colecao("users") 

user = { 
                "name": "Beicola",
                "email": "bruna@email.com",
                "password": "senha123",
                "is_active": True
            }


async def add_user():
    
    await create_user(
        COLECAO_USER,
        dict(user)
    )
    
    print('DEU CERTOOOO')
    return user


async def get_user():
    
    await get_user_by_email(
        COLECAO_USER,
        user["email"]
    )
        
    return user


# async def delete_user():
#     await