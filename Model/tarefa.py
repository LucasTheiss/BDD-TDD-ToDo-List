class Tarefa:
    def __init__(
            self, 
            titulo: str, 
            descricao: str, 
            data_vencimento: str, 
            status: int = 0, 
            id: int = None
        ):
        self.id = id
        self.titulo = titulo
        ano, mes, dia = map(int, data_vencimento.split("-"))
        self.data_vencimento = f"{ano:04d}-{mes:02d}-{dia:02d}"
        self.descricao = descricao
        self.status = status
