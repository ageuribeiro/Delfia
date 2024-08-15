# Document Manager System

Este projeto é um sistema de gestão de documentos criptografados, desenvolvido utilizando FastAPI para o backend e React para o frontend. O sistema permite que os usuários façam upload de documentos e os listem.

## Estrutura do Projeto

- **Backend (FastAPI)**: Responsável por gerenciar as operações do servidor, como upload e listagem de arquivos.
- **Frontend (React)**: Interface gráfica para o usuário interagir com o sistema, enviando e visualizando documentos.

## Pré-requisitos

Antes de iniciar o projeto, certifique-se de ter as seguintes ferramentas instaladas:

- **Python 3.8+**
- **Node.js e npm**: [Instale o Node.js](https://nodejs.org/)
- **Git**: [Instale o Git](https://git-scm.com/)

## Configuração do Backend

1. **Clone o Repositório**

   Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/document-manager.git
   cd document-manager
   
2. **Crie um Ambiente Virtual**

    Crie e ative um ambiente virtual Python:

    ```bash
    python -m venv venv_manage_files
    source venv_manage_files/bin/activate  # Para Linux/MacOS
    venv_manage_files\Scripts\activate     # Para Windows
    
3. **Instale as Dependências**

    Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    
4. **Executando o Backend**

    Para iniciar o servidor FastAPI:

   ```bash
   uvicorn api.main:app --reload

  O servidor estará disponível em http://127.0.0.1:8000.
  
5. **Configuração de CORS**

   O backend está configurado para permitir requisições do frontend. Se precisar restringir os domínios permitidos, edite a configuração CORS em api/main.py.

   
## Configuração do Frontend

1. **Instale as Dependências do Frontend**
   
   Navegue até a pasta do frontend e instale as dependências necessárias:

   ```bash
   cd document-manager-frontend
   npm install

   
2. **Executando o Frontend**
   Inicie o servidor de desenvolvimento React:

   ```bash
   npm start


  A interface será aberta em http://localhost:3000.

# Estrutura do Código
## Backend (api/main.py)
* ```bash
  api/main.py:
Ponto de entrada para a aplicação FastAPI, onde as rotas são definidas para upload e listagem de arquivos.

  * Rotas:
    * /upload: Rota para upload de arquivos. Recebe um arquivo via POST e o armazena no servidor.
    * /files: Rota para listar os arquivos disponíveis. Retorna uma lista de nomes de arquivos armazenados no servidor.
  * security.py: Gerencia a criptografia das senhas utilizando a biblioteca passlib.

## Frontend (src/components)
  * UploadPage.js: Página de upload de documentos. Contém um formulário para selecionar um arquivo e enviá-lo para o servidor.

    * Funções:
      * handleFileChange: Atualiza o estado com o arquivo selecionado.
      * handleUpload: Envia o arquivo selecionado para o servidor.

  * ListPage.js: Página de listagem de documentos. Exibe uma lista de arquivos armazenados no servidor.

    * Funções:
      *  useEffect: Faz uma requisição GET para obter a lista de arquivos assim que a página é carregada.
## Navegação
  * App.js: Configura as rotas utilizando react-router-dom.
    * /: Página principal para upload de documentos.
    * /list: Página para listar os documentos armazenados.

# Como Acessar o Sistema
* ## Backend:
    * Certifique-se de que o servidor FastAPI está rodando em http://127.0.0.1:8000.
* ## Frontend:
    * Acesse http://localhost:3000 em seu navegador para acessar a interface de usuário.

* ## Possíveis Erros e Soluções
    * Erro de Backend (bcrypt):
    * Se ocorrer um erro relacionado ao bcrypt, instale o backend necessário com:
    
    ```bash
    pip install bcrypt
* ## Erro de CORS:

   Caso tenha problemas com CORS, verifique as configurações no main.py do backend.

## Contribuições
    Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença
    Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
