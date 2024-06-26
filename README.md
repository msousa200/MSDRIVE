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

- **static/**: Arquivos estáticos como CSS, JavaScript e imagens.
  - **drive/css/style.css**: Estilos principais para a aplicação.

### Descrição das Funcionalidades

- **Autenticação**: Registro, login e logout de usuários.
- **Gestão de Diretórios e Arquivos**: Criação de diretórios, upload de arquivos, listagem de documentos e exclusão de arquivos.
- **Templates Reutilizáveis**: Uso de templates base para manter a consistência visual.
- **Segurança**: Middleware para redirecionar automaticamente os administradores para a página de administração após o login.

## Processo de Instalação

### Pré-requisitos

- Python 3.x
- Virtualenv
- Make

### Passos de Instalação

1. **Clone o Repositório**

    ```sh
    git clone https://github.com/msousa200/MSDRIVE
    cd ms_drive
    ```

2. **Crie e Ative o Ambiente Virtual**

    ```sh
    make venv
    source venv/bin/activate
    ```

3. **Instale as Dependências**

    ```sh
    make install
    ```

4. **Configure as Variáveis de Ambiente**

    Crie um arquivo `.env` na raiz do projeto e configure as variáveis necessárias, como `SECRET_KEY` e configurações do banco de dados.

5. **Aplique as Migrações**

    ```sh
    make migrate
    ```

6. **Execute o Servidor de Desenvolvimento**

    ```sh
    make run
    ```

### Comandos do Makefile

- **venv**: Cria o ambiente virtual.
- **install**: Instala as dependências do projeto listadas em `requirements.txt`.
- **migrate**: Aplica as migrações do banco de dados.
- **run**: Executa o servidor de desenvolvimento.

## Exemplo de Makefile

```makefile
VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
DJANGO_MANAGE := $(PYTHON) manage.py

venv:
    python3 -m venv $(VENV)

install: venv
    $(PIP) install -r requirements.txt

migrate: install
    $(DJANGO_MANAGE) migrate

run: migrate
    $(DJANGO_MANAGE) runserver

clean:
    find . -name '*.pyc' -delete
    find . -name '__pycache__' -delete
