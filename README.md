# BDD + TDD: To-Do List

## 1. Proposta do Projeto

Este é um projeto acadêmico desenvolvido com o objetivo principal de aplicar e praticar ativamente as metodologias de **BDD (Behavior-Driven Development)** e **TDD (Test-Driven Development)**.

O sistema é uma simples aplicação de To-Do List onde o foco não está na interface do usuário, mas no processo de desenvolvimento orientado a testes e comportamentos.

* **BDD:** Foi utilizado na fase inicial para definir o comportamento esperado da aplicação e refinar o escopo. Os cenários foram escritos em linguagem Gherkin para descrever o que o sistema deveria fazer do ponto de vista comportamental.
* **TDD:** Foi aplicado o ciclo de desenvolvimento (Red-Green-Refactor). Para cada funcionalidade, um teste unitário foi escrito *antes* da implementação do código de produção, garantindo que o desenvolvimento fosse guiado pelos testes.

**`Obs*: O relatório com os passos executados e documentados do TDD estão no arquivo relatorio.md`**

## 2. Design

O projeto foi desenvolvido em **Python**, seguindo princípios de **Orientação a Objetos (OOP)** para estruturar o código de forma clara e organizada.

* **OOP:** As responsabilidades são separadas, com a classe `Tarefa` (`Model/tarefa.py`) representando a entidade de dados e a classe `TarefaRepo` (`Repo/tarefa_repo.py`) atuando como um repositório que abstrai a lógica de negócios e o acesso ao banco de dados.
* **Banco de Dados:** Foi utilizado **SQLite** para persistência dos dados, com scripts de criação e limpeza (`db/db.py`).
* **Testes:** A suíte de testes foi construída com a biblioteca nativa `unittest` do Python.
* **Evidências:** Localizadas na pasta evi, o nome indica o caso de teste (ctx, onde x é o número do caso de teste), podendo ser acompanhado por "-s" caso indique que é uma evidência de sucesso, caso contrário, representa uma evidência de falha.

## BDD
Os **casos de teste** formulados e organizados através do **BDD** e **linguagem Gherking** foram: 

`CT1 -  Criar uma tarefa com dados válidos`\
**Dado** que tenho dados válidos para uma tarefa\
**Quando** chamo a função adicionar_tarefa(dados)\
**Então** a tarefa é efetivamente adicionada no banco de dados\
**E** é retornado True

`CT2 - Visualizar tarefas`\
**Dado** que existe ao menos uma tarefa registrada no banco de dados\
**Quando** chamo a função visualizar_tarefas()\
**Então** é retornado uma lista com as tarefas\

`CT3 - Criar uma tarefa com dados incorretos`\
**Dado** que tenho dados inválidos de uma nova tarefa\
**Quando** eu chamo a função adicionar_tarefa(dados)\
**Então** é retornado False\
**E** nenhuma tarefa é adicionada à lista\

`CT4 - Marcar tarefa como concluída`\
**Dado** tenho uma tarefa registrada e não marcada como concluída\
**Quando** chamo a função alterar_status(tarefa, 1)\
**Então** o status da tarefa é alterado para 1 no banco de dados\
**E** é retornado True\

`CT5 - Desmarcar tarefa como concluída`\
**Dado** que existe uma tarefa marcada como concluída e dentro da data aceitável\
**Quando** chamo a função alterar_status(tarefa, 0)\
**Então** o status da tarefa é alterado para 0\
**E** é retornado True\

`CT6 - Editar uma tarefa com dados corretos`\
**Dado** que existe uma tarefa\
**E** tenho dados corretos\
**Quando** chamo a função editar_tarefa(dados)\
**Então** a tarefa é alterada no banco de dados\
**E** é retornado True

`CT7 - Editar uma tarefa com dados incorretos`\
**Dado** que existe uma tarefa\
**E** tenho dados incorretos\
**Quando** chamo a função editar_tarefa(dados)\
**Então** é retornado False\
**E** a tarefa não é alterada

`CT8 - Vencimento de tarefas on-access`\
**Dado** que tenho uma tarefa na qual a data de vencimento já passou\
**Quando** chamo a função visualizar_tarefas()\
**Então** o status da tarefa é atualizado para 2\
**E** é retornado uma lista das tarefas registradas

`CT9 - Deletar uma tarefa`\
**Dado** que tenho uma tarefa\
**Quando** chamo a função deletarTarefa(tarefa)\
**Então** a tarefa é deletada do banco de dados\
**E** é retornado True
