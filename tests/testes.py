from datetime import datetime
import unittest
from Repo.tarefa_repo import TarefaRepo
from Model.tarefa import Tarefa
from db.db import clear_db_connection, criar_banco

class TestesToDoList(unittest.TestCase):
    def setUp(self): # Executa sempre antes de cada teste
        self.tarefaCorreta = Tarefa("Tarefa", "Fazer tarefa", "2025-11-10")
        self.tarefaComStatus = Tarefa("Tarefa2", "Fazer tarefa 2", "2025-13-15", status=1)
        self.tarefaIncorreta = Tarefa("", "", "2000-01-01")
        self.tarefaVencida = Tarefa("Tarefa Vencida", "Fazer tarefa vencida", "2020-01-01")
        self.tarefaRepo = TarefaRepo() # Limpa o repositório
        clear_db_connection() # Limpa e recria o banco de dados
        criar_banco()

    def test_criarTarefaCorretamente(self):
        self.assertTrue(self.tarefaRepo.adicionar_tarefa(self.tarefaCorreta))
        self.assertTrue(
            any(
                t.titulo == self.tarefaCorreta.titulo and
                t.data_vencimento == self.tarefaCorreta.data_vencimento and
                t.descricao == self.tarefaCorreta.descricao
                for t in self.tarefaRepo.tarefas
            )
        )

    def test_criarTarefaIncorretamente(self):
        self.assertFalse(self.tarefaRepo.adicionar_tarefa(self.tarefaIncorreta))
        self.assertFalse(
            any(
                t.titulo == self.tarefaIncorreta.titulo and
                t.data_vencimento == self.tarefaIncorreta.data_vencimento and
                t.descricao == self.tarefaIncorreta.descricao
                for t in self.tarefaRepo.tarefas
            )
        )

    def test_visualizarDados(self):
        self.tarefaRepo.adicionar_tarefa(self.tarefaCorreta)

        self.assertTrue(len(self.tarefaRepo.visualizar_tarefas()) > 0)
    
    def test_marcarConcluida(self):
        self.tarefaRepo.adicionar_tarefa(self.tarefaCorreta)

        self.assertTrue(self.tarefaRepo.alterar_status(self.tarefaRepo.visualizar_tarefas()[0]['id'], True))
        self.assertTrue(self.tarefaRepo.visualizar_tarefas()[0]['status'] == 1)
    
    def test_desmarcarConcluida(self):
        self.tarefaRepo.adicionar_tarefa(self.tarefaComStatus)

        self.assertTrue(self.tarefaRepo.alterar_status(self.tarefaRepo.visualizar_tarefas()[0]['id'], 0))
        self.assertTrue(self.tarefaRepo.visualizar_tarefas()[0]['status'] == 0)
    
    def test_editarTarefaCorretamente(self):
        self.tarefaRepo.adicionar_tarefa(self.tarefaCorreta)
        tarefa_id = self.tarefaRepo.visualizar_tarefas()[0]['id']

        self.assertTrue(self.tarefaRepo.editar_tarefa(tarefa_id, "Tarefa Editada", "Descrição Editada", "20-12-2025"))
        
        tarefa = self.tarefaRepo.visualizar_tarefas()[0]

        self.assertTrue(
            tarefa['nome'] == "Tarefa Editada" and
            tarefa['descricao'] == "Descrição Editada" and
            tarefa['data'] == "2025-12-20"
        )
    
    def test_editarTarefaIncorretamente(self):
        self.tarefaRepo.adicionar_tarefa(self.tarefaCorreta)
        tarefa_id = self.tarefaRepo.visualizar_tarefas()[0]['id']

        self.assertFalse(self.tarefaRepo.editar_tarefa(tarefa_id, "", "", "20-12-1"))
        
        tarefa = self.tarefaRepo.visualizar_tarefas()[0]

        self.assertTrue(
            tarefa['nome'] == "Tarefa" and
            tarefa['descricao'] == "Fazer Tarefa" and
            tarefa['data'] == "2025-10-11"
        )
    
    def test_vencimentoTarefa(self):
        self.tarefaRepo.adicionar_tarefa(self.tarefaVencida)
        tarefas = self.tarefaRepo.visualizar_tarefas()
        now = datetime.now()

        # Verificar se a tarefa está vencida e não está marcada como vencida
        for t in tarefas:
            if datetime.strptime(t['data'][:10], "%Y-%m-%d") < now:
                self.assertEqual(t['status'], 2)

    def test_deletarTarefa(self):
        self.tarefaRepo.adicionar_tarefa(self.tarefaCorreta)
        tarefa_id = self.tarefaRepo.visualizar_tarefas()[0]['id']
        
        self.assertTrue(self.tarefaRepo.deletar_tarefa(tarefa_id))
        self.assertFalse(
            any(
                t['id'] == tarefa_id
                for t in self.tarefaRepo.visualizar_tarefas()
            )
        )
    

if __name__ == '__main__':
    unittest.main()