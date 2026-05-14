# Visualizador de Atividades do GitHub

## 📋 Descrição
Aplicação desktop que permite visualizar as atividades recentes de qualquer usuário do GitHub através de uma interface gráfica intuitiva. O programa utiliza a API pública do GitHub para buscar e exibir eventos como commits, criação de repositórios, forks, issues e muito mais.

---

## ✨ Características
- **Interface Gráfica Moderna**: Desenvolvida com Tkinter, oferece uma experiência amigável
- **Busca em Tempo Real**: Consulta a API do GitHub para obter dados atualizados
- **Exibição Estruturada**: Mostra as 10 atividades mais recentes do usuário
- **Tipos de Eventos Suportados**:
  - 📤 Push (commits)
  - 🆕 Create (novas branches/tags)
  - 🔀 Fork
  - ⚠️ Issues
  - E muito mais!

---

## 🛠️ Requisitos
- Python 3.7 ou superior
- Bibliotecas Python: `tkinter`, `requests`, `datetime`

---

## 📦 Instalação

### 1. Clonar ou baixar o projeto
```bash
cd "github activity viewer"
```

### 2. Instalar as dependências
Execute o comando abaixo para instalar as bibliotecas necessárias:
```bash
pip install -r requeriments.txt
```

Ou instale manualmente:
```bash
pip install requests
```

---

## 🚀 Como Executar

### No Windows (PowerShell):
```powershell
python main.py
```

### No Windows (Prompt de Comando):
```cmd
python main.py
```

### No Linux/Mac:
```bash
python3 main.py
```

---

## 📝 Como Usar
1. **Execute o programa** usando os comandos acima
2. **Digite um nome de usuário** do GitHub na primeira área
3. **Clique em "Buscar"** ou pressione **Enter**
4. **Visualize as atividades** na área de resultados

### Exemplo:
Digite `torvalds` para ver as atividades de Linus Torvalds, ou `guido` para Guido van Rossum.

---

## 🏗️ Estrutura do Código

### Funções Principais
- **`get_github_activity()`**: Busca eventos da API do GitHub e os exibe na interface
- **`format_date()`**: Converte a data ISO (2026-05-14T16:10:00Z) para formato brasileiro (14/05/2026 16:10)

### Interface
- **Área 1 - Título**: "Visualizador de Atividades do GitHub"
- **Área 2 - Busca**: Campo de entrada para nome de usuário + botão Buscar
- **Área 3 - Resultados**: Exibição das atividades com barra de rolagem

---

## 🔍 Detalhes dos Eventos Exibidos
Para cada evento encontrado, o programa mostra:
- **Tipo**: PushEvent, CreateEvent, ForkEvent, IssuesEvent, etc.
- **Repositório**: Nome do repositório relacionado ao evento
- **Data**: Data e hora formatadas em padrão brasileiro
- **Detalhes adicionais**: Mensagens de commit, tipo de criação, ações em issues

---

## ⚠️ Observações
- A API do GitHub tem limite de requisições: 60 por hora para requisições não autenticadas
- Se não encontrar eventos, pode significar que o usuário não tem atividades públicas recentes
- A aplicação busca apenas as 10 atividades mais recentes