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
    update_address,
    delete_address,
    get_address
   )

async def get_user(email):
    print(email)
    response = await get_user_by_email(
        COLECAO_USER,
        email = "amarelo@email.com"
    )
    print(response)
    return response


async def creating_address(address_data:Address, user:UserSchema):
    
    #colocar o user que foi buscado pelo email aqui embaixo
     
    address = await create_address(
        COLECAO_ADDRESS,
        user =  {
            "name": "lya",
            "email": "amarelo@email.com",
            "password": "senha123",
            "is_active": True,
        },
        address_data={
            "street": "Rua Setenta e três, Numero 20",
            "cep": "7451263",
            "city": "São Paulo",
            "state": "São Paulo",
            "is_delivery": True
        }, 
    )
    print(address)
    
    
#fazer o update do endereço
async def updating_address(address_email, address_data):
    address = await update_address(
        COLECAO_ADDRESS,
        address_email = "amarelo@email.com",
        address_data = {
            "street": "Rua 9 de julho, 1656",
            "cep": "7451263",
            "city": "Ribeirao Preto",
            "state": "São Paulo",
            "is_delivery": True
        }
    )
    print(address)


#buscar endereço pelo email
async def search_address(address_email):
          
    address = await get_address(
        COLECAO_ADDRESS,
        address_email = "amarelo@email.com"
    )
    print(address)
    
#pegar o address_id com a função search_address
async def deleting_address(address_id):
    
    delete = await delete_address(
        COLECAO_ADDRESS,
        address_id = "colocar o address_id"
    )
    print('endereço deletado')