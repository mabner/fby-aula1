# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Exercício 1
# %% [markdown]
# **Sobre outras estruturas de dados, implemente**
# - Set: Coleção não ordenada sem duplicidade
# %% [markdown]
# Set é uma coleção não ordenada e sem indexação, que é imutável e não permite itens duplicados (valores duplicados são ignorados). Como não possuem indexação, não se tem uma previsão certa da ordem em que vão ser listados is itens do set. Sets são delimitados com chaves {}.
# E.g.:

# %%
peixes = {"donzela", "palhaço", "fridmani", "coris"}
print(peixes)

# %% [markdown]
# ---
# -  Tuple: Alguns valores separados por vírgula
# %% [markdown]
# Uma tupla é uma coleção ordenada que pode conter valores duplicados. A tupla é imutável, depois de criada não conseguimos alterar a ordem nem adicionar ou remover itens. Tuplas são delimitadas com parênteses ().
# E.g.:

# %%
peixes = ("donzela", "palhaço", "fridmani", "coris")
print(peixes)

# %% [markdown]
# ---
# **Sobre listas, como podemos implementá-las**
#
# - ...como uma fila (ou queue)?
#
# Na fila, o primeiro a chegar é o primeiro a sair.

# %%
class Queue:
    def __init__(self):
        self.itens = []
    def vazia(self):
        return self.itens == []
    def adicionar(self, item):
        self.itens.insert(0,item)
    def remover(self):
        return self.itens.pop()
    def tamanho(self):
        return len(self.itens)

fila = Queue()

print("Fila vazia?", fila.vazia())
print("Tamanho da fila:", fila.tamanho())
fila.adicionar("Peixe Azul"); print("Itens da fila:", fila.itens)

fila.adicionar("Peixe Laranja"); print("Itens da fila:", fila.itens)

fila.adicionar("Peixe Roxo"); print("Itens da fila:", fila.itens)

fila.adicionar("Peixe Amarelo"); print("Itens da fila:", fila.itens)

print("Tamanho da fila:", fila.tamanho())

fila.remover()
print("Itens da fila:", fila.itens)

fila.remover()
print("Itens da fila:", fila.itens)

fila.remover()
print("Itens da fila:", fila.itens)

print("Tamanho da fila:", fila.tamanho())
print("Fila vazia?", fila.vazia())

# %% [markdown]
# ---
# - ...como uma pilha (ou stack)?
#
#
# Na pilha, o último a chegar é o primeiro a sair, como em uma pilha de pratos.

# %%
class Queue:
    def __init__(self):
        self.itens = []
    def vazia(self):
        return self.itens == []
    def adicionar(self, item):
        self.itens.insert(-0,item)
    def remover(self):
        return self.itens.pop(-0)
    def tamanho(self):
        return len(self.itens)

fila = Queue()

print("Fila vazia?", fila.vazia())
print("Tamanho da fila:", fila.tamanho())
fila.adicionar("Peixe Azul"); print("Itens da fila:", fila.itens)

fila.adicionar("Peixe Laranja"); print("Itens da fila:", fila.itens)

fila.adicionar("Peixe Roxo"); print("Itens da fila:", fila.itens)

fila.adicionar("Peixe Amarelo"); print("Itens da fila:", fila.itens)

print("Tamanho da fila:", fila.tamanho())

fila.remover()
print("Itens da fila:", fila.itens)

fila.remover()
print("Itens da fila:", fila.itens)

fila.remover()
print("Itens da fila:", fila.itens)

print("Tamanho da fila:", fila.tamanho())
print("Fila vazia?", fila.vazia())

# %% [markdown]
# ---
# **O que o statement else faz em um loop (note que o 'else' está identado com o 'for')?**

# %%

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# %% [markdown]
# O **else** é o caminho que o código vai seguir se a condição do **for** não for cumprida, neste caso, quando não estiver no range definido.
