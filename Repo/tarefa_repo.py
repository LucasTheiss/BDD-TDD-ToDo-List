from datetime import datetime
from db.db import get_db_connection
from Model.tarefa import Tarefa

class TarefaRepo:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, t: Tarefa) -> bool:
        conn = get_db_connection()
        if not t.titulo or not t.data_vencimento:
            return False
        conn.execute(
            "INSERT INTO tarefa (nome, descricao, data) VALUES (?, ?, ?)",
            (t.titulo, t.descricao, t.data_vencimento)
        )
        conn.commit()
        conn.close()
        self.tarefas.append(t)
        return True

    def visualizar_tarefas(self, id: int = 0) -> list:
        self.atualizar_tarefas_vencidas() # atualiza on access

        conn = get_db_connection()

        # Por foco em testes, essa possibilidade de filtro por id foi adicionada
        query = "SELECT * FROM tarefa"
        if id > 0:
            query += f" WHERE id = {id}"

        try:
            cursor = conn.execute(query)
            tarefas = cursor.fetchall()
            conn.close()
        except:
            return []

        return tarefas
    
    def alterar_status(self, id: int, status: int) -> bool:
        conn = get_db_connection()
        try:
            conn.execute(
                "UPDATE tarefa SET status = ? WHERE id = ?",
                (status, id)
            )
            conn.commit()
            conn.close()
            self.tarefas = map(lambda t: setattr(t, 'status', status) or t if t.id == id else t, self.tarefas)
            return True
        except:
            return False
        
    def atualizar_tarefas_vencidas(self):
        now = datetime.now().strftime("%Y-%m-%d")
        conn = get_db_connection()
        conn.execute(
            "UPDATE tarefa SET status = 2 WHERE status = 0 AND date(data) < date(?)",
            (now,)
        )
        conn.commit()
        conn.close()

    def editar_tarefa(self, id: int, titulo: str, descricao: str, data_vencimento: str) -> bool:
        """
        Funcão dedicada exclusivamente para editar os de uma tarefa, sem considerar status ou ID.
        """
        if not titulo or not data_vencimento:
            return False

        conn = get_db_connection()
        try:
            conn.execute(
                "UPDATE tarefa SET nome = ?, descricao = ?, data = ? WHERE id = ?",
                (titulo, descricao, data_vencimento, id)
            )
            conn.commit()
            conn.close()

            # Atualiza na lista interna
            for t in self.tarefas:
                if t.id == id:
                    t.titulo = titulo
                    t.descricao = descricao
                    t.data_vencimento = data_vencimento
                    break

            return True
        except:
            return False

    def deletar_tarefa(self, id: int) -> bool:
        conn = get_db_connection()
        try:
            conn.execute(
                "DELETE FROM tarefa WHERE id = ?",
                (id,)
            )
            conn.commit()
            conn.close()

            # Remove da lista interna
            for i, t in enumerate(self.tarefas):
                if t.id == id:
                    self.tarefas.pop(i)
                    break

            return True
        except:
            return False
