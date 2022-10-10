import email
from src.models.persistencia_bd import obter_colecao


COLECAO_ADDRESS = obter_colecao("addresses") 



from src.models.address import (
    create_address,
    get_address_id_user,
    update_address,
    delete_address,
    add_address,
    get_address
   )


async def adding_address():
    
    ##colocar as regras aqui
    
    ##user_found = COLECAO_USERS.find_one() -- usar esse user no create_address abaixo no lugar de user
    
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
    

async def search_address():
    
    address_email = 'fazer busca do user pelo email usando o find_one'
    
    address = await get_address(
        COLECAO_ADDRESS,
        address_email
    )
    print(address)
    

async def deleting_address():
    ...