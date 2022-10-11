
from src.models.persistencia_bd import obter_colecao
from src.models.user import create_user, get_user_by_email, if_user_exists
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

COLECAO_USER = obter_colecao("users") 

user = { 
                "name": "lya",
                "email": "amarelo@email.com",
                "password": "senha123",
                "is_active": True
            }


def check(email):
    if(re.search(regex,email)):
        return True  
          
    else:
        return False  
        

async def add_user():
    
    user = { 
                "name": "cascão",
                "email": "amarelo@gmail.com",
                "password": "senha123",
                "is_active": True
            }
    
    validate_email = check(user["email"])
    
    length = user["email"].split('@')
       
    if len(length[0]) >= 3:
        
        if validate_email == True:
            
            user_exist = await if_user_exists(user["email"], COLECAO_USER)
            
            if user_exist == True:
                return "Email já cadastrado"
            
            await create_user(
                COLECAO_USER,
                dict(user)
                )

            return user
        
    else:
        return False
         
    
async def get_user(email):
    response = await get_user_by_email(
        COLECAO_USER,
        email
    )
    return response

async def get_everybody():
    if_user_exists(
        COLECAO_USER
    )
