
from src.models.address import get_address
from src.models.persistencia_bd import obter_colecao
import datetime
from src.models.cart import create_cart, get_cart_by_email, update_cart
from src.models.user import if_user_exists

COLECAO_CART = obter_colecao("carts") 
COLECAO_USER = obter_colecao("users") 
COLECAO_ADDRESS = obter_colecao("addresses")
COLECAO_PRODUCTS = obter_colecao("products")


async def add_cart(email):
        cart_found = await get_cart_by_email(COLECAO_CART, email)
        
        
        user = await get_address(
            COLECAO_ADDRESS,
            email
        )
        print(user)
    
        cart = { 
                    "address": user,
                    "create": datetime.datetime.now(),
                    "product": [],
                    "items": []
                }
        
        user_exist = await if_user_exists(
            email,
            COLECAO_USER
               
        )
         
        
        if user_exist == True:
            await create_cart(
                COLECAO_CART,
                dict(cart)
            )
            return "Carrinho criado com sucesso!"
        else:
            return "Usuario nao cadastrado!"
         

 
 
async def insert_product(email, product_code):
    
    cart_recieve = await get_cart_by_email(
        COLECAO_CART,
        email
    )
    
    teste = int(product_code)
    product_recieve = await COLECAO_PRODUCTS.find_one({"code": teste})
   
    await update_cart(
        COLECAO_CART,
        cart_recieve,
        product_recieve
    )
    print("Produto inserido com sucesso")
    
    cart_recieve_two = await get_cart_by_email(
        COLECAO_CART,
        email
    )
    
    if cart_recieve_two is not None:
        x = cart_recieve_two["product"]
        y = len(x)

        await COLECAO_CART.update_one(
            {'address.user.email': email},
            {"$set": {"items": y}}
        )
    else:
        print("Error")
    
    
    sum = 0
    for prod in x:
        sum = sum + prod["price"]
    print (sum)
    
    await COLECAO_CART.update_one(
            {'address.user.email': email},
            {"$set": {"total_price": sum}}
        )
    
    
    return "Ok"
    
    
    



