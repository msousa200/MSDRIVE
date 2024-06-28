# Projeto MS-DRIVE

## Objetivo

O projeto MS-DRIVE é um sistema de gerenciamento de arquivos desenvolvido com Django. Ele permite aos usuários registrar-se, fazer login, criar diretórios, fazer upload de arquivos e gerenciar seus documentos de forma organizada.

## Organização do Projeto

### Estrutura de Diretórios

- **ms_drive/**: Pasta raiz do projeto que contém a configuração principal do Django.
  - **settings.py**: Configurações globais do Django.
  - **urls.py**: Configurações de roteamento de URLs principais.
  - **wsgi.py**: Configurações WSGI para o servidor web.

- **drive/**: Aplicação que gerencia a autenticação e o perfil dos usuários.
  - **migrations/**: Arquivos de migração do banco de dados.
  - **templates/drive/**: Templates HTML para login, registro e redefinição de senha.
  - **models.py**: Modelos de dados para a aplicação de autenticação.
  - **views.py**: Lógica das views para autenticação e gerenciamento de perfis.
  - **urls.py**: Configurações de roteamento para a aplicação de autenticação.

- **filemanage/**: Aplicação que gerencia diretórios e arquivos dos usuários.
  - **migrations/**: Arquivos de migração do banco de dados.
  - **templates/filemanage/**: Templates HTML para operações de gerenciamento de arquivos.
  - **models.py**: Modelos de dados para diretórios e documentos.
  - **views.py**: Lógica das views para operações de upload, listagem, download e exclusão de arquivos.
  - **urls.py**: Configurações de roteamento para a aplicação de gerenciamento de arquivos.

- **static/**: Arquivos estáticos como CSS e imagens.
  - **drive/css/style.css**: Estilos principais para a aplicação.

### Descrição das Funcionalidades

- **Autenticação**: Registro, login e logout de usuários.
- **Gestão de Diretórios e Arquivos**: Criação de diretórios, upload de arquivos, listagem de documentos e exclusão de arquivos.
- **Templates Reutilizáveis**: Uso de templates base para manter a consistência visual.
- **Segurança**: Middleware para redirecionar automaticamente os administradores para a página de administração após o login.

## Processo de Instalação

### Pré-requisitos

- Python 3.x
- Make
- Docker
- Docker Compose

### Passos de Instalação

1. **Clone o Repositório**

    ```sh
    git clone https://github.com/msousa200/MSDRIVE
    cd ms_drive
    ```

2. **Instale as Dependências**

    ```sh
    pip install -r requirements.txt
    ```

3. **Configure as Variáveis de Ambiente**

    Crie um arquivo `.env` na raiz do projeto e configure as variáveis necessárias, como `SECRET_KEY` e configurações do banco de dados.

4. **Aplique as Migrações**

    ```sh
    make migrate
    ```

5. **Execute o Servidor de Desenvolvimento**

    ```sh
    make run
    ```

### Comandos do Makefile

- **install**: Instala as dependências do projeto listadas em `requirements.txt`.
- **migrate**: Aplica as migrações do banco de dados.
- **run**: Executa o servidor de desenvolvimento.
- **clean**: Remove arquivos compilados Python.

### Comandos para Docker Compose

Para rodar o projeto usando Docker Compose:

1. **Iniciar os serviços:**
    ```sh
    docker compose up
    ```

2. **Parar os serviços:**
    ```sh
    docker compose down
    ```


