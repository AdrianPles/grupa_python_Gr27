lista1 = [10, 30, 5, 7, 100, -5]
lista2 = lista1
print(lista1)

# modificam lista2
lista2.append(88)
print(lista1)

# variabile prin valoare
var1 = 100
var2 = var1

var2 = 77

print(var1) # variabila nu s-a schimbat

# structuri de date primitive
# int, float, string, bool

# structura de date complexa : list, dict, set, tuplu
# bug -> eroare in cod sau comportament neasteptat

lista3 = [9, 10, 100, 5, 50, 4]
#         0   1   2   3   4  5
# slicing, splicing
# syntax list[start:stop:step]
#           inclus : exclus : pas
# print(lista3[0:4:3])
# print(lista3[::-1])

lista4 = lista3 [:] # lista4 este o clona de lista, fara ase reflecta schimbarile de lista din lista veche lista3
lista4.append(88)

print(lista3)

lista5 = [7, 10]
lista5.append(99)
lista5.extend([100, 101, 102])
lista5 += [103, 104, 105]
lista5.remove(101) # sterge doar primul numar 101 intalnit in lista, daca sunt 2, doar primul este sters

lista5.sort()
print(lista5)
lista6 = sorted(lista5)
print(lista6)

# matrici
# Matrix, Keanu Reeves.

matrice1 = [
    [3, 4 , 10],
    [7, 8, 11],
    [0, 3, 99]
]
print(matrice1[0][1])

# list comprehension

lista7 = [3, 4, 10]
lista8 = [x ** 3 for x in lista7] # ridicare la putere a elementelor unei liste
print(lista8)

lista9 = [x **3 for x in lista7 if x % 2 ==0]
print(lista9)

# Strings
alfabet = "   abcdefghijklmn"
print(alfabet[::-1])

print(alfabet.lower())
print(alfabet.upper())
# eroare:
# alfabet[0] = "P"

print(alfabet.strip())
print(alfabet.replace('a', '00'))

prop1 = "  Gabi a inceput sa invete python. El, un student, urmeaza acest curs, cursul de python."
rezultat1 = (prop1.strip().lower().split("."))
rezultat1.remove('')
print(rezultat1)

# proop = "."
# print(prop2.split(".")

var3 = ['a', 'b', 'c', 'detrical D3 10000IU']
rezultat2 = "-".join(var3)

print(rezultat2)

if "D3" in rezultat2:
    print("avem vitamina D")

print(99 in lista5)

ex1 = "AVG-JRD-IOR:RED-GRN-BLU:QWE-RTY-UIO"
# luati acest string si creati o matrice 3x3, in care sa pastrati doar literele.
# primul element e "AVG", urmatorul de pe randul 1 e "JRD", etc.

part1 = ex1.split(":")
print(part1)
# print(part1.split("-")

rezultat3 = []
for elem in part1:
    print(elem)
    rezultat3.append(elem.split("-"))

print(rezultat3[1][0])


# while

listaw = [4, 10, 20, 50, 100]

while len(listaw)>0:
    print(listaw.pop())


nr_imens = 1000000

while nr_imens>0:
    nr_imens -= 10000
    print(nr_imens)

# folosim while cand nu stim numarul de pasi, sau cand spatiul de explorare este necunoscut,
# dar avem o conditie clara de sfarsit.

# for-ul il folosim cand parcurgem o lista deseori, sau un dictionar, etc, cand stim clar cum cum arata structura de date.
# Daca lista se modifica intre timp, for-ul nu este potrivit pentru a parcurge lista.


lista13 = [10, 20, 300, 1000]

while True:
    if len(lista13) <= 0:
        break
    print(lista13.pop())


# formatare
# f-string
name = "Alex"
age = 25
profession = "Carpenter"

print(f"Hello! My name is {name}. I'm {age} years old, and I'm a {profession}.") # varianta moderna

print("Hello! My name is {}, I'm {} years old, and I'm a {}".format(name, age, profession)) # varianta veche

# basic concatenation
print("Hello! My name is " + str(name) + ", I'm " + str(age) + " years old, and I'm a " + str(profession))

msg = " Line 1 \n Line 2"   # new line \n
print(msg)

# multiline string
msg2 = """  
Line 2
etc etc
"""
print(msg2)




