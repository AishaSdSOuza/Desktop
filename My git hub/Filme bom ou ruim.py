# Filme bom ou ruim
FILME = input("Digite o filme de sua preferencia: ")
AVALIAÇÃO = int(input("Qual a sua avalição de 1 a 5? "))


match AVALIAÇÃO:
    case 1:
        print("PESSIMO")
        PORQUE = input("Descreva porque a avaliação foi baixa")
    case 2:
        print("RUIM")
        PORQUE = input("Descreva porque a avaliação foi baixa")
    case 3:
        print("RAZOAVEL")
    case 4:
         print("BOM")
    case 5:
        print("OTIMO")
    case _:
        print("Opção não reconhecida!")    
      
