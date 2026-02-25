# a_p_i_kako

---


# 📚 API de Gerenciamento de Aulas

API desenvolvida em **Flask** para gerenciamento de **cadastro e confirmação de presença em aulas**, com dois tipos de usuários:

- 👨‍🏫 Professor
- 🎓 Aluno

> ⚠️ Este projeto ainda está em desenvolvimento.

---

## 🚀 Tecnologias utilizadas

- Python 3.x
- Flask
- MySQL
- mysql-connector-python

---
## 📁 Estrutura do projeto

```

a_p_i_kako
├── aluno
│   ├── __init__.py
│   └── routes
│       ├── __init__.py
│       └── one.py
├── api
│   ├── config
│   │   ├── __init__.py
│   │   └── vl.py
│   ├── db
│   │   ├── config
│   │   │   ├── __init__.py
│   │   │   ├── l.txt
│   │   │   ├── professor.py
│   │   │   └── rb_aln.py
│   │   ├── __init__.py
│   │   ├── pr.py
│   │   └── tp_aln.py
│   ├── __init__.py
│   ├── k.py
│   ├── models
│   │   ├── aln.py
│   │   └── __init__.py
│   └── routes
│       ├── aln.py
│       ├── __init__.py
│       ├── prfssr.py
│       └── teste.py
├── interessante.txt
├── professor
│   ├── __init__.py
│   └── routes
│       ├── __init__.py
│       ├── teste.py
│       └── vrss_antigas
│           └── t.py
├── README.md
├── requirements.txt
└── run.py


```


> A estrutura pode ser modificada conforme o projeto evoluir.

---

## ⚙️ Como executar o projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/Pablo-sltv-Dev/a_p_i_kako.git
```

---

### 2️⃣ Crie e ative um ambiente virtual

```bash
python -m venv venv
```

**Windows**

```bash 
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure o banco de dados

* Banco: **MySQL**
* Criado via **MySQL Workbench**
* Conexão feita com `mysql-connector-python`

Exemplo de conexão:

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="nome_do_banco"
)
```

---

### 5️⃣ Execute a aplicação

```bash
python app.py
```

A API estará disponível em:

```bash
http://localhost:5000

```

---

## 📌 Endpoints da API

### 👨‍🏫 Professor

#### ➤ Teste de conexão

**GET** `/professor/teste`

📄 Descrição:
Endpoint utilizado para verificar se a API está funcionando corretamente.

📤 Resposta esperada:

```json
{
  "status": "ok",
  "message": "Conexão realizada com sucesso"
}
```

---

#### ➤ Cadastro do professor

**POST** `/mtrcl/dc`

📄 Descrição:
Rota responsável pelo cadastro do professor.

> Atualmente existe apenas **um professor** no sistema.

📥 Body (JSON):

```json
{
  "nome": "Nome do professor",
  "email": "email@exemplo.com",
  "senha": "senha123"
}
```

📤 Resposta esperada:

```json
{
  "message": "Professor cadastrado com sucesso"
}
```

---

### 🎓 Aluno

#### ➤ Login do aluno

**POST** `/aln_bjj/vrfcc/`

📄 Descrição:
Realiza a verificação das credenciais do aluno e efetua o login.

📥 Body (JSON):

```json
{
  "email": "aluno@exemplo.com",
  "senha": "senha123"
}
```

📤 Resposta esperada:

```json
{
  "message": "Login realizado com sucesso",
  "aluno_id": 1
}
```

---

## ❌ Possíveis erros

| Código | Descrição                |
| ------ | ------------------------ |
| 400    | Dados inválidos          |
| 401    | Credenciais incorretas   |
| 404    | Usuário não encontrado   |
| 500    | Erro interno do servidor |

---

## 🧪 Testes da API

Os endpoints podem ser testados usando:

* Postman


---

## 🚧 Status do projeto

🔧 **Em desenvolvimento**

Funcionalidades futuras planejadas:

* Cadastro de alunos
* Confirmação de presença
* Controle de aulas
* Autenticação com tokens
* Organização em Blueprints

---

## 👩‍💻 Autor(a)

Projeto desenvolvido por **Pablo Solotv**
🔗 GitHub: [https://github.com/seu-usuario](https://github.com/Pablo-sltv-Dev)





