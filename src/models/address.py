from src.schemas.address import Address
from src.schemas.user import UserSchema
from src.schemas.address import AddressSchema

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
async def create_address(address_collection, user, address_data):
    try:
        data = {k: v for k, v in address_data.items() if v is not None}
        print(data)
        address = await address_collection.insert_one(
           {"user": user, "address": address_data}
        )
        
        if address.inserted_id:
            print(address)
            return address

    except Exception as e:
        print(f'create_address.error: {e}')
        
