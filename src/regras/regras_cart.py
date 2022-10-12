
from src.models.address import get_address
from src.models.persistencia_bd import obter_colecao
from bson.objectid import ObjectId
import datetime
from src.models.cart import create_cart, get_cart, get_cart_by_email, update_cart
from src.models.product import get_product_by_code


COLECAO_CART = obter_colecao("carts") 
COLECAO_USER = obter_colecao("users") 
COLECAO_ADDRESS = obter_colecao("addresses")
COLECAO_PRODUCTS = obter_colecao("products")


async def add_cart(email):
        cart_found = await get_cart(COLECAO_CART, email)
        
        user = await get_address(
            COLECAO_ADDRESS,
            email
        )
        
    
        cart = { 
                    "address": user,
                    "create": datetime.datetime.now(),
                    "product": [],
                    "item": []
                }
    
        if not email in cart["address"]:
            await create_cart(
                COLECAO_CART,
                dict(cart)
            )
        else:
            print("Error")
        
        
    
 
async def insert_product(email, product_code):

    cart_recieve = await get_cart_by_email(
        COLECAO_CART,
        email
    )
    
    teste = int(product_code)
    product_recieve = await COLECAO_PRODUCTS.find_one({"code": teste})
    product_exist = await COLECAO_CART.find_one({"code": teste}, {'_id': 0})
    
    if product_exist:
    
        
        aggregating = await COLECAO_CART.aggregate([
            {
                "$unwind": "$carts"
            },
            {
                "$group":
            {
                "_id": "$carts.code",
                "total": {"$sum": "$carts.quantity"}
            }

            }
        ])
    
        print("Esse é o aggragate", aggregating)
        return "Agregou"
    else:
        result = await update_cart(
            COLECAO_CART,
            cart_recieve,
            product_recieve
    )
    print("Chegou aqui")
    # return result
    
    
   


