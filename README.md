# Crawler Teste

O projeto consiste em desenvolver e testar o modulo de Crawler com a biblioteca Selenium.

## Configuração de Ambiente
- As informações de ambiente se encontram no arquivo `.settings.ini`
- As informações de bibliotecas se encontram no arquivo `requirements.txt`

### Estrutura de Diretorios

- `app` (Scripts referentes ao projeto)
- `log`  (Pasta para armazenar os logs de execução do projeto)
- `download` (Pasta para receber os downloads do projeto)

#### Scripts 
- `Configs.py` - Metodos referente a configuração inicial do projeto
- `Crawler.py` - Metodos referentes a interação com o Browser
- `Files.py` - Metodos referente a interação com diretorios e arquivos
- `Log.py` - Metodos referentes a todo o gerenciamento e criação de Logs

### Requisitos para Execução

- instale o google chrome - https://www.google.com/chrome/
- instale o python anaconda - https://www.anaconda.com/download
- instale as bibliotecas listadas no arquivo `requirements.txt` pelo pip

### Como Executar

- abra um prompt do anaconda e digite os comandos abaixo em ordem
- cd `caminho para a pasta app`
- python app_test_crawler.py
