import os

def Atividade():
    print('ATIVIDADE 3: Verdadeiro ou falso\n')

def informar_dados():
    login_correto ="J"
    senha_correta = '123'
    usuario=input('Informe o Nome de usuário: ')
    senha=input('Informe a senha: ')
    if login_correto == 'J' and senha == '123':
        print ('Logado com sucesso!')
    else:
        print('dados incorretos. tente novamente.')

def main():
    Atividade()
    informar_dados()

if __name__ == '__main__':
    main()
