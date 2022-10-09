from bson.objectid import ObjectId

async def create_product(product_collection, product):
    try: 
        product = await product_collection.insert_one(product)
        if product.inserted_id:
            print(product)
            return product  
    except Exception as e:
        print(f'create_product.error: {e}')
        
async def get_product_by_id(product_collection, product_id):
    try:
        data = await product_collection.find_one({'_id': ObjectId(product_id)})
        if data:
            return data
    except Exception as e:
        print(f'get_product.error: {e}')
        
async def get_all_products(product_collection):
    try:
        filtro = {}
        lista_todas = []
        cursor_pesquisa = product_collection.find(filtro)
        print(cursor_pesquisa)
        async for product in cursor_pesquisa:
            print(">>", product)
            lista_todas.append(dict(product))
            
        # lista_todas = [
        #     product
        #     async for product in cursor_pesquisa
        # ]
        return lista_todas
    except Exception as e:
        print(f'get_product.error: {e}')

async def delete_product_by_id(product_collection, product_id):
    try:
        product = await product_collection.delete_one(
            {'_id': ObjectId(product_id)}
        )
        if product.deleted_count:
            return {'status': 'Product deleted'}
    except Exception as e:
        print(f'delete_product.error: {e}')