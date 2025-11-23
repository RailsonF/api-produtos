# 📦 Catálogo de Produtos 

Bem-vindo à API de Catálogo de Produtos!
Este projeto foi desenvolvido com foco em **segurança, organização e simplicidade**, utilizando:

* **FastAPI** — Backend rápido e tipado
* **Supabase Auth** — Autenticação e geração de JWT
* **PostgREST** — CRUD automático direto no banco
* **Supabase Postgres** — Banco de dados em nuvem
* **Render** — Deploy

---

### 🌐 Acessando a API

A API está publicada no Render.

> **URL base da API:**

```
https://api-produtos-jdw9.onrender.com
```
**🔴🔴OBS: Se demorar a carregar é por que o render deixa o projeto suspenso quando não está sendo utilizado, a primeira chamada pode demorar de 30 a 50 segundos**

### 📄 Documentação Interativa (Swagger)

Acesse:

```
https://api-produtos-jdw9.onrender.com/docs
```

A interface Swagger permite: </br>
✔ Testar todas as rotas </br>
✔ Preencher requisições </br>
✔ Enviar tokens </br>
✔ Visualizar respostas </br>
✔ Explorar erros </br>

---

# 🔑 Autenticação (Supabase Auth)

Toda autenticação é feita **no Supabase**, e **a API não cria usuários na mão**.
Existe **registro** e **login**, e cada login retorna um **JWT** usado nas requisições.

### 1️⃣ Criando um Usuário (`POST /auth/register`)

* Abra a rota **`/auth/register`** na interface da documentação
* Clique em **Try it out**
* Envie um corpo JSON como:

```json
{
  "email": "seuemail@teste.com",
  "password": "suasenha123"
}
```

* Clique em **Execute**

Se tudo estiver correto, você receberá um retorno confirmando a criação do usuário.
<img width="1452" height="417" alt="image" src="https://github.com/user-attachments/assets/172f6f7e-e0ad-4028-96f7-a9dd0471a474" />

---

### 2️⃣ Fazendo Login (`POST /auth/login`)

* Abra a rota **`/auth/login`**
* Clique em **Try it out**
* Envie:

```json
{
  "email": "seuemail@teste.com",
  "password": "suasenha123"
}
```

* Clique em **Execute**

Você receberá uma resposta contendo o **access_token**:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Copie apenas o token**, sem aspas.

---

###  3️⃣ Autorizando no Swagger

No canto superior direito da documentação, clique em **Authorize**:
<img width="1463" height="422" alt="login" src="https://github.com/user-attachments/assets/9462bc21-a9ee-422a-9a7a-c69e36234afe" />

Na janela que abrir, cole:

```
SEU_ACCESS_TOKEN_AQUI
```

E clique **Authorize**.
<img width="768" height="364" alt="authorize" src="https://github.com/user-attachments/assets/317edc9a-231c-42a6-b677-ed306eb0e06d" />

---

### 4️⃣ Testando as Rotas de Produtos

Após autorizar, você pode testar:

### ✔ Listar produtos

`GET /products/`

### ✔ Criar produto

`POST /products/`

### ✔ Atualizar produto

`PATCH /products/{product_id}`

### ✔ Deletar produto

`DELETE /products/{product_id}`

---

# Exemplo completo de criação de produto

1. Abra `POST /products/`
2. Clique **Try it out**
3. No campo **Authorization**, coloque:

```
Bearer SEU_ACCESS_TOKEN_AQUI
```

4. No corpo da requisição, envie:

```json
{
  "nome": "Processador Intel Core i5 10400F",
  "preco": 799.00,
  "estoque": 15,
  "descricao": "6 núcleos, 12 threads, 4.3GHz Max Turbo"
}
```

5. Clique **Execute**.

<img width="1456" height="830" alt="rotas" src="https://github.com/user-attachments/assets/30171bc5-773c-4309-9484-cdd4ff241f72" />


---

# 🔴🔴Observações importantes

* **Sem o token JWT, todas as rotas de produtos retornam 401 Unauthorized**
* O header deve SEMPRE ser enviado como:

```
Authorization: Bearer <seu_token>
```

* Cada produto fica vinculado a **um usuário específico**, então:

  * Usuário A só vê os próprios produtos
  * Usuário B não acessa produtos de A

---

# 📁 Estrutura do Projeto

```
app/
 ├─ dependencies/
 │   ├─ router.py         → Contém as definições das rotas da APi
 ├─ routes/
 │   ├─ auth_routes.py         → Define as rotas relacionadas à autenticação, como registro e login de usuários
 │   └─ products-routes.py        → Define as rotas para operações CRUD (Criar, Ler, Atualizar, Deletar) relacionadas aos produtos
 ├─ utils/
 │   └─ supabase_jwt.py   → validação e extração de claims do JWT
 ├─ schemas/
 │   └─ product_schema.py           → Define os esquemas para criação, atualização e resposta de produtos, garantindo que os dados estejam no formato correto
 ├─ services/
 │   └─ product_service.py   → Implementa funções para listar, criar, atualizar e deletar produtos, utilizando a API do Supabase
 ├─ utils/
 │   └─ convert_decimal.py   → Contém a função serialize_payload, que converte valores do tipo Decimal para float antes de enviar para o Supabase.
 │   └─ jwt_tools.py        → Contém a função extract_user_id_from_jwt, que extrai o ID do usuário do token JWT.
 ├─ main.py
 └─ config.py
```
