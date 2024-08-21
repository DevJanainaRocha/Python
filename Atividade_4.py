import os

def Atividade():
    print('ATIVIDADE 4: Coordenadas\n')

def informar_coordenadas():
    coordenadaX=float(input('Informe as coordenadas X: '))
    coordenadaY=float(input('Informe as coordenadas Y: '))
    if coordenadaX > 0 and coordenadaY > 0:
        print('O ponto esta localizado no primeiro quadrante')
    elif coordenadaX < 0 and coordenadaY > 0:
        print('O ponto esta localizado no segundo quadrante')
    elif coordenadaX < 0 and coordenadaY < 0:
        print('O ponto esta localizado no terceiro quadrante')
    elif coordenadaX > 0 and coordenadaY < 0:
        print('O ponto esta localizado no quarto quadrante')
    else:
        print('o ponto está localizado no eixo de origem.')

def main():
    Atividade()
    informar_coordenadas()

if __name__ == '__main__':
    main()