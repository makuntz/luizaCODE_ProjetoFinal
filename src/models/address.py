from src.schemas.address import Address
from src.schemas.user import UserSchema
from src.schemas.address import AddressSchema
import json

#buscar endereço pelo email
async def get_address(address_collection, address_email):
    try:
        data = await address_collection.find_one({'user.email': address_email})
        if data:
            print (data)
            return data
    except Exception as e:
        print(f'get_address.error: {e}')

#criar endereço quando não existe nenhum endereço vinculado ao usuário
async def create_address(address_collection, address_data:Address, user:UserSchema):
    try:
        data = {k: v for k, v in address_data.items() if v is not None}
        
        address = await address_collection.insert_one(
            {"user": user}, 
            {"address": data}
        )
        
        if address.inserted_id:
            print(address)
            return address

    except Exception as e:
        print(f'create_address.error: {e}')
        

#criar endereço quando já existe um endereço vinculado ao usuario
async def update_address(address_collection, address_email, address_data):
    try:
        data = {k: v for k, v in address_data.items() if v is not None}

        address = await address_collection.update_one(

            {'user.email': address_email}, 
            {'$addToSet': {'address': data}}

        )

        if address.modified_count:
            print(address)
            return True, address.modified_count


        return False, 0
    except Exception as e:

        print(f'add_address.error: {e}')


#deletar endereço
async def delete_address(address_collection, address_id):
    try:
        address = await address_collection.delete_one(
            {'_id': address_id}
        )
        if address.deleted_count:
            print('Address deleted')
            return {'status': 'Address deleted'}
    except Exception as e:
        print(f'delete_address.error: {e}')

