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
        data = await user_collection.find_one({'_id': user_id})
        if data:
            return data
    except Exception as e:
        print(f'get_user.error: {e}')