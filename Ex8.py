import datetime

class Equipamentos:
    def __init__(self, id, descricao):
        self.id = id

        self.descricao = descricao

class Cliente:
    def __init__(self, id, nome):
        self.id = id

        self.nome = nome


class Emprestimo:
    def __init__(self, data, id, equipamentos, cliente):
        self.data = data

        self.id = id

        self.equipamentos = equipamentos

        self.cliente = cliente


cliente1 = Cliente(1, 'Thallys')
client2 = Cliente(2, 'Prefeito Géri')

equi1 = Equipamentos(1, 'Escada')
equi2 = Equipamentos(2, 'Enxada')
equi3 = Equipamentos(3, 'Serrote')
equi4 = Equipamentos(4, 'Facão')


emp = Emprestimo(1, cliente1, [equi2, equi4], datetime.datetime(2020, 12, 25))

print(f'O emprestimo com o codigo do cliente: {emp.id} esta relacionado ao cliente: {emp.cliente.nome} '
      f' \n o mesmo emprestou os equipamentos: {emp.equipamentos[3].descricao} e '
      f'{emp.equipamentos[1].descricao} com previsao de devolução: {emp.data} ')
