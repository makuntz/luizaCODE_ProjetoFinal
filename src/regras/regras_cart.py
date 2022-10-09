
from src.models.persistencia_bd import obter_colecao
from bson.objectid import ObjectId
import datetime
from src.models.cart import create_cart


COLECAO_CART = obter_colecao("carts") 


async def add_cart(id_user, id_product):
    
    # user_found = chamar funcao de busca do usuario
    
    ##essa variavel deve conter funcao de busca no banco
    cart = { 
                "user": "123456789",
                "price": 111.22,
                "paid": False
                # "create": datetime.datetime.now()
            }
    

    await create_cart(
        COLECAO_CART,
        dict(cart)
    )
    
    print('DEU CERTOOOO')
    
    
    
 