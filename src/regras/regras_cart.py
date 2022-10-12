
from src.models.address import get_address
from src.models.persistencia_bd import obter_colecao
from bson.objectid import ObjectId
import datetime
from src.models.cart import create_cart, get_cart_by_email, update_cart
from src.models.product import get_product_by_code
import json

COLECAO_CART = obter_colecao("carts") 
COLECAO_USER = obter_colecao("users") 
COLECAO_ADDRESS = obter_colecao("addresses")
COLECAO_PRODUCTS = obter_colecao("products")


async def add_cart(email):
        print(email)
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
                    "item": []
                }
    
        # if  email != cart_found["address"]["user"]["email"]:
        await create_cart(
            COLECAO_CART,
            dict(cart)
        )
        #     return "deu certo"
            
        # else:
        #     return "Errouuuuuu"
            
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
             
    testing = await COLECAO_CART.update_one(
        {'address.user.email': email},
        {"$addToSet": {"item": {} }}
    )
    
    
    
    
     # product_exists = await COLECAO_CART.find_one({"code": teste}, {'_id': 0})
    # print(product_exists)
    
    # if product_exists:
    
async def aggregatin_item(email):
    print(email)
    aggregating =  COLECAO_CART.aggregate([
        # {
        #     "$match":{
        #         "address.user.email": email,
    
        #     }
        # },
        {
            "$unwind": "$carts"
        },
        {
            "$group":
        {
            "_id": "$products.code",
            "count": {"$sum": "$item"}
        }

        }
    ])
    
    print(json.loads(aggregating))
    
    # {'address.user.email': cart["address"]["user"]["email"]},
    #         {"$addToSet": {"product": produto}}
            
    testing = await COLECAO_CART.update_one(
        {'address.user.email': email},
        {"$addToSet": {"item": {} }}
    )
    
    print("Esse é o aggragate")
    # pprint(list(COLECAO_CART.aggragate(aggregating)))
    # print(testing)
    
    return "OK"
    
    
   


