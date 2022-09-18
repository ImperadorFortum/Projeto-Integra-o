from mailbox import NotEmptyError


class Consulta():
    def __init__(self,id,nome,telefone,data_recebimento,descricao,data_entrega):
     self.id = id
     self.nome = nome
     self.telefone = telefone
     self.data_recebimento = data_recebimento
     self.descricao = descricao
     self.data_entrega = data_entrega

class Editar():
    def __init__(self,id,nome,telefone,data_recebimento,descricao,data_entrega):
     self.id = id
     self.nome = nome 
     self.telefone = telefone
     self.data_recebimento = data_recebimento
     self.descricao = descricao
     self.data_entrega = data_entrega
