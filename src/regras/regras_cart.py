
from src.models.address import get_address
from src.models.persistencia_bd import obter_colecao
from bson.objectid import ObjectId
import datetime
from src.models.cart import create_cart, get_cart_by_email, update_cart
from src.models.product import get_product_by_code


COLECAO_CART = obter_colecao("carts") 
COLECAO_USER = obter_colecao("users") 
COLECAO_ADDRESS = obter_colecao("addresses")
COLECAO_PRODUCTS = obter_colecao("products")


async def add_cart(email):
    
        email= await get_address(
            COLECAO_ADDRESS,
            email
        )
    
        cart = { 
                    "address": email,
                    "price": 111.22,
                    "paid": False,
                    "create": datetime.datetime.now()
                }
    

        await create_cart(
            COLECAO_CART,
            dict(cart)
        )
        
        print('DEU CERTOOOO')
        
    
    
async def insert_product(email, code):

   cart_recieve = await get_cart_by_email(
       COLECAO_CART,
       email
   )
   print(cart_recieve)
   
   product_recieve = await get_product_by_code(
       COLECAO_PRODUCTS,
       code
   )
   
   print(product_recieve)
   await update_cart(
        COLECAO_CART,
        cart_recieve,
        product_recieve
   )
   
   print("xablau")