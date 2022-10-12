import datetime
from decimal import Decimal
from itertools import product
from typing import List
from pydantic import BaseModel, Field
from src.schemas.user import UserSchema
from src.schemas.address import Address, AddressSchema
from src.schemas.product import ProductSchema

# from src.schemas.address import Address
# from src.schemas.user import UserSchema

class CartSchema(BaseModel):
    address: AddressSchema
    create: datetime.datetime = Field(default=datetime.datetime.now())
    product: List[ProductSchema]=[]
    item: List=[]
  

    
# 1.

# Criar um carrinho de compras aberto e adicionar itens ao carrinho.
    # a. Todo carrinho de compras deve conter um cliente.
    # c. Se há um produto um mais produtos, na criação do carrinho, informe a quantidade de
    # cada produto. No seu trabalho, você pode começar com apenas um produto.

    # d. Ao criar o carrinho, você deve::
        # i. Validar se o cliente existe
        # ii. Validar se o produto a ser adicionado no carrinho existe
        # iii. Verificar se o cliente já possui um carrinho aberto. Caso contrário criar um
        # carrinho novo.
        # iv.

    # e. Ao adicionar um item no carrinho, o mesmo terá o valor total e quantidade de itens
    # atualizado


# 2. Alterar a quantidade de itens do carrinho novo.
    # a. No carrinho novo, com base no produto informado, a quantidade é modificada.
    
    # b. Para isto, você irá:
        # i. Validar se produto existe no carrinho
        # iii. Atualizar o valor total e quantidade de itens do carrinho
        
    # c. Se o carrinho zerar o número de itens, ou seja, o cliente removeu todos os itens do
    # carrinho, o mesmo pode ser excluído.
    
# 3. Consultar carrinho de compras aberto:.
    # a. Informar o cliente e retornar os dados do carrinho e produtos
    

# 7. Fechar o carrinho aberto:
# a. Simplesmente pode-se mudar o tipo do carrinho de compras para “fechado”..

