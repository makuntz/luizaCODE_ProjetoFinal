from src.models.persistencia_bd import obter_colecao


COLECAO_ADDRESS = obter_colecao("addresses") 



from src.models.address import (
    create_address,
    get_address_id_user,
    update_address,
    delete_address,
    add_address
   )


async def add_address():
    
    ##colocar as regras aqui
    
    await create_address(
        COLECAO_ADDRESS,
        user = "123456",
        address={
            "street": "Rua Setenta e três, Numero 20",
              "cep": "7451263",
              "district": "São Paulo",
              "city": "São Paulo",
              "state": "São Paulo",
              "is_delivery": True
        }
    )