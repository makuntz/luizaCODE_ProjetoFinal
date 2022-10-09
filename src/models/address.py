from src.schemas.address import Address
from src.schemas.user import UserSchema
from src.schemas.address import AddressSchema

# Buscar usuário pelo email para achar o user_id
async def get_user_by_email(users_collection, email):
    user = await users_collection.find_one({'email': email})
    return user

# Ver se existe endereço para o usuário
async def get_address_id_user(address_collection, user_id):
    try:
        data = await address_collection.find_one({'user._id': user_id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')

#criar endereço quando não existe nenhum endereço vinculado ao usuário
async def create_address(address_collection, address, user):
    try:
        address = await address_collection.insert_one({"user": user, "address": address})
        
        if address.inserted_id:
            address = await get_address(address_collection, address.inserted_id)
            return address

    except Exception as e:
        print(f'create_address.error: {e}')
        

async def get_address(address_collection, address_id):
    try:
        data = await address_collection.find_one({'_id': address_id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')

#criar endereço quando já existe um endereço vinculado ao usuario
async def add_address(address_collection, user_id, address_data):
    try:
        data = {k: v for k, v in address_data.items() if v is not None}

        address = await address_collection.update_one(

            {'user._id': user_id}, 
            {'$addToSet': {'address': data}}

        )

        if address.modified_count:
            return True, address.modified_count

        return False, 0
    except Exception as e:

        print(f'add_address.error: {e}')


#fazer o update do endereço existente
async def update_address(address_collection, address_id, address_data):
    try:
        data = {k: v for k, v in address_data.items() if v is not None}

        address = await address_collection.update_one(
            {'_id': address_id}, {'$set': data}
        )

        if address.modified_count:
            return True, address.modified_count

        return False, 0
    except Exception as e:
        print(f'update_address.error: {e}')



#deletar endereço
async def delete_address(address_collection, address_id):
    try:
        address = await address_collection.delete_one(
            {'_id': address_id}
        )
        if address.deleted_count:
            return {'status': 'Address deleted'}
    except Exception as e:
        print(f'delete_address.error: {e}')

#agregar endereço com is delivery = true
async def aggregate_address(address_collection, user_id):
    try:
        address_aggregate = await address_collection.aggregate(
            [{'$match':{
                'user._id': user_id,
                'user.is_active': True
            }  
            },
            {
                '$unwind': '$address'
            }, 
            {
                '$match':{
                    'address.is_delivery': True
                }
            }]
        )
        if address_aggregate:
            return (address_aggregate)
    except Exception as e:
        print(f'delete_address.error: {e}')