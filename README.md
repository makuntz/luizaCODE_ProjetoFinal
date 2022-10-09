# Carrinho luiza < CODE >
## Atividade API -  Carrinho de compra de roupas

Esse projeto contém a implementação do projeto final do luiza < CODE >. Trata de um sistema de carrinho de compras utililizando rotas, validações e banco de dados.

## Requisitos e Ferramentas

Esse projeto utiliza os seguintes:

    .Python3
    .MongoDB

Somente é necessário ter o Python3 pré instalado para a execução do projeto. Outras dependências são gerenciadas pelo gerenciador de pacotes.

## Execução

Após instalar o Python3: 
1. Clone [este repositório](https://github.com/makuntz/luizaCODE_ProjetoFinal) através do comando:

   `git clone`

   <b>Importante: </b> Certifique-se de estar clonando a branch main (master). 

2. Instale as dependências do projeto na pasta raíz:

   `pip install -r requirements.txt`

3. Na pasta raíz rode o projeto, inicie a aplicação utilizando o comando:

   `<uvicorn main:app --reload>`

Esse comando compila o projeto, iniciando o cliente em: 
>http://localhost:8000.

## Funcionamento

Ao acessar a URL

> http://localhost:8000

A primeira rota/pagina (página principal) é apenas as boas vindas do projeto. Portanto nesse endereço acima, deverá aparecer: 

`Seja bem vinda!`

## Documentação Swagger

Nessa etapa também é possível acessar a documentação Swagger através da URL:

> http://localhost:8000/docs

Essa é uma documentação nativa da FastAPI. Para mais informações acesse a documentação a documentação [aqui](https://fastapi.tiangolo.com/tutorial/first-steps/#interactive-api-docs).

## Divisão do Projeto

O projeto foi arquitetado em pastas, onde cada pasta possui arquivos com responsabilidades própria.
A divisão de pastas foi feita da seguinte forma:

* <b>Controllers:</b> Possui o controle das rotas.
* <b>Models:</b> Ações relacionadas a alterações no banco de dados.
* <b>Regras:</b> Definições de regras de negócio
* <b>Routers:</b> Armazena a configuração de rota principal.
* <b>Schemas:</b> Declaração de classes onde é feita a interface dos objetos trabalhados ao longo do projeto.
* <b>Server:</b> É onde é feita as configurações da nosso _database_, assim como as definições das nossas coleções.

Já a divisão das responsabilidades são:
* <b>User:</b>
* <b>Address:</b>
* <b>Products:</b>
* <b>Carts:</b>

