from fastapi import APIRouter

from src.models.product import (
    create_product,
    get_product_by_id,
    get_all_products,
    delete_product_by_id
)

from src.schemas.product import  ProductSchema

from src.models.persistencia_bd import obter_colecao

OK = "OK"
FALHA = "FALHA"

# Deixando o meu 'recurso de conversa' com coleção global.
COLECAO_PRODUTO = obter_colecao("products")

# Minha rota API de músicas
rota_produtos = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/products",
    # Rótulos/tags
    tags=["Produtos"],
)

# Criando produto
@rota_produtos.post("/")
async def criar_produto(produto: dict):
    print(produto)
    await create_product(COLECAO_PRODUTO, produto)
    print(COLECAO_PRODUTO)
    return OK

# Retornando todos os produtos
@rota_produtos.get("/")
async def retornar_produtos():
    return  await get_all_products(COLECAO_PRODUTO)

# Deletando um produto pelo seu id
@rota_produtos.delete("/produto/{id_produto}/")
async def deletar_produto(id_produto: str):
   return await delete_product_by_id(COLECAO_PRODUTO, id_produto)
    
# Deletando um produto do carrinho 
# def deletar_produto_carrinho(id_produto):
#     for carrinho in db_carrinhos.items():
#         print(carrinho)
#         if id_produto in carrinho[1]["id_produtos"]:
#             print(f"Deletando o produto {id_produto}")
            
#             #Descontando o valor e quantidade do item retirado
#             qtdProdRemov        = carrinho[1]["id_produtos"][id_produto]["quantidade"]
#             precoTotProdRemov   = Decimal(COLECAO_PRODUTO[id_produto].preco) * qtdProdRemov    
#             print(qtdProdRemov) 
#             db_carrinhos[1]['quantidade_de_produtos'] -=  qtdProdRemov
#             db_carrinhos[1]['preco_total'] -=  precoTotProdRemov
            
#             carrinho[1]["id_produtos"].pop(id_produto)
            