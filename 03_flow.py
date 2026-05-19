# flow -> curge

lista1 = [5, 10, 20, 40, 90, 100]

# instructiuni for, while, if, try/catch, switch, etc.

nr_executii = 0

for elem in lista1:
    print(elem)
    nr_executii = nr_executii + 1

print("Nr. executii :")
print(nr_executii)

# range(4) -> 0, 1, 2 , 3
# len(lista1) -> 6
for i in range(len(lista1)): # lungimea listei - indecsii
    print("-------------------------------------")
    print(i) # indecsii de la lista
    print(lista1[i]) # printeaza valoarea din lista

