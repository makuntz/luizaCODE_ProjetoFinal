
# {
#     "name": "Saia preta da Shein ",
#     "size": "M",
#     "decription": "Saia de courinho preto",
#     "price": 50.00,
#     "type": "saia",
#     "category": "feminina",
#     "trademark": "Shein",
#     "color": "preto"   
# }

def verifica_dados_produto(produto):
    if produto["name"] is None:
        return "Produto sem nome!"
    elif produto["decription"] is None:
        return "Produto sem descrição!"
    elif produto["code"] is None:
        return "Produto sem código!"
    elif produto["price"] <= 0.01:
        return "Produto sem código!"