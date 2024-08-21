import os

def atividade():
    print("ATIVIDADDE 2: Classificação da idade\n")

def classificar_idade():
    idade=int(input('Digite a sua idade: '))
    if idade <= 12:
        print(f'A idade informada é {idade} e você ainda é uma criança')
    elif idade == 13 or idade < 18:
        print(f'A idade informada é {idade} e você já é um adolescente')
    else:
         print(f'Você já se encontra na fase adulta')

def main():
    atividade()
    classificar_idade()

if __name__ == '__main__':
    main()