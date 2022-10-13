
from src.schemas.user import UserSchema
from typing import List

async def create_user(user_collection, user):
    try:
        user = await user_collection.insert_one(user)
        
        if user.inserted_id:
            user = await get_user(user_collection, user.inserted_id)

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
    


async def if_user_exists(email, user_collection):
    
    user = await user_collection.find_one({'email': email})
    
    if user:
        return True
    return False

async def get_all_users(user_collection) -> List[dict]:
    try:
        filtro = {}
        lista_todas = []
        cursor_pesquisa = user_collection.find(filtro)
        async for user in cursor_pesquisa:
            user['_id'] = str(user['_id'])
            lista_todas.append(user)     
        return lista_todas
    
    except Exception as e:
        print(f'get_all_users.error: {e}')

    




   

# async def if_user_exists(user_collection, limit, skip):
#     try:
#         user =  user_collection.find({'_id': 0}).skip(int(skip)).limit(int(limit))
#         users = await user.to_list(length=int(limit))
#         print(users)
        
#         if user:
#             return user
#     except Exception as e:
#         print(f'if_user_exists.error: {e}')



# async def delete_user(user_collection, user_id):
#     try:
#         user = await user_collection.delete_one({'_id': user_id})
#         if user.deleted_count:
#             return {'status': 'Usuário deletado'}
#     except Exception as e:
#          print(f'delete_user.error: {e}')