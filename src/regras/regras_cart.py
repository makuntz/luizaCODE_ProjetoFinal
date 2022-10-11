
from src.models.persistencia_bd import obter_colecao
from bson.objectid import ObjectId
import datetime
from src.models.cart import create_cart
from src.models.user import get_user_by_email
from src.


COLECAO_CART = obter_colecao("carts") 
COLECAO_USER = obter_colecao("users") 


async def add_cart(email):
    
    #colocar o user que foi buscado pelo email aqui embaixo
        email= await get_user_by_email(
            COLECAO_USER,
            email
        )
    
    # user_found = chamar funcao de busca do usuario
    
    ##essa variavel deve conter funcao de busca no banco
        cart = { 
                    "user": email,
                    "price": 111.22,
                    "paid": False,
                    "create": datetime.datetime.now()
                }
    

        await create_cart(
            COLECAO_CART,
            dict(cart)
        )
        
        print('DEU CERTOOOO')
        
    
    
 