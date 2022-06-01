<p align="center">
 <img src="https://raw.githubusercontent.com/Henrique0501/Meu_Portfolio/main/static/Logo_HM.png">
</p>
<h1 align="center">API_de_Imoveis</h1>
<p align="center">
 <img style="display: inline-block" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
 <img style="display: inline-block" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
 <img style="display: inline-block" src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white">
</p>

Um exemplo simplório de API Rest em Flask tratando de imóveis.

<h2>Descrição</h2>

<p>Essa API foi construída a partir microframework Flask.</p>
<p>Para integração com o banco de dados utilizou-se o ORM SQLAlchemy.</p>
<p>Para os processos de serialização e desserialização foi utilzado o framework Marshmallow.</p>
<p>Para os processos de autenticação utilizou-se a extensão flask_jwt_extended.</p>
<br>
<p>A API está totalmente documentada de acordo com os padrões Open API 3.0.0 na plataforma Swagger.</p>

---

## :bust_in_silhouette: Rotas de autenticação
**Arquivos relacionados:** <a href="https://github.com/Henrique0501/API_de_Imoveis/blob/main/app/authentication.py">app/authentication.py</a> e <a href="https://github.com/Henrique0501/API_de_Imoveis/blob/main/app/user_model.py">app/user_model.py</a>
<h3>POST: /api/auth/register</h4>
 Qualquer pessoa pode fazer um cadastro informando um username, uma senha e opcionalmente um id.
<h3>POST: /api/auth/login</h4>
 Use o username e a senha informados na rota de cadastro para obter um token de autenticação.
<br>

## :computer:Rotas da API
**Arquivos relacionados:**
<a href="https://github.com/Henrique0501/API_de_Imoveis/blob/main/app/api_views.py">app/api_views.py</a> e <a href="https://github.com/Henrique0501/API_de_Imoveis/blob/main/app/imovel_model.py">app/imovel_model.py</a>


  <h3>GET: /api/imoveis/search</h3>
  
  
  <p>Essa rota é desprotegida. Qualquer pessoa pode acessar os imóveis cadastrados com ou sem um filtro.</p>
  <p>Os parâmetros de filtros são passados na query da URL:</p>
  <ul>
   <li>place: Localidade do imóvel</li>
   <li>area: Área igual a</li>
   <li>area_bg_th: Área maior que</li>
   <li>area_sm_th: Área menor que</li>
   <li>rooms: Quantidade de quartos igual a</li>
   <li>rooms_bg_th: Quantidade de quartos maior que</li>
   <li>rooms_sm_th: Quantidade de quartos menor que</li>
   <li>garages: Quantidade de vagas na garagem igual a</li>
   <li>garages_bg_th: Quantidade de vagas maior que</li>
   <li>garages_sm_th: Quantidade de vagas menor que</li>
   <li>price: Preço do imóvel igual a</li>
   <li>price_bg_th:Preço do imóvel maior que</li>
   <li>price_sm_th:Preço do imóvel menor que</li>
  </ul>
  <p>Exemplo:</p>
  
  ```
  /api/imoveis/search?area_bg_th=400&price_sm_th=900000.0
  ```
  
  Isso retorna todos os imóveis com área maior que 400 m<sup>2</sup> e preço menor que R$ 900000,00.
  
  <h4>POST: /api/imoveis/register</h4>
  <p>Rota protegida.</p> 
  <p>Registra um novo imóvel</p>
  
  <h4>PUT:/api/imoveis/update/{id}</h4>
  <p>Rota protegida.</p> 
  <p>Altera um imóvel já registrado</p>
  
  <h4>DELETE: /api/imoveis/delete/{id}</h4>
  <p>Rota protegida.</p>
  <p>Deleta umimóvel já registrado</p>
  
## :memo: Documentação


**Rota: /api/docs**

**Arquivos relacionados:** <a href="https://github.com/Henrique0501/API_de_Imoveis/blob/main/app/static/swagger.yaml">app/static/swagger.yaml</a>

A documentação foi feita no formato .yaml seguindo os padrões Open API 3.0.0
