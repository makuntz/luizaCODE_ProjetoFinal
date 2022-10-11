import email
from manugr.luizaCODE_ProjetoFinal.src.models.address import get_user_by_email
from src.models.persistencia_bd import obter_colecao


COLECAO_ADDRESS = obter_colecao("addresses") 
COLECAO_USER = obter_colecao("users")


from src.models.address import (
    create_address,
    get_address_id_user,
    update_address,
    delete_address,
    add_address,
    get_address
   )

async def get_user(email):
    print(email)
    response = await get_user_by_email(
        COLECAO_USER,
        email
    )
    print(response)
    return response


async def adding_address():
    
    #colocar o user que foi buscado pelo email aqui embaixo
     
    await create_address(
        COLECAO_ADDRESS,
        user = "123456",
        address=[{
              "street": "Rua Setenta e três, Numero 20",
              "cep": "7451263",
              "city": "São Paulo",
              "state": "São Paulo",
              "is_delivery": True
        }, 
                 
        {
            "street": "Rua 9 de julho, 1656",
            "cep": "7451263",
            "city": "Ribeirao Preto",
            "state": "São Paulo",
            "is_delivery": True
        }]
    )
    

async def search_address(address_email):
          
    address = await get_address(
        COLECAO_ADDRESS,
        address_email
    )
    print(address)
    
#pegar o address_id com a função search_address
async def deleting_address(address_id):
    
    delete = await delete_address(
        COLECAO_ADDRESS,
        address_id
    )
    print('endereço deletado')