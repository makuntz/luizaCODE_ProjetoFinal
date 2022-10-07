async def create_cart(cart_collection, cart):
    #try:
        #new_cart = cart.dict()
        cart = await cart_collection.insert_one(cart)
        return cart

        # if inserted_cart.inserted_id:
        #     data_cart = await get_cart(cart_collection, cart.inserted_id)
        #     return data_cart

#     except Exception as e:
#         print(f'create_order.error: {e}')

# async def get_cart(cart_collection, cart_id):
#     try:
#         data = await cart_collection.find_one({'_id': cart_id})
#         if data:
#             return data
#     except Exception as e:
#         print(f'get_cart.error: {e}')