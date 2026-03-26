import os

def Tabuada():
    print('Tabuada um número\n')
    num = int(input('Digite um número: '))

    print(f'A Tabuada de {num} é:\n')
    for i in range (1,11):
        resultado = num * i
        print(f'{num} é {num} x {i} = {resultado}')

def menu():
    print('O que deseja fazer agora?\n')
    print('1. Recomeçar')
    print('0. Encerrar')

def escolha():
    opcao = int(input('Escolha uma opcao: '))
    if opcao == 1:
        Tabuada()
    elif opcao == 0:
        encerrar_programa()
    else:
        print('Opção inválida. Tente novamente!')

def encerrar_programa():
    os.system ('cls')
    print('Programa encerrado')
        
def main():
    Tabuada()
    menu()
    escolha()

if __name__ == '__main__':
    main()

          

