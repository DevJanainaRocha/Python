import os

def atividade():
    print ('Atividade 1: ímar e par\n')

def menu_de_opcoes():
    print('1. digitar um número')
    print('2. Sair do programa')

def sair_do_programa():
    os.system('cls')
    print('Programa encerrado!\n') 

def resultado():
    num=int(input('Digite um número: '))
    if num % 2 == 0:
        print ('Este número é par')
    else:
        print ('Este número é ímpar')

def escolher_opcao():
    menu_de_opcoes()
    opcao=int(input('Escolha uma das opções acima: '))
    match opcao:
        case 1:
            resultado()
        case 2:
            sair_do_programa()
        
def main():
    atividade()
    escolher_opcao()
    resultado()
  
    
if __name__ == '__main__':
    main()