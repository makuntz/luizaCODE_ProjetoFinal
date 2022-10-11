from src.schemas.cart import CartSchema


async def create_cart(cart_collection, cart):
    try:
        cart = await cart_collection.insert_one(cart)
        print("oi luan")
        
        if cart.inserted_id:
            cart = await get_cart(cart_collection, cart.inserted_id)
            print("tchau luan")
        return cart

    except Exception as e:
        print(f'create_cart.error: {e}')

async def get_cart(cart_collection, cart_id):
    try:
        data = await cart_collection.find_one({'_id': cart_id})
        if data:
            return data
    except Exception as e:
        print(f'get_cart.error: {e}')
        


async def get_cart_by_email(cart_collection, email):
    try:
        data = await cart_collection.find_one({'address.user.email': email})
        if data:
            return data
    except Exception as e:
        print(f'get_cart_by_email.error: {e}')
        


async def update_cart(cart_collection, email, produto):
    try:
        cart = await cart_collection.update_one(
            {'address.user.email': email}, 
            {"$addToSet": {"produto": produto}}
        )
        if cart:
            return cart
    except Exception as e:
        print(f'update_cart.error: {e}')