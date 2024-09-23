# Demonstração de uso diferentes operoadores...
print('Qual e o saldo atual da sua conta bancaria?')
print('Obs: utilize ponto para representar os centavos...')
SALDO = float(input())

if SALDO < 0 :
    print('Putz! Você esta devendo o banco!')
elif SALDO == 0 : 
    print('Impossivel! Deve ter ai alguns centavos...')
elif SALDO < 1:
    print("Putz! So miseros centavinhos na conta?") 
elif SALDO <= 9:
    print("Opa! Ja da para comprar umas balinhas...") 
elif SALDO >= 1000000:
    print("Eita, voce tem mais de um milhão!") 

if SALDO != 0:
    print("Ao menos, voce esta movimento a conta...")


 
