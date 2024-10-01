# demonstração de metodos em listas...
INSS = ['Maria', 'Manoel', 'José', 'Isabela']
print('Eis, a fila do inss:', INSS)

NOVO = input('Insira mais uma pessoa:')
INSS.append(NOVO)
print('Converindo a nova lista:', INSS)

print('Vouu tirar a ultima pessoa desta lista...')
ESPECIAL = INSS.pop()

print('Agora, vou coloca-la na frente de todos!')
INSS.insert(0, ESPECIAL)
print('Conferindo a lista:', INSS)

print('Maria não gostou e reclamou...')
INSS.remove('Maria')
print('E agora, ela ficou pe da vida: ', INSS)

print('Para não ter mais reclamação, vamos atender...')
INSS.sort()
print('... em ordem alfabetica:', INSS)

print('Onde esta esta pessoa chamada', ESPECIAL, '?')
print('Ela agora ficou na posição', INSS.index (ESPECIAL)+1, '!')