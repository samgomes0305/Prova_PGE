# Lê a palavra inserida
palavra = input("digite uma palavra: ")
#Cria uma lista com as possíveis vogais do idioma português
vogais = [
    'ã', 'õ'
    'â', 'ê', 'ô',
    'á', 'é', 'í', 'ó', 'ú',
    'à',
    'a', 'e', 'i', 'o', 'u'
]
# Cria uma variável que será usada para contar as vogais
count_vogal = 0
# Percorre todas as letras da palavra
for l in palavra:
  l = l.lower()
# Cria uma condicional que considera apenas as vogais que serão adicionadas a variavel já criada
  if l in vogais:
        count_vogal +=1
# Usa a função integrada ao python "len" para contar o número de letras na palavra
quantidade = len(palavra)
# Cria uma condicional utilizando um string method que verifica se a primeira letra é maiúscula
if palavra.istitle() == True:
# Se a palavra retornar "True", então ela é maiúscula, caso contrário é minúscula
    print(f"A palavra '{palavra}' começa por letra Maiúscula")
else:
    print(f"A palavra '{palavra}' começa por letra minúscula")
# Imprime na tela a quantidade de letras, de consoantes e vogais respectivamente
print(f"A palavra '{palavra}' tem {quantidade} letras")
print(f"A palavra '{palavra}' tem {quantidade - count_vogal} consoantes")
print(f"A palavra '{palavra}' tem {count_vogal} vogais")