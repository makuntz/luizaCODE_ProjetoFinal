
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
        cart_found = await get_cart_by_email(COLECAO_CART, email)
        
        print(cart_found)
        
        user = await get_address(
            COLECAO_ADDRESS,
            email
        )
        
    
        cart = { 
                    "address": user,
                    "create": datetime.datetime.now(),
                    "product": [],
                    "items": []
                }
    
       
        await create_cart(
            COLECAO_CART,
            dict(cart)
        )
         
        return "criado"
 
 
 
 
async def insert_product(email, product_code):
    
    cart_recieve = await get_cart_by_email(
        COLECAO_CART,
        email
    )
    
    teste = int(product_code)
    product_recieve = await COLECAO_PRODUCTS.find_one({"code": teste})
   
    result = await update_cart(
        COLECAO_CART,
        cart_recieve,
        product_recieve
    )
    print("Produto inserido com sucesso")
    
    cart_recieve_two = await get_cart_by_email(
        COLECAO_CART,
        email
    )
    
    x = cart_recieve_two["product"]
    y = len(x)
    
    testing = await COLECAO_CART.update_one(
        {'address.user.email': email},
        {"$set": {"items": y}}
    )
    
    print(testing)
    
    return "Ok"
    
    
    



