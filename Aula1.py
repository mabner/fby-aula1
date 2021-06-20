# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Códigos gerados em aula:
# %% [markdown]
# ## Hello-world

# %%
# -*- coding: utf-8 -*-

a = 9
b = 5
c = a - b
print("----------------------------------------------------")
print("                      Olá mundo!                    ")  # Comentario de uma linha
print("----------------------------------------------------")

"""
Comentario
de
varias linhas
"""
print("Tchao mundo!", a, "menos", b, "é", c)
# A=2 =/= a=2

# %% [markdown]
# ## Declaração de funções

# %%
# Declaração de funções
def somar(a=-100, b=100):
    return a + b

# Chamada de função
total = somar(a, b)
print("Soma total de", a, "mais", b, "é de:", total)
print("Chamada direta de função. Soma é:", somar(a, b))
print("Uma variavel:", somar(b=a))


# %%
# range( valor inicial , valor de parada , intervalo )
for i in range(0, 125, 25):
    print(i)

# %% [markdown]
# ## Usando bibliotecas

# %%
# Usando bibliotecas
import random as rd

print("Os 5 ganhadores são:")
for i in range(5):
    a = rd.randint(1,100)
    print("Número:", a)


# %%
numeros = [2, 7, 16, 34, 95, 68, 3]
numero = rd.choice(numeros)
print("Números concorrendo:", numeros)
print("Número sorteado:", numero)

# %% [markdown]
# ## Criando e usando o ambiente virtual
#
# - Criar o ambiente: python -m venv itp
#
# - Ativar o ambiente: itp\Scripts\activate
#
# - Desativar o ambiente: itp\Scripts\deactivate
#
#
#
# ### Salvar as dependencias pra instalar depois
#
# - Salvar as dependencias: pip freeze > requirements.txt
#
# - Usando o arquivo pra instalar: pip install -r requirements.txt
#
# Ps. Adicionar a pasta do ambiente no .gitignore.
# %% [markdown]
# ## Operações com strings

# %%
# .strip() = trim()

nome = "Marcos"

print(len(nome), "caracteres")


# %%
print(nome[0].upper(), nome[2].upper(), nome[5].upper())


# %%
for i in range(7): # 7 porque para uma casa antes
    print(nome[:i]) # Vai do inicio até o valor atual de i


# %%
print("O r está na posição", nome.find("r")+1)


# %%
setaDireita = ">>>>>"
setaEsquerda = "<<<<<"


def seta(lado):
    if lado == "d":
        for i in range(6):
            print(setaDireita[:i])
    elif lado == "e":
        for i in range(6):
            print(setaEsquerda[:i])
    else:
        print("Escolha os lados por d ou e")

seta(input("Escolha o lado (d ou e):"))

# %% [markdown]
# ### Diferenres formas de usar o valor da variável

# %%
nome = input("Nome:")
sobrenome = input("Sobrenome:")
idade = input("Idade:")

nomecompleto = nome + " " + sobrenome

print(nome + " " + sobrenome + " tem " + idade + " anos.")


# %%
print("%s %s tem %s anos." % (nome, sobrenome, idade))


# %%
print(f"{nomecompleto} tem {idade} anos.")

# %% [markdown]
# ## Tratamento de exceções

# %%
try:
    a = 0
    b = 50
    if(a<b):
        raise Exception("A não pode ser menor que B") # Exceções personalizadas
    c = b/a
    x = "Oi" + b
except ZeroDivisionError:
    print("Não é possível dividir por zero")
except Exception as erro:
    print("Erro:", erro)

# %% [markdown]
# ## Manipulação de arquivo
# %% [markdown]
# ### Leitura

# %%
import os

arquivo = open("req.txt", "r")
linhas = arquivo.readlines() # Lê todas as linhas e permite escolher qual vai ser usada
numLinha = 0
# print(arquivo.readline()) # Lê uma linha

print(f"Linha {numLinha} ->", linhas[numLinha]) # Define nos [] ou usa uma variável

arquivo.close()

# %% [markdown]
# ### Escrita

# %%
import os

arquivo = open("escrita.txt", "r+") # a permite apenas adicionar ao final do arquivo
arquivo.write("\nEscrita")

arquivo.close()

# %% [markdown]
# ### Close automático

# %%
import os

with open("escrita.txt", "r+") as arquivo:
    print(arquivo.readlines())
    arquivo.write("\nnovo_texto")

# %% [markdown]
# ## Estrutura de dados

# %%
nomes = ["Marcos", "Abner", "Leidiane"]
print(nomes[-1]) # -1 retorna o ultimo item da lista


# %%
nomes.append(256)
nomes.append("Silva")

if "Silva" in nomes:
    print("Silva está na lista")
else:
    print("Silva não está na lista")
print(nomes[-1])


# %%
for i in nomes: # Imprimir os itens da lista
    print(i)


# %%
del nomes[3] # Remover da lista
# nomes.sort() # Ordena os itens da lista em ordem asc., sort(reverse=True) ordena em desc.
print("antes: " , nomes[1])
print("sorted: " , sorted(nomes)) # sorted mostra ordenada mas não altera a lista
print("depois: ", nomes[1])


# %%
for i in nomes:
    print(i)


# %%
nomes = ["Marcos", "Leidiane", "José", "Maria", "Christian"]

casa = {
    "tipo": "Apartamento",
    "quartos": 2,
    "transporte": ["moto", "bicicleta"],
    "moradores": nomes[0:2]
}

print(casa)


# %%
# https://www.w3schools.com/python/python_ref_string.asp
for i in casa: # Print mais organizado, cada chave em uma linha
    print(f"{i.capitalize()}: {casa[i]}")


# %%
for i in casa.items(): # .items() imprime em tuplas
    print(i)


# %%
print("Tipo:", type(casa)) # Imprime o tipo do objeto

# %% [markdown]
# ### Classes

# %%
class Corais:
    tipo = "cnidários"

    def __init__(self, nome): # Contrutor
        self.nome = nome # self. == this

    def classif(self):
        print(f"{self.nome} LPS")

c = Corais("Ducan Aussie")
d = Corais("Trumpet Kryptonita")
print("..::", c.tipo.capitalize(), "::..")
c.classif()
d.classif()

# %% [markdown]
# ### Mais coisas legais do Python
# %% [markdown]
# #### Enumerate

# %%
for i, nome in enumerate(nomes): # enumerate retorna a posição da string encontrada
    if nome == "Maria":
        print("Posição do nome:", i)

# %% [markdown]
# #### List comprehension

# %%
numeros = [0, 3, 6, 9]
lista_por_3 = [ int(x/3) for x in numeros if x > 5] # Percorre a lista dividindo cada item por 3, se forem maio que 5
print (lista_por_3)

# %% [markdown]
# #### Função sobre todos os elementos

# %%
def pi(a):
    return a * 3.14

multiplicados = list(map(pi, numeros))
print(multiplicados)

# %% [markdown]
# #### Redução (map c/ 2 argumentos)

# %%
from functools import reduce

def soma (a, b):
    return a+b

print(reduce(soma, numeros)) # Percorre a lista somando todos os itens

# %% [markdown]
# #### Acesso simultâneo

# %%
nome = ["Marcos", "Leidiane"]
segundonome = ["Abner", "Aparecida", "Silva"]

for nome, segundonome in zip(nome, segundonome): # Zip junta os items das listas de acordo com as posições
    print(nome, segundonome)


# %%
