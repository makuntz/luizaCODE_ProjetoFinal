from src.models.address import (
    create_address,
    get_address_id_user,
    update_address,
    delete_address,
    add_address
   )
from src.server.database import connect_db, db, disconnect_db


async def addredd_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    address_collection = db.address_collection

    address =  [
           {
              "street": "Rua Quarenta e Sete, Numero 3",
              "cep": "8465312",
              "district": "São Paulo",
              "city": "São Paulo",
              "state": "São Paulo",
              "is_delivery": True
           }
       ]

    if option == '1':
        # create address
        address = await create_address(
            address_collection,
            address
        )
        print(address)
    elif option == '2':
        # get address
        address = await get_address_id_user(
            address_collection,
            address["user._id"]
        )
        print(address)
    elif option == '3':
        # update
        address = await get_address_id_user(
            address_collection,
            address["user._id"]
        )

        address_data = {
            "street": "Rua Quarenta e Sete, Numero 4"
        }

        is_updated, numbers_updated = await update_address(
            address_collection,
            address["_id"],
            address_data
        )
        if is_updated:
            print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
        else:
            print("Atualização falhou!")
    
    elif option == '4':
        # add address para um usuário que já possui endereço
        address = await get_address_id_user(
            address_collection,
            address["user._id"]
        )

        address_data = [
           {
              "street": "Rua Setenta e três, Numero 20",
              "cep": "7451263",
              "district": "São Paulo",
              "city": "São Paulo",
              "state": "São Paulo",
              "is_delivery": True
           }
       ]
       

        is_updated, numbers_updated = await add_address(
            address_collection,
            address["user._id"],
            address_data
        )
        if is_updated:
            print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
        else:
            print("Atualização falhou!")
    
    elif option == '5':
        # delete
        address = await get_address_id_user(
            address_collection,
            address["user._id"]
        )

        result = await delete_address(
            address_collection,
            address["_id"]
        )

        print(result)

   
    await disconnect_db()
