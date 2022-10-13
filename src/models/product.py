from bson.objectid import ObjectId
from typing import List
from fastapi import status, HTTPException
import logging

logger = logging.getLogger(__name__)

async def regra_cad_product(product_collection, product_code):
    product = await get_product_by_code(product_collection, product_code)
    if "code" in product:
        if product["code"] == product_code:
            return True

async def create_product(product_collection, product):
    try: 
        product = dict(product)
        response = await regra_cad_product(product_collection, (product["code"]))
        if response:
                return {'status': 'product already exists'}
        else:
            answer = await product_collection.insert_one(product)
        
            if answer.inserted_id:
                id = str(answer.inserted_id)
                return {'status': 'product inserted', '_id':id, "status_code": status.HTTP_200_OK}
            return {}
        
    except Exception as e:
       logger.exception(f'create_product.error: {e}')
       raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
async def get_product_by_id(product_collection, product_id):
    try:
        filtro = {'_id': ObjectId(product_id)}
        product = await product_collection.find_one(filtro)
        
        if product:
            product['_id'] = str(product['_id'])
            return product
        return {'status': 'product not found', "status_code": status.HTTP_200_OK}
        
    except Exception as e:
        logger.exception(f'get_product.error: {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
async def get_product_by_code(product_collection, product_code):
   
    try:
        # filtro = {'code': 2}
        product = await product_collection.find_one({'code': product_code})
        
        if product:
            # product['_id'] = str(product['_id'])
            return product
        return {'status': 'product not found', "status_code": status.HTTP_200_OK}
        
    except Exception as e:
        logger.exception(f'get_product.error: {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
       

async def get_product_by_name(product_collection, product_name):
    try:
        lista_todas = []
        filtro = {"name": {"$regex": '/*'+product_name+'/*'}}
        cursor_pesquisa = product_collection.find(filtro)
        
        async for product in cursor_pesquisa:
            product['_id'] = str(product['_id'])
            lista_todas.append(product)     
        return lista_todas
    
    except Exception as e:
        logger.exception(f'get_product_by_name.error: {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
async def get_all_products(product_collection) -> List[dict]:
    try:
        filtro = {}
        lista_todas = []
        cursor_pesquisa = product_collection.find(filtro)
        async for product in cursor_pesquisa:
            product['_id'] = str(product['_id'])
            lista_todas.append(product)     
        return lista_todas
    
    except Exception as e:
        logger.exception(f'get_product.error: {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

async def delete_product_by_id(product_collection, product_id):
    try:
        filtro = {'_id': ObjectId(product_id)}
        answer = await product_collection.delete_one(filtro)
        if answer.deleted_count:
            return {'status': 'product deleted', "status_code": status.HTTP_200_OK}
        return {'status': 'product not deleted', "status_code": status.HTTP_200_OK}
        
    except Exception as e:
        logger.exception(f'delete_product.error: {e}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
async def update_product_by_id(product_collection, product_id, product):
    try:
        product_datas = dict(product)
        product_datas = {k: v for k, v in product_datas.items() if v is not None}
        filtro = {"_id": ObjectId(product_id)}
        
        novos_dados = {"$set": product_datas}
        answer = await product_collection.update_one(filtro, novos_dados)
        
        if answer.modified_count:
            return {'status': 'product modified', "status_code": status.HTTP_200_OK}
        return {'status': 'product not modified', "status_code": status.HTTP_200_OK}
    
    except Exception as e:
        logger.exception(f'update_product.error: {e}') 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
 