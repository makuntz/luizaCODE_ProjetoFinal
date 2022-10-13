
from urllib import response
from src.models.persistencia_bd import obter_colecao
from bson.objectid import ObjectId
import datetime
from src.models.user import create_user, get_user_by_email, if_user_exists, get_all_users
import re

from src.regras.regras_cart import add_cart


COLECAO_USER = obter_colecao("users") 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check(email):
    if(re.search(regex,email)):
        return True  
        #print("Email válido")  
          
    else:
        print("Email inválido")
        return False  
        

async def add_user(user):
    user = dict(user)
    validate_email = check(user["email"])
    
    length = user["email"].split('@')
    print(length[0])
    
    if len(length[0]) >= 3:
        #print(user["email"])
        #return "Deu bom"
        
        if validate_email == True:
            print(COLECAO_USER)
            
            user_exist = await if_user_exists(user["email"], COLECAO_USER)
            
            if user_exist == True:
                return "Email já cadastrado"
            
            await create_user(
                COLECAO_USER,
                dict(user)
                )
            

            print('DEU CERTOOOO')
            return user
        else:
            print("Falhou!")
    else:
        return "Deu ruim"
         
    
async def get_user(email):
    # email = "bruna@email.com"
    print(email)
    response = await get_user_by_email(
        COLECAO_USER,
        email
    )
    print(response)
    return response

async def get_everybody():
    response = await get_all_users(
        COLECAO_USER
    )
    print(response)
    return response
    
# async def delete_user():
#     await

# {'_id': ObjectId('634482316167dd031bc29ee5'), 'name': 'lya', 'email': 'bruna@email.com', 'password': 'senha123', 'is_active': True}