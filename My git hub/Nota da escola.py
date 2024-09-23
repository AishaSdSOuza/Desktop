# aluno reprovado ou aprovado
N1 = float(input("1a. nota: "))
N2 = float(input("2a. nota: "))
N3 = float(input("3a. nota: "))
N4 = float(input("4a. nota: "))

#calculo da media final
MEDIA = (N1 + N2 + N3 + N4) / 4

#VERIFICAÇÃO SE APROVADO OU NÃO
if MEDIA >= 6:
    print("estudante aprovado!")
else:
    print("estudante reprovado!")

print("a media dele é:", MEDIA)    
