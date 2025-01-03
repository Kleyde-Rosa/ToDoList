# Todo List CLI Application

Este é um aplicativo de linha de comando (CLI) para gerenciar tarefas (To-Do list). O projeto permite adicionar, marcar como concluídas e listar tarefas, além de possibilitar que o usuário visualize tarefas concluídas e não concluídas.

## Funcionalidades

- **Adicionar Tarefas**: Adiciona uma nova tarefa à lista.
- **Marcar como Concluída**: Marca uma tarefa como concluída.
- **Listar Tarefas Concluídas**: Exibe todas as tarefas marcadas como concluídas.
- **Listar Tarefas Não Concluídas**: Exibe todas as tarefas que ainda não foram concluídas.
- **Sair**: Permite que o usuário saia do aplicativo.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
.
├── models/
│   └── task.py            # Definição da classe Task
├── repositories/
│   └── task_repository.py # Definição do repositório Task
├── services/
│   └── todo_service.py    # Lógica de gerenciamento de tarefas
├── ui/
│   └── console_ui.py      # Interface de linha de comando para interação
├── main.py                # Arquivo de entrada
└── README.md              # Este arquivo
```

## Requisitos

- Python 3.x

## Instalação

Clone o repositório para o seu computador:

```bash
git clone https://github.com/jrdimande/ToDoList
```

Navegue até o diretório do projeto:

```bash
cd ToDoList/src
```

## Como Usar

1. Execute o aplicativo:

```bash
python3 main.py
```

2. No terminal, você verá o menu com as opções. Digite o número da opção desejada e pressione `Enter`:

- `1` - Adicionar tarefa
- `2` - Marcar tarefa como concluída
- `3` - Listar tarefas concluídas
- `4` - Listar tarefas não concluídas
- `q` - Sair do aplicativo

## Exemplo de Uso

1. **Adicionar Tarefa**:

   O sistema pedirá o nome da tarefa. Você pode inserir algo como:

   ```bash
   Enter task name: Estudar Python
   ```

2. **Marcar Tarefa como Concluída**:

   O sistema pedirá o nome da tarefa que você deseja marcar como concluída. Exemplo:

   ```bash
   Enter task name: Estudar Python
   ```

3. **Listar Tarefas Concluídas**:

   O sistema mostrará todas as tarefas que foram marcadas como concluídas.

4. **Listar Tarefas Não Concluídas**:

   O sistema mostrará todas as tarefas que ainda não foram concluídas.
