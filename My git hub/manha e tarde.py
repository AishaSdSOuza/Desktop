#Demonstração de operadores lógico em condicionais ...
print('O que voce vai fazer amanhã de manhã?')
print('Dormir/ Estudar / Planejar')
MANHA = input()
print('O que voce vai fazer amanhã a tarde?')
print('Jogar/ Treinar / Trabalhar')
TARDE = input()

if not MANHA or not TARDE:
    print('Voce precisa dizer o que fazer!') 
else:
    if MANHA == 'Dormir' or TARDE == 'Jogar':
        print("Voce esta desperdiçando o seu dia!")
    elif MANHA == "Estudar" or TARDE == 'Treinar':
        print("Que Bom! Voce ira se aperfeiçoar!")
    elif MANHA == "Planejar" and TARDE == 'Trabalhar':
        print('')


