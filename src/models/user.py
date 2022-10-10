from src.schemas.user import UserSchema


async def create_user(user_collection, user):
    try:
        user = await user_collection.insert_one(user)
        print("socorro deus")
        
        if user.inserted_id:
            user = await get_user(user_collection, user.inserted_id)
            print("tchau luan")
        return user

    except Exception as e:
        print(f'create_user.error: {e}')

async def get_user(user_collection, user_id):
    try:
        user = await user_collection.find_one({'_id': user_id})
        if user:
            return user
    except Exception as e:
        print(f'get_user.error: {e}')
        
        
async def get_user_by_email(user_collection, email):
    try:
        user = await user_collection.find_one({'email': email}, {'_id': 0})
        
        if user:
            return user
    except Exception as e:
        print(f'find_user_by_email.error: {e}')
    


# async def delete_user(user_collection, user_id):
#     try:
#         user = await user_collection.delete_one({'_id': user_id})
#         if user.deleted_count:
#             return {'status': 'Usuário deletado'}
#     except Exception as e:
#          print(f'delete_user.error: {e}')