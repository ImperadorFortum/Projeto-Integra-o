from .db import connect
from .consulta import Consulta

class ConsultaDAO():
    """DAO - Data Access Object"""

    def add(c: Consulta):
        conn = connect()  # Cria a conexão
        cursor = conn.cursor()  # manipular o banco
        SQL = "INSERT INTO Consultorias(nome,telefone,data_recebimento,descricao,data_entrega) VALUES (?,?,?,?,?);"
        dados = [c.nome,c.telefone, c.data_recebimento, c.descricao, c.data_entrega]  # lista com os valores de entrada
        cursor.execute(SQL, dados)
        # pega o ID do último selecionado
        id_return = cursor.execute("SELECT last_insert_rowid();")
        id = id_return.fetchall()[0][0]

        conn.commit()  # salvar no banco
        conn.close()  # fecha a conexão

        return id

    def edit(c: Consulta):
        conn = connect()  # Cria a conexão
        cursor = conn.cursor()
        SQL = "UPDATE Consultorias SET nome=?,telefone=?,data_recebimento=?,descricao=?,data_entrega=? WHERE id=?"
        dados = [c.nome,c.telefone, c.data_recebimento,c.descricao,c.id,c.data_entrega] # lista com os valores de entrada
        cursor.execute(SQL, dados)
        conn.commit()  # salvar no banco
        conn.close()  # fecha a conexão

    def delete(id):
        print(id)
        conn = connect()
        cursor = conn.cursor()
        SQL = "DELETE FROM Consultorias WHERE id = ?;"
        cursor.execute(SQL, [id])
        conn.commit()  # salvar no banco
        conn.close()  # fecha a conexão
        

    def selectAll() -> list:
        lista_consultas = []

        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM Consultorias;"
        cursor.execute(SQL)
        return_list = cursor.fetchall()
        for c in return_list:
            # Obs.: Lembrar de colocar o ID no objeto Consulta
            nova_consulta = Consulta(c[0],c[1], c[2], c[3], c[4], c[5],)
            lista_consultas.append(nova_consulta)

        conn.close()

        return lista_consultas
