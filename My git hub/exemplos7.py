# Demonstração do comportamento das listas 
print('Vou almoçar em um restaurante a quilo!')

ORIGINAL = ['Arroz','Feijão', 'Batata', 'Alface', 'Frango']
print('Eis, a minha comida:', ORIGINAL)
DERIVADA = ORIGINAL
print('Meu amigo ira comer também:', DERIVADA)

print('Vou alterar as opções sem ele ver...')
ORIGINAL.remove('Arroz')
ORIGINAL.remove('Feijão')
ORIGINAL.remove('Alface')
ORIGINAL.append('picanha')
ORIGINAL.append('linguiça')

print('Amiguinho,me mostre o que voce vai comer?')
print('Claro! Da uma conferida', DERIVADA)
