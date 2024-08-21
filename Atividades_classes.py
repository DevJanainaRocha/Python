#1.Implemente uma classe chamada Carro com os atributos básicos, 
#como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
# Instanciando um carro e atribuindo valores aos seus atributos
meu_carro = Carro(modelo='Fusca', cor='Azul', ano=1970)

#2.Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo 
#e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, capacidade, ativo=False, inauguracao=int):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo 
        self.capacidade = capacidade
        self.inauguracao = inauguracao
# Instanciando um carro e atribuindo valores aos seus atributos
meu_restaurante = Restaurante(nome='Rancho', categoria='Comida de Boteco', capacidade= '350 mil', inauguracao= 2014 )

#3.Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como 
#parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria, capacidade, ativo=False, inauguracao=int):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo 
        self.capacidade = capacidade
        self.inauguracao = inauguracao
novo_restaurant = Restaurante(nome='Rancho', categoria= 'Comida de boteco')

#4.Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância,
#seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma 
#instância de restaurante.

class Restaurante:
     def __init__(self, nome, categoria, capacidade, ativo=False, inauguracao=int):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo 
        self.capacidade = capacidade
        self.inauguracao = inauguracao
    
     def __str__(self):
        return f'{self.nome}    |   {self.categoria}'

#5.Crie uma classe chamada `Cliente` e pense em 4 atributos. Em seguida, instancie
#3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome, cpf, nascimento, cidade):
        cliente1 = Cliente (nome= 'Janaina', cpf= '094.564.957-60', nascimento= '12/07/1982', cidade='Sobradinho')
        cliente2 = Cliente (nome= 'Rogerio', cpf= '093.313.177-19', nascimento= '16/06/1981', cidade='Sobradinho')
        cliente3 = Cliente (nome= 'Nicolas', cpf= '123.456.789-01', nascimento= '25/02/2010', cidade='Sobradinho')
        cliente4 = Cliente (nome= 'Théo', cpf= '321.654.987-02', nascimento= '18/06/2020', cidade='Sobradinho')
