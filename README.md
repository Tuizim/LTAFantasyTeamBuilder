# LTAFantasy

Este é o projeto LTAFantasy, que inclui serviços desenvolvidos em **Java** e **Python** para gerenciar e processar dados relacionados a jogadores. O projeto utiliza **Docker** para orquestrar os containers e também utiliza variáveis de ambiente e um ambiente virtual Python (venv) para facilitar o desenvolvimento.

## Índice

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Variáveis de Ambiente (.env)](#variáveis-de-ambiente-env)
- [Configuração do Ambiente Virtual Python](#configuração-do-ambiente-virtual-python)
- [Execução](#execução)
- [Testes](#testes)
- [Limpeza de Containers](#limpeza-de-containers)

---

## Requisitos

Antes de iniciar, certifique-se de ter as seguintes ferramentas instaladas:

- **Docker** e **Docker Compose**
- **Python 3.x**
- **pip** (gerenciador de pacotes Python)
- **Git** (para clonar o repositório)

---

## Instalação

1. **Clone o repositório:**

   Se você ainda não tem o repositório clonado, faça isso com o comando:

   ```bash
   git clone https://github.com/usuario/LTAFantasy.git
   cd LTAFantasy
   ```

2. **Crie o arquivo `.env`:**

   O arquivo `.env` contém as variáveis de ambiente usadas tanto pela API Python quanto pela API Java. Copie o modelo do `.env.example` (caso exista) ou crie o seu próprio arquivo `.env`.

   Exemplo de um `.env` básico:

   ```env
   # .env

   # Banco de dados PostgreSQL
   POSTGRES_DB=ltadb
   POSTGRES_USER=usuario
   POSTGRES_PASSWORD=senha

   # API Java
   API_JAVA_HOST=ltafantasy-api
   API_JAVA_PORT=8080
   ```

   O **`POSTGRES_DB`**, **`POSTGRES_USER`** e **`POSTGRES_PASSWORD`** são usados para configurar o banco de dados PostgreSQL.  
   **`API_JAVA_HOST`** e **`API_JAVA_PORT`** são usados para definir onde a API Java estará rodando (dentro do Docker, usamos o nome do serviço Docker `ltafantasy-api`).

---

## Variáveis de Ambiente (.env)

As variáveis de ambiente são usadas para armazenar informações sensíveis e configurações necessárias para o funcionamento do sistema. Elas são carregadas automaticamente pela aplicação ao iniciar.

### Principais variáveis que você pode encontrar no arquivo `.env`:

- **`POSTGRES_DB`**: Nome do banco de dados.
- **`POSTGRES_USER`**: Usuário do banco de dados.
- **`POSTGRES_PASSWORD`**: Senha do banco de dados.
- **`API_JAVA_HOST`**: O host onde a API Java estará rodando (no Docker, deve ser o nome do serviço, como `ltafantasy-api`).
- **`API_JAVA_PORT`**: A porta onde a API Java estará acessível.
- **Outras variáveis específicas** podem ser adicionadas conforme a necessidade do projeto.

---

## Configuração do Ambiente Virtual Python

### 1. **Criando o Ambiente Virtual (venv)**

Dentro da pasta do projeto(LTAFantasyTeamBuilder), você pode criar um ambiente virtual Python para a API Python (usando a biblioteca `venv`). Isso é importante para garantir que as dependências sejam isoladas do resto do sistema.

Execute os seguintes comandos:

```bash
# Criação do venv
python3 -m venv venv

# Ativando o venv
# No Linux ou MacOS:
source venv/bin/activate
# No Windows:
venv\Scripts\activate
```

Isso ativa o ambiente virtual, e você verá algo como `(venv)` no início da linha de comando, indicando que o venv está ativo.

### 2. **Instalando as dependências**

Depois de ativar o ambiente virtual, instale as dependências necessárias que estão no arquivo `requirements.txt`:

```bash
pip install -r LTAFantasyInteligence/requirements.txt
```

Isso vai instalar todos os pacotes necessários para a API Python funcionar corretamente.

---

## Execução

Para executar o projeto no ambiente Docker, você pode usar o Docker Compose. O Docker Compose vai orquestrar os containers para a API Java, a API Python e o banco de dados PostgreSQL.

1. **Inicie os containers Docker com o Docker Compose**:

   No diretório raiz do projeto, execute:

   ```bash
   docker-compose up --build
   ```

   Isso vai construir e rodar os containers definidos no arquivo `docker-compose.yml`. O Docker vai:

   - Rodar o banco de dados PostgreSQL na porta `5433`.
   - Subir a API Java na porta `8080`.
   - Subir a API Python na porta `8000`.

2. **Acessar a API Python diretamente**:

   Após subir os containers, a API Python estará disponível na porta `8000` e a API Java na porta `8080`.

---

## Testes

Para testar se as APIs estão funcionando corretamente, você pode usar o `curl` ou qualquer outro cliente HTTP.

Exemplo de teste da API Python:

```bash
curl http://localhost:8000/jogadores?sortBy=nickname&ordem=asc
```

Isso deve retornar uma resposta da API Python.

Para testar a integração com a API Java (se necessário):

```bash
curl http://localhost:8080/jogadores?sortBy=nickname&ordem=asc
```

Isso vai chamar a API Java, que pode fornecer dados sobre os jogadores.

---

## Limpeza de Containers

Quando você quiser parar e remover os containers, redes e volumes criados pelo `docker-compose up`, você pode usar o comando:

```bash
docker-compose down --remove-orphans
```

O `--remove-orphans` serve para garantir que **containers órfãos** (aqueles que não estão mais definidos no seu arquivo `docker-compose.yml`) sejam removidos, mantendo seu ambiente Docker limpo.

---

## Contribuindo

Se você deseja contribuir para o projeto, faça o seguinte:

1. Fork o repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça suas modificações.
4. Envie um pull request para a branch `main`.

---

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
