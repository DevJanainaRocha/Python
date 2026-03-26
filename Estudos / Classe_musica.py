#class Musica:
    #nome = ''
    #artista = ''
    #duracao = int

#Melhorando a classe acima:

class Musica:
    musicas = []

    def __init__(self, nome, artista):
        self.nome = nome
        self.artista = artista
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome}    |   {self.artista}'

    def listar_musicas():
        for musica in Musica.musicas:
            print (f'{musica.nome}  | {musica.artista}')

musica_pagode = Musica('Sai da minha aba', 'SPC')
musica_rap = Musica('Eterno amor', 'Sampa Crew')

Musica.listar_musicas()






