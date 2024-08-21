
print('Meu dicionário\n')
pessoa = [{'Nome': 'Janaina', 'Idade': '41', 'Cidade': 'Rio de Janeiro'}]
# Atualização de Idade
pessoa['idade'] = 31

# Adicionando Profissão
pessoa['profissao'] = 'Engenheiro'

# Remoção de Elemento
del pessoa['cidade']


#- Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:

frase = "Python muito legal."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)




