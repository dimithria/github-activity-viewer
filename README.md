# Visualizador de Atividade do GitHub

## Introdução
Esse é um código em Python que permite visualizar as atividades recentes de um usuário no GitHub. Usando a API do GitHub, o código busca eventos relacionados a um usuário específico e os exibe de forma organizada.

---

## Key Concepts

Alguns conceitos-chave:

- **API do GitHub**: Uma interface que permite interagir com os dados do GitHub, como repositórios, usuários e eventos.
- **Eventos**: Ações realizadas por um usuário, como commits, criação de repositórios, e muito mais.
- **Requests**: Uma biblioteca Python que facilita fazer requisições HTTP.

---

## Code Structure

O código é estruturado em funções que realizam tarefas específicas:

- `get_github_activity(username)`: Busca e exibe as atividades do usuário.
- `format_date(date_str)`: Formata a data recebida da API para um formato mais legível.

---

## Explicação do Código

## 1 Importações
O código começa importando as bibliotecas necessárias:

- `requests` para fazer chamadas à API  
- `datetime` para manipulação de datas  


## 2 Função `get_github_activity`

- Recebe o nome de usuário como parâmetro  
- Constrói a URL da API e faz uma requisição GET  
- Verifica se a resposta é bem-sucedida (status 200). Se não, exibe uma mensagem de erro  
- Se não houver eventos, informa que nenhuma atividade foi encontrada  
- Para cada evento, exibe:
  - O tipo  
  - O repositório  
  - A data formatada  

## 3 Detalhes dos Eventos
Para cada tipo de evento, o código verifica e exibe informações adicionais, como:

- Commits em um `PushEvent`  
- Ações em um `IssuesEvent`  


## 4 Função `format_date`

Converte a string de data recebida da API para um formato mais legível: (DD/MM/AAAA HH:MM).

## 5 Execução do Programa:  
O bloco `if __name__ == "__main__` permite que o código seja executado diretamente, solicitando ao usuário o nome de usuário do GitHub.

---

## Conclusão
Esse código é uma ótima maneira de interagir com a API do GitHub e visualizar as atividades de um usuário. Com algumas modificações, você pode expandir suas funcionalidades, como adicionar mais filtros ou exibir mais informações. Experimente e veja como você pode personalizar!!
