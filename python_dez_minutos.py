# Isso aqui é um comentário

# Variáveis
nome = "Gabriel"
mensagem = "Texto bem legal"
numero = 80
nota = 9.5
verdade = True
falso = False

nome[:6] # Gabrie
nome[2:5] # bri
nome[4:] # iel
nome[::-1] #leirbaG


# Operadores Aritmeticos
10 + 10
5 - 2
3 * 4
10 / 5
15 // 2 # Divisão Inteira
30 % 4 # Módulo/Resto
3 ** 10 # Potência

# Operadores lógico
True and True
False or True
not True

# Operadores Relacionais
1 == 1
2 != 1
2 > 1
1 < 2
2 >= 1
1 <= 2


# Listas, Tuplas e Dicionarios

# Lista
a = [1, 2, "gato", True, "bicicleta"]
a[2] # "gato"
a.append(5) # [1, 2, "gato", True, "bicicleta", 5]

# Tupla
b = (2, 4, 6)
b[2] # 6

# Dicionario
c = {'chave': "valor", "numero": 20}
c['chave'] # "valor"


# Estruturas de decisão

if a == "teste":
    print "Gabriel"
elif b == "outra_coisa":
    print "Miranda"
else:
    print "Carvalho"


# Loops

while True:
    print "Executando ..."


for i in [1,2,3,4,5]:
    print i


# Funcoes

def somar(numero1, numero2):
    return numero1 + numero2

somar(2,2)

def subtrair(numero1=0, numero2=0):
    return numero1 - numero2

subtrair(numero1=10, numero2=5)
subtrair(numero1=40)
subtrair()


# Classes

class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        return "AUAU!"

    def dizer_nome(self):
        print "Meu nome é {}!".format(self.nome)

dog = Cachorro("Billy")
dog.latir()
