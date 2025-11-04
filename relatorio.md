# Relatório do Ciclo TDD

O desenvolvimento de cada funcionalidade seguiu estritamente o ciclo TDD. Abaixo está o relatório de passos para cada Caso de Teste (CT), com as evidências de falha (Red) e sucesso (Green) extraídas dos arquivos. Quando houve refatoração (na fase Refactor), há a explicação das alterações realizadas ao perceber que algo poderia ser feito de uma forma melhor.

**`Obs*: Como placeholder para evitar exceções de código, as funções eram criadas com uma apenas linha que retornava False ou None`**

### CT 1: Criar Tarefa Corretamente
* **Red:** Um teste foi escrito (`test_criarTarefaCorretamente`) para adicionar uma tarefa e falhou. A evidência (`ct1.png`) mostra a falha `AssertionError: False is not true`.
* **Green:** O código mínimo foi implementado em `tarefa_repo.py` para que a tarefa fosse salva no banco e a função retornasse `True`. A evidência (`ct1-s.png`) mostra `Ran 1 test... OK`.
* **Refactor:** Não houve refatoração específica para este CT.

### CT 2: Criar Tarefa Incorretamente
* **Red:** Um teste (`test_criarTarefaIncorretamente`) foi escrito para validar que a função `adicionar_tarefa` retornaria `False` ao receber dados inválidos (título vazio). O teste falhou (`ct2.png`) com `AssertionError: True is not false`, indicando que a função retornou `True` incorretamente.
* **Green:** A função `adicionar_tarefa` foi ajustada para incluir a validação (`if not t.titulo... return False`). O teste passou, como visto na evidência de sucesso (`ct2-s.png`).
* **Refactor:** Não houve refatoração específica para este CT.

### CT 3: Visualizar Tarefas
* **Red:** O teste `test_visualizarDados` foi criado para verificar se uma lista com tarefas era retornada. Ele falhou (`ct3.png`) com `AssertionError: False is not true`, pois a função `visualizar_tarefas` retornou uma lista vazia (`len() < 0` é `False`).
* **Green:** O código da função foi implementado para consultar o banco de dados e retornar as tarefas. O teste passou, como visto na evidência (`ct3-s.png`).
* **Refactor:** A função `visualizar_tarefas` sofreu refatoração posterior durante o **CT 8**.

### CT 4: Marcar Tarefa como Concluída
* **Red:** O teste `test_marcarConcluida` foi escrito, esperando um retorno `True` da função de alteração de status. O teste falhou (`ct4.png`) com `AssertionError: False is not true`, pois a função `alterar_status` ainda não estava implementada.
* **Green:** A função `alterar_status` foi implementada para executar o `UPDATE` no banco de dados. O teste passou, como visto na evidência (`ct4-s.png`).
* **Refactor:** Houve refatoração, o plano inicial era ter duas funções dedicadas especialmente para marcar ou desmarcar. Durante a fase de refatoração, percebeu-se que apenas uma função `alterar_status` com um parâmetro era necessária, unificando a lógica e permitindo maior reusabilidade.

### CT 5: Desmarcar Tarefa como Concluída
* **Red:** Este teste (`test_desmarcarConcluida`) foi implementado levando em consideração que haveria uma função específica para desmarcar. Porém, a refatoração anterior mostrou que não seria necessário, logo, não houve falhas, já que a função `alterar_status` foi desenvolvida de forma modular o suficiente para suportar ambos casos de teste diretamente.
* **Green:** A função implementada no passo anterior já atendia a este caso de uso (alterando o status para `0`). O teste passou, como visto na evidência (`ct5-s.png`).
* **Refactor:** A refatoração deste CT pode ser considerada unificada com a do CT 4.

### CT 6: Editar Tarefa Corretamente
* **Red:** O teste `test_editarTarefaCorretamente` foi escrito. A evidência de falha (`ct6.png`) mostra `AssertionError: None is not true`, indicando que a função `editar_tarefa` foi criada, mas não retornava `True` após a execução.
* **Green:** A função foi então desenvolvida para retornar `True` após o `UPDATE` no banco e o teste passou, como visto na evidência (`ct6-s.png`).
* **Refactor:** Não houve refatoração específica para este CT.

### CT 7: Editar Tarefa Incorretamente
* **Red:** O teste `test_editarTarefaIncorretamente` foi escrito para garantir que a edição falhe com dados inválidos. O teste falhou (`ct7.png`) com `AssertionError: False is not true` por não haver verificação na função originalmente.
* **Green:** A função `editar_tarefa` foi alterada, implementando a validação (`if not titulo...`). O teste passou (`ct7-s.png`).
* **Refactor:** Não houve refatoração específica para este CT.

### CT 8: Vencimento de Tarefas (On-Access)
* **Red:** O teste `test_vencimentoTarefa` foi escrito para verificar se, ao `visualizar_tarefas`, as tarefas vencidas tinham seu status atualizado para `2`. O teste falhou (`ct8.png`) com `AssertionError: True is not false`, já que ainda não havia a função de atualização dos dados.
* **Green:** A lógica foi implementada em conjunto com a função `atualizar_tarefas_vencidas`. O teste passou (`ct8-s.png`).
* **Refactor:** Houve refatoração, a lógica inicial era um loop dentro de `visualizar_tarefas`, aonde cada iteração checava a data de vencimento, caso vencido, executava uma query. Na refatoração, isso foi extraído para uma função dedicada `atualizar_tarefas_vencidas`, que executa um único `UPDATE` no banco antes de buscar os dados, tornando o processo mais eficiente, sem a necessidade de abrir várias conexões e executar diversas querys.

### CT 9: Deletar Tarefa
* **Red:** O teste `test_deletarTarefa` foi escrito. A evidência de falha (`ct9.png`) mostra `AssertionError: None is not true`, indicando a não implementação prévia da função.
* **Green:** A função `deletar_tarefa` foi corrigida para incluir a query para deletar a tarefa passada e em caso de sucesso `return True`. O teste passou (`ct9-s.png`).
* **Refactor:** Não houve refatoração específica para este CT.
