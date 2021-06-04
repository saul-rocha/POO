from diretor import Diretor
from funcionario import Funcionario
from controleBonificacao import ControleBonificacao

f1 = Funcionario('Fl', '11', 1000)
d1 = Diretor('Flavio', '123', 1000, 'senha')


cb = ControleBonificacao()

cb.registra(f1)
cb.registra(d1)

print(cb._total_bonificacao)