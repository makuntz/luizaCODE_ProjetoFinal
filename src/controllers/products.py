from multiprocessing.connection import answer_challenge
from fastapi import APIRouter

from src.models.product import (
    create_product,
    get_product_by_id,
    get_product_by_code,
    get_all_products,
    delete_product_by_id,
    get_product_by_name,
    update_product_by_id
)

from src.schemas.product import  ProductUpdatedSchema, ProductSchema

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
async def criar_produto(produto: ProductSchema):
    print(f"Produto: {produto}")
    return await create_product(COLECAO_PRODUTO, produto)

# Retornando todos os produtos
@rota_produtos.get("/")
async def retornar_produtos():
    print('retornar todos os produtos')
    return await get_all_products(COLECAO_PRODUTO)

# Retornando um produto pelo id
@rota_produtos.get("/{id_produto}/")
async def retornar_produto(id_produto: str):
    print(f"retornar o produto de id: {id_produto}")
    return await get_product_by_id(COLECAO_PRODUTO, id_produto)

# Retornando um produto pelo codigo
@rota_produtos.get("/code/{code}/")
async def retornar_produto_por_codigo(code: int):
    print(f"retornar o produto de codigo: {code}")
    return await get_product_by_code(COLECAO_PRODUTO, code)

# Retornando um produto pelo nome
@rota_produtos.get("/name/{nome}/")
async def retornar_produto_pelo_nome(nome: str):
    print(f"retornar produtos que contenham a string: {nome}")
    return await get_product_by_name(COLECAO_PRODUTO, nome)

# Deletando um produto pelo seu id
@rota_produtos.delete("/{id_produto}/")
async def deletar_produto(id_produto: str):
    print(f"deletar produto de id:{id_produto}")
    return await delete_product_by_id(COLECAO_PRODUTO, id_produto)

@rota_produtos.put("/{id_produto}")
async def atualizar_produto(id_produto: str, produto: ProductUpdatedSchema):
    print("atualizar produto", id_produto, "|", produto)
    return await update_product_by_id(COLECAO_PRODUTO, id_produto, produto)

    
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
            