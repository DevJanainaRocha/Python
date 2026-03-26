class Pessoa:
    pessoas = []

    def __init__(self, nome='', idade= 0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.profissao} | {self.idade}'
    
    def aniversario(self):
        self.idade += 1

    @classmethod 
    def listar_pessoa(cls):
        print(f'{'Nome'.ljust(25)} | {'Profissão'.ljust(25)} | {'Idade'}\n')
        for pessoa in cls.pessoas: 
            print (f'{pessoa.nome.ljust(25)} | {pessoa.profissao.ljust(25)} | {pessoa.idade} anos')

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao} e tenho {self.idade} anos.'
        else:
            return f'Olá, sou {self.nome}!'     

pessoa1 = Pessoa('Janaina', 42, 'Desenvolvedora BackEnd')
pessoa2 = Pessoa('Luiza', 30, 'Desenvolvedor')
pessoa3 = Pessoa('Jaque', 22)

Pessoa.listar_pessoa()
print('\n**Lista de pessoas com a idde a pessoa 1 incrementada**\n')
pessoa1.aniversario()
Pessoa.listar_pessoa()
print('\n**Saudação da pessoa 1**\n')
print(pessoa1.saudacao)
