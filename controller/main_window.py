from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import uic

from model.consulta import Consulta, Editar
from model.consulta_dao import ConsultaDAO 



FILE_UI = 'view/main_window.ui'


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(FILE_UI, self)
 
        self.addBtn.clicked.connect(self.add)
        self.editBtn.clicked.connect(self.edit)
        self.delBtn.clicked.connect(self.delete)

        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.loadData()

    def loadData(self):
        listaCon = ConsultaDAO.selectAll()
        for c in listaCon:
            self.addTableWidget(c)

    def add(self):
        nome = self.nome.text()
        telefone = self.telefone.text()
        data_recebimento = self.data_recebimento.text()
        descricao = self.descricao.text()
        data_entrega = self.data_entrega.text()
       

        novaConsulta = Consulta(-1, nome, telefone,
                                data_recebimento,descricao,data_entrega)
        
        id = ConsultaDAO.add(novaConsulta)
        novaConsulta.id = id

        self.addTableWidget(novaConsulta)
        
        self.nome.clear()
        self.telefone.clear()
        self.data_recebimento.clear()
        self.descricao.clear()
        self.data_entrega.clear()

    def edit(self):
        lineSel = self.tabela.currentRow()
        id = self.tabela.item(lineSel, 0)
        n_nome = self.tabela.item(lineSel,1) 
        n_telefone = self.tabela.item(lineSel,2)
        n_data_recebimento = self.tabela.item(lineSel,3)
        n_descricao = self.tabela.item(lineSel,4)
        n_data_entrega = self.tabela.item(lineSel,5)
        
        
        n_nome = self.nome.text()
        n_telefone = self.telefone.text()
        n_data_recebimento = self.data_recebimento.text()
        n_descricao = self.descricao.text()
        n_data_entrega= self.data_entrega.text()

        edit = Consulta(id, n_nome, n_telefone,
                        n_data_recebimento, n_descricao,n_data_entrega)

        self.edicao(edit)
        ConsultaDAO.edit(edit)
        
        self.nome.clear()
        self.telefone.clear()
        self.data_recebimento.clear()
        self.descricao.clear()
        self.data_entrega.clear()

    def delete(self):
        # pega a linha 
        lineSel = self.tabela.currentRow()

        item = self.tabela.item(lineSel,0) 
        id = item.text()
        print(id)
        # remove do banco
        ConsultaDAO.delete(id) 
        # remove a linha 
        self.tabela.removeRow(lineSel)

   
    def addTableWidget(self, c: Consulta):
        line = self.tabela.rowCount()
        self.tabela.insertRow(line)
        
        nome = QTableWidgetItem(str(c.id))
        telefone = QTableWidgetItem(c.telefone)
        data_recebimento = QTableWidgetItem(c.data_recebimento)
        descricao = QTableWidgetItem(c.descricao)
        data_entrega= QTableWidgetItem(c.data_entrega)


        self.tabela.setItem(line, 0, nome)
        self.tabela.setItem(line, 1, telefone)
        self.tabela.setItem(line, 2, data_recebimento)
        self.tabela.setItem(line, 3, descricao)
        self.tabela.setItem(line, 4, data_entrega)

    def edicao(self, c: Editar):
        lineSel = self.tabela.currentRow()
        n_nome = QTableWidgetItem(c.nome)
        n_telefone = QTableWidgetItem(c.telefone)
        n_data_recebimento = QTableWidgetItem(c.data_recebimento)
        n_descricao = QTableWidgetItem(c.descricao)
        n_data_entrega = QTableWidgetItem(c.data_entrega)


        self.tabela.setItem(lineSel, 0, n_nome)
        self.tabela.setItem(lineSel, 1, n_telefone)
        self.tabela.setItem(lineSel, 2, n_data_recebimento)
        self.tabela.setItem(lineSel, 3, n_descricao)
        self.tabela.setItem(lineSel, 4, n_data_entrega)

