
print("Hello World")
print("This is the change")
print("Another change")

var1 = True

# if statements:

# calculator: 9 + 8 -> 17
# decizii / alegeri

populatie_brasov = 300000
nou_nascuti_curent = 35000

populatie_brasov = populatie_brasov + nou_nascuti_curent

if populatie_brasov > 310000:
    print("populatia brasovului a crescut considerabil")
    print("felicitari")
    if populatie_brasov > 330000:
        print("populatia a crescut cu mai mulde de 10%")
else:
    print("nu se nasc destui copii sa mentina societatea curenta.")

# vrem sa printam toate numerele pare

# a+b
# a / b, a // b -> rezultatul impartirii
# a % b -> restul impartirii

# 5 // 3 -> 1, 5 % 3 ->

lista2 = [6, 7, 10, 90, 100, 33, 88, 5, 13, 0, -2, -10, -5, -100]
# for, if, %
nr_pare = []
nr_impare = []

for nr in lista2:
    # nr -> 6, 7, 8...etc
    if nr % 2 == 0:
        # nr este par
        print(nr)
        nr_pare.append(nr)
    else:
        nr_impare.append(nr)

print("Nr pare:")
print(nr_pare)
print("Nr impare:")
print(nr_impare)

# Expresii logice.

for nr in lista2:
    if nr % 2 == 0 and nr % 5 == 0:
        print("Nr urmator este si par si multiplu de 5")
        print(nr)