# Liste


list1 = [4, 5, 10, 20, 30, 100, 500, 999, 1000]
#        0  1  2   3    4   5   6     7     8
print(list[0])
print(list[-1])

index = (len(list1)) // 2
print(list1[index])  # printeaza valoarea indexului
print(index) # printeaza indexul din lista


list2 = [0, 1, 2, 50, 100, 100, 100, 100, 2, 2, 2, 9, 10, 99]
print(list2)

# putem schimba un element din lista folosind [] si punand indexul elementului in ele.
list2[3] = 100
print(list2)

# Dictionare:

persoana = {
    "key": "valoare",
    "nume": "Alex",
    "inaltime": "1.85",
    "varsta": 27,
    "cetatean_roman": True,
    "bolnav": False,
    "greutate": 75.7,
}

# scurtaturi de copy/paste
# CTRL+C , CTRL+V
print(persoana)
# fast lookup
print(persoana["key"])
print(persoana["varsta"])
persoana["inaltime"] = "3m"
persoana["CNP"] = " 29855116656552255222"

# cel mai intalnit tip de date
# bool

# string
# cont bancar
# RO 224526579797BCR
# " helloo "
# 104 101 108 108 111  cod ASCII
# 01101010011   011001000111  1101011011  110001101  110010010 cod binar


# Seturi :
 # colectie de elemente care nu sunt duplicate

 # curly braces,
 # squigly brackets
elemset = {3, 6, 10, 9, 8, 100, 3}
print(elemset)

list2 = [0, 1, 2, 50, 100, 100, 100, 100, 2, 2, 2, 9, 10, 99]

list2_no_duplicates = set(list2)
print(list2_no_duplicates)


list3 = ["gigel_99", "alina_32", "alex", "marius"]
# "adrian" -> vreau sa-mi fac cont. introduc username. Sistemul trebuie sa verifice daca username-ul este nefolosit
# complexitate n. O(n)

# pentru un set, aceeasi actiune are O(1)

# "gigel_99" -> 98548755452
# "alina_32" -> 52215456852

list4 = list(set(list2))
print(list4)

# tuple, like a list, but immutable

coordinates = (5, 1)
coordinates3d = (0, 15, -5)

print(coordinates[1])

coordinates = (8, 19)

# Metode:

# catel = "Spot"
# catel.latra("cioara")
# catel.mananca("peste")
# catel.miroase("adrian")
# catel.musca("adrian")

# obiect.actiune/functie/metoda (paramaetrii)

lista5 = [7, 8, 100, 99]

lista5.append(-50)
print(lista5)
lista5.pop(1)
print(lista5)
lista5.reverse()
print(lista5)
lista5.sort()
print(lista5)
set2 = {7, 6, 8, 8, 10, 90, 100}
set2.add(-5)
set2.remove(90)
print(set2)

# chei de dictionare

dict_2 = {
    "key": "value",
    1: "one",
    3.14: "PI",
    True: False,
    (2,3): "coordinates",
    "bizar":{
        "level": {
            "list1": [0, 1, 2, 3, 100, 99, -5]
        }
    }
}
print(dict_2)
print("End of file")