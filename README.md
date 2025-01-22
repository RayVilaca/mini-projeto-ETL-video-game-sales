# Projeto ETL de Vendas de Video Games

## Visão Geral

Este projeto é um pipeline ETL usando Apache Airflow para orquestrar a extração, transformação e carregamento (ETL) de dados de vendas de video games. Os dados são extraídos do Kaggle, transformados para limpar e filtrar os dados, validados usando Soda SQL e, em seguida, carregados em um bucket S3.

## Conteúdo do Projeto

O projeto Astro contém os seguintes arquivos e pastas:

- **dags**: Esta pasta contém os arquivos Python para as DAGs do Airflow.
  - `video-game-sales-dag.py`: Este DAG define o pipeline ETL para dados de vendas de video games.
- **Dockerfile**: Este arquivo contém uma imagem Docker do Astro Runtime versionada que fornece uma experiência diferenciada do Airflow. Se você quiser executar outros comandos ou substituições em tempo de execução, especifique-os aqui.
- **include**: Esta pasta contém quaisquer arquivos adicionais que você deseja incluir como parte do projeto. Está vazia por padrão.
- **packages.txt**: Instale pacotes de nível de sistema operacional necessários para o projeto adicionando-os a este arquivo. Está vazio por padrão.
- **requirements.txt**: Instale pacotes Python necessários para o projeto adicionando-os a este arquivo. Inclui:
  - `kagglehub`
  - `python-dotenv`
  - `apache-airflow-providers-amazon`
  - `soda-sql`
- **plugins**: Adicione plugins personalizados ou da comunidade para o projeto neste arquivo. Está vazio por padrão.
- **airflow_settings.yaml**: Use este arquivo apenas localmente para especificar Conexões, Variáveis e Pools do Airflow em vez de inseri-los na interface do Airflow enquanto você desenvolve DAGs neste projeto.
- **.env**: Este arquivo contém variáveis de ambiente usadas no projeto, como `BUCKET_NAME` e `KEY`.

## Começando

### Pré-requisitos

- Docker
- Astro CLI
- Credenciais da API do Kaggle

### Configuração

1. **Clone o repositório**:

   ```sh
   git clone git@github.com:RayVilaca/mini-projeto-ETL-video-game-sales.git
   cd mini-projeto-ETL-video-game-sales
   ```

2. **Configure as variáveis de ambiente**:
   Crie um arquivo [.env](http://_vscodecontentref_/0) no diretório raiz com o seguinte conteúdo:

   ```properties
   BUCKET_NAME=seu-nome-do-bucket
   KEY=data/video-game-sales.parquet
   ```

3. **Instale as dependências**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Inicie o Airflow**:

   ```sh
   astro dev start
   ```

5. **Acesse a interface do Airflow**:
   Abra seu navegador e vá para `http://localhost:8080`. Use as credenciais padrão (`admin`/`admin`) para fazer login.

### Executando o DAG

1. **Dispare o DAG**:
   Na interface do Airflow, navegue até o DAG `airflow_video_game_sales` e dispare-o manualmente.

2. **Monitore o DAG**:
   Monitore o progresso do DAG na interface do Airflow. Você pode verificar os logs de cada tarefa para ver informações detalhadas.

## Estrutura do Projeto

- **Extract**: Baixa dados de vendas de video games do Kaggle.
- **Transform**: Limpa e filtra os dados.
- **Validate**: Usa Soda SQL para validar a qualidade dos dados.
- **Load**: Carrega os dados transformados em um bucket S3.

## Contribuindo

Se você quiser contribuir para este projeto, por favor, faça um fork do repositório e crie um pull request com suas alterações.
