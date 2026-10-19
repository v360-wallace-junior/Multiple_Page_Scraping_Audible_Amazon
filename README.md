# Scraping de livros na Audible

Pequeno projeto em Python que usa Selenium para coletar informações dos livros
exibidos na página de busca da Audible Brasil e exportá-las para um arquivo CSV.

## O que o script faz

O arquivo [`main.py`](./main.py):

1. Abre `https://www.audible.com.br/search` no Google Chrome.
2. Aguarda até 10 segundos pelo carregamento da área de resultados.
3. Extrai o título, a autoria e a duração dos itens encontrados na página.
4. Salva os dados em `books.csv`, substituindo o arquivo caso ele já exista.
5. Fecha o navegador ao terminar, inclusive se ocorrer um erro.

> **Escopo atual:** apesar do nome do projeto, o script coleta apenas os
> resultados presentes na página inicial da busca. Ele não navega por páginas
> seguintes nem aplica filtros de pesquisa.

## Requisitos

- Python 3.10 ou superior.
- Google Chrome instalado.
- Pacotes Python `selenium` e `pandas`.

O Selenium 4 pode gerenciar automaticamente o ChromeDriver compatível por meio
do Selenium Manager. Na primeira execução, pode ser necessário acesso à internet
para baixar o driver.

## Instalação

No terminal, na pasta do projeto, crie e ative um ambiente virtual (opcional,
mas recomendado):

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows PowerShell, ative-o com:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install selenium pandas
```

## Execução

Com o ambiente virtual ativado, execute na pasta do projeto:

```bash
python main.py
```

O resultado será gravado em `books.csv`, no diretório de onde o comando foi
executado. O CSV contém as colunas:

| Coluna | Conteúdo |
| --- | --- |
| `title` | Título do livro |
| `author` | Texto de autoria apresentado pela Audible |
| `length` | Duração apresentada pela Audible |

## Observações

- O script depende dos seletores HTML usados atualmente pela Audible; alterações
  no site podem exigir ajustes em `main.py`.
- A coleta depende de conexão com a internet e de a página de busca estar
  acessível.
- Use a automação de forma responsável e respeite os termos de uso e as políticas
  do site.
