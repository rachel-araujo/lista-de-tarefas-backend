# Projeto Lista de Tarefas - Backend

### Objetivo

Este é o backend da aplicação Lista de Tarefas, desenvolvido em Flask com SQLAlchemy.

1. Criar uma API RESTful para manipulação das tarefas (CRUD).
2. Utilizar um banco de dados para armazenar as tarefas(SQLAlchemy)
3. Implementar endpoints para:
    - Listar todas as tarefas
    - Adicionar uma nova tarefa
    - Marcar uma tarefa como completa
    - Remover uma tarefa
  
      
![image](https://github.com/rachel-araujo/lista-de-tarefas-backend/assets/79382072/53ff4142-e134-476d-a9a3-eef39f57322a)

# Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python (versão 3.6 ou superior)
- pip (gerenciador de pacotes do Python)
  
Recomenda-se também utilizar um ambiente virtual para isolar as dependências do projeto. Para criar um ambiente virtual, execute:

`python -m venv venv` 

Ative o ambiente virtual:

- No Windows:
  `venv\Scripts\activate`

- No macOS e Linux:
  `source venv/bin/activate`

### Configuração do Banco de Dados

O projeto utiliza SQLite como banco de dados. Para criar o banco de dados e suas tabelas, execute:

`python app.py`

### Executando o Servidor
`python app.py`

O servidor será iniciado em http://localhost:5000/.

# Rotas da API

- GET /api/tasks: Retorna todas as tarefas cadastradas.
- POST /api/tasks: Adiciona uma nova tarefa.
- PUT /api/tasks/<task_id>: Marca uma tarefa como concluída.
- DELETE /api/tasks/<task_id>: Deleta uma tarefa.
