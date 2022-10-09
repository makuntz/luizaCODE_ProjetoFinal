from bson.objectid import ObjectId
from typing import List, Optional
import json

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
        filtro = {'_id': ObjectId(product_id)}
        product = await product_collection.find_one(filtro)
        if product:
            product['_id'] = str(product['_id'])
            print("Retorno", product)
            return product
    except Exception as e:
        print(f'get_product.error: {e}')
        
async def get_all_products(product_collection) -> List[dict]:
    try:
        filtro = {}
        lista_todas = []
        cursor_pesquisa = product_collection.find(filtro)
        print(cursor_pesquisa)
        async for product in cursor_pesquisa:
            product['_id'] = str(product['_id'])
            lista_todas.append(product)     
        return lista_todas
    
    except Exception as e:
        print(f'get_product.error: {e}')

async def delete_product_by_id(product_collection, product_id):
    try:
        filtro = {'_id': ObjectId(product_id)}
        product = await product_collection.delete_one(filtro)
        if product.deleted_count:
            return {'status': 'Product deleted'}
    except Exception as e:
        print(f'delete_product.error: {e}')