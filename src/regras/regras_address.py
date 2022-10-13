from urllib import response
from src.schemas.address import Address
from src.schemas.user import UserSchema
from src.models.persistencia_bd import obter_colecao


COLECAO_ADDRESS = obter_colecao("addresses") 
COLECAO_USER = obter_colecao("users")

from src.models.user import (
    get_user_by_email
)

from src.models.address import (
    create_address,
    get_address
   )

async def creating_address(email):
    
    #colocar o user que foi buscado pelo email aqui embaixo
    email= await get_user_by_email(
        COLECAO_USER,
        email
    )
    
    
    address = await create_address(
        COLECAO_ADDRESS,
        email,
        address_data={
            "street": "Rua Setenta e três, Numero 20",
            "cep": "7451263",
            "city": "São Paulo",
            "state": "São Paulo",
            "is_delivery": True
        }
        
    )
        

#buscar endereço pelo email
async def search_address(email):
          
    address = await get_address(
        COLECAO_ADDRESS,
        email
    )
   
    
