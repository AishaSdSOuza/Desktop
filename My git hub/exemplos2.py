# demonstração de acesso a lista...
print('Vou montar a marmita com 5 alimentos')
MARMITA = ("Feijão","Arroz","Legumes","Saladas","Carne")
print("Eis, a nossa remomendação:", MARMITA)

RESPOSTA = input('Quer montar uma marmita diferente (s/n)?')
if RESPOSTA == "s":
    for x in range(len(MARMITA)):
        print(f"Digite o (x+1)o. item do carpapio: ")
        MARMITA[x] = input()
        print("A marmita montada foi",MARMITA)
        print("Os tres primeiros itens foram: ",MARMITA[0:3])
        print('O ultimo item da marmita foi:',MARMITA[-1] )
else:
    print("Ok, voce decide...")

