# Projeto Final: luiza < CODE >

## Atividade API: Carrinho de compra - e commerce de roupas 

Esse projeto contém a implementação do projeto final do luiza < CODE >. Trata de um sistema de uma API de carrinho de compras utililizando rotas, validações e banco de dados.

---
## :hammer: Requisitos e Ferramentas:

Esse projeto utiliza os seguintes:

    .Python3
    .MongoDB

Somente é necessário ter o Python3 pré instalado para a execução do projeto. Outras dependências são gerenciadas pelo gerenciador de pacotes.


## :construction: Execução:

Após instalar o Python3:

1. Clone [este repositório](https://github.com/makuntz/luizaCODE_ProjetoFinal) através do comando:

   `git clone`

   <b>Importante: </b> Certifique-se de estar clonando a branch main (master).

2. Ciração e ativação do ambiente virtual (Opcional):
   `python -m venv venv`
   `venv\Scripts\activate`

3. Instale as dependências do projeto na pasta raíz:

   `pip install -r requirements.txt`

4. Na pasta raíz rode o projeto, inicie a aplicação utilizando o comando:

   `uvicorn main:app --reload`

Esse comando compila o projeto, iniciando o cliente em:

> http://localhost:8000.

## ⚙️ Funcionamento:

Ao acessar a URL

> http://localhost:8000

A primeira rota/pagina (página principal) é apenas as boas vindas do projeto. Portanto nesse endereço acima, deverá aparecer:

`Seja bem vinda!`

## :page_facing_up: Documentação Swagger:

Nessa etapa também é possível acessar a documentação Swagger através da URL:

> http://localhost:8000/docs

Essa é uma documentação nativa da FastAPI. Para mais informações acesse a documentação a documentação [aqui](https://fastapi.tiangolo.com/tutorial/first-steps/#interactive-api-docs).

## 💻 Divisão do Projeto:

O projeto foi arquitetado em pastas, onde cada pasta possui arquivos com responsabilidades própria.
A divisão de pastas foi feita da seguinte forma:

- <b>Controllers:</b> Possui o controle das rotas.
- <b>Models:</b> Ações relacionadas a alterações no banco de dados.
- <b>Regras:</b> Definições de regras de negócio
- <b>Routers:</b> Armazena a configuração de rota principal.
- <b>Schemas:</b> Declaração de classes onde é feita a interface dos objetos trabalhados ao longo do projeto.
- <b>Server:</b> É onde é feita as configurações da nosso _database_, assim como as definições das nossas coleções.

Já a divisão das responsabilidades são:

- <b>User: Catiussia e Lya</b>
- <b>Address: Manuela e Maíra</b>
- <b>Products: Marcella</b>
- <b>Carts: Maíra e Lya</b>

## :globe_with_meridians: Rotas e endpoints:

Os endpoints disponíveis são:

1. Home

- GET / --> pagina inicial

2. Users

- POST/api/user --> cria um novo usuário

- GET/api/user/{email} --> faz busca de um usuário pelo email cadastrado

3. Address

- POST api/address/{id_user} --> adiciona um novo endereço ao usuário
- GET api/address/{email} --> faz busca do endereço através do email que for passado como parâmetro

4. Cart

- POST api/cart/{id_user}/{id_product} --> adicionar um carrinho passando um usuario e um produto como pamâmetro


## :rocket: Desenvolvedoras: 

<table>
    <tr align="center">
       <td>
            <a href="https://github.com/catiuu" target="_blank">
              <img src="https://avatars.githubusercontent.com/u/85588757?v=4" height="150px">
            </a>
        </td>
        <td>
          <a href="https://github.com/lyacarolina" target="_blank">
            <img src="https://avatars.githubusercontent.com/u/38046847?v=4" height="150px">
          </a>
        </td>
        <td>
            <a href="https://github.com/makuntz" target="_blank">
              <img src="https://avatars.githubusercontent.com/u/75498529?v=4" height="150px">
            </a>
        </td>
        <td>
            <a href="https://github.com/manuelaagr" target="_blank">
              <img src="https://avatars.githubusercontent.com/u/112256271?v=4" height="150px">
            </a>
        </td>
         <td>
            <a href="https://github.com/MarcellaMenezes" target="_blank">
              <img src="https://avatars.githubusercontent.com/u/49349873?v=4" height="150px">
            </a>
        </td>
    </tr>
    <tr align="center">
        <td>
        <a href="https://github.com/catiuu" target="_blank">Catiussia Nascimento</a>
        </td>
        <td>
        <a href="https://github.com/lyacarolina" target="_blank">Lya Carolina</a>
        </td>
        <td>
        <a href="https://github.com/makuntz" target="_blank">Maíra Kuntz</a>
        </td>
         <td>
        <a href="https://github.com/manuelaagr" target="_blank">Manuela Rocha</a>
        </td>
        <td>
        <a href="https://github.com/MarcellaMenezes" target="_blank">Marcella Menezes</a>
        </td>
    </tr>
</table>