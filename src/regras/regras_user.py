
from src.models.persistencia_bd import obter_colecao
from bson.objectid import ObjectId
import datetime
from src.models.user import create_user, get_user_by_email
import re


COLECAO_USER = obter_colecao("users") 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


user = { 
                "name": "lya",
                "email": "amarelo@email.com",
                "password": "senha123",
                "is_active": True
            }

# def check(email):
#     if(re.search(regex,email)):  
#         print("Email válido")  
          
#     else:  
#         print("Email inválido")
    




async def add_user():
    
#     validate_email = check(user.email)   
    user = { 
                "name": "lya",
                "email": "amarelo@email.com",
                "password": "senha123",
                "is_active": True
            }
    
    
    
    await create_user(
        COLECAO_USER,
        dict(user)
        )

    print('DEU CERTOOOO')
    return user


async def get_user(email):
    # email = "bruna@email.com"
    print(email)
    response = await get_user_by_email(
        COLECAO_USER,
        email
    )
    print(response)
    return response


# async def delete_user():
#     await

# {'_id': ObjectId('634482316167dd031bc29ee5'), 'name': 'lya', 'email': 'bruna@email.com', 'password': 'senha123', 'is_active': True}