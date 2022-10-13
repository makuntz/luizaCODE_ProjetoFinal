from src.schemas.cart import CartSchema


async def create_cart(cart_collection, cart):
    try:
        cart = await cart_collection.insert_one(cart)
                
        if cart.inserted_id:
            cart = await get_cart(cart_collection, cart.inserted_id)
            
        return cart

    except Exception as e:
        print(f'create_cart.error: {e}')

async def get_cart(cart_collection, email):
    
    try:
        data = await cart_collection.find_one({'email': email})
        if data:
            return data
    except Exception as e:
        print(f'get_cart.error: {e}')
        


async def get_cart_by_email(cart_collection, email):
    
    try:
        data = await cart_collection.find_one({'address.user.email': email}, {'_id': 0})
        if data:
            return data
    except Exception as e:
        print(f'get_cart_by_email.error: {e}')
        


async def update_cart(cart_collection, cart, produto):
    try:
        cart = await cart_collection.update_one(
            {'address.user.email': cart["address"]["user"]["email"]},
            {"$push": {"product": produto}}
        )
        
        if cart:
            return cart
    except Exception as e:
        print(f'update_cart.error: {e}')
        


