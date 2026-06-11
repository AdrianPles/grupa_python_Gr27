# Teme fundamentale 3.1 (platforma)

# Creati un program care are ca scop un meniu.
# Meniul se va selecta prin introducerea de la tastaura a unui numar intre 1 si 5 captat intr-o variabila.
# Printati in terminal acest mesaj:
#
# “””
# 1 – Afisare lista de cumparaturi
# 2 – Adaugare element
# 3 – Stergere element
# 4 – Sterere lista de cumparaturi
# 5 - Cautare in lista de cumparaturi “””
#
# Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
# tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
# afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
# element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
# - daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
# scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”
# Implementati logica pentru toate aceste operatii, optional folosind functii.


import sys
print("======================================================")

print('''
1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Stergere lista de cumparaturi
5 - Cautare in lista de cumparaturi
6 - Iesire
''')

print("======================================================")

def lista_cumparaturi(lista = list):
    '''
    functia modifica o lista in raport cu optiunile noastre
    :param lista: se da o lista cu oricate elemente
    :return: pass
    '''
    str_var_opt = ["1", "2", "3", "4", "5", "6"]  # var str optima d.p.d.v. al stabilitatii programului :-)
    # am adaugat optiunea 6 pentru iesirea din bucla (program)
    # int_var_optiune = [1, 2, 3, 4, 5, 6] -> pentru varianta cu int(input)

    while True:
        elem = input("Introduceti optiunea dvs. = ")
        if elem == str_var_opt[5]:
            sys.exit("Ati iesit din program !")
        elif elem == str_var_opt[0]:
            print("Lista este : ", lista)
        elif elem == str_var_opt[1]:
            new_elem = input('Introduceti noul element = ').lower()
            lista.append(new_elem)
            print("Lista actualizata, este :", lista)
        elif elem == str_var_opt[2]:
            print(f"Lista este {lista}")
            del_elem = input("Introduceti elementul pe care doriti sa-l stergeti = ").lower()
            if del_elem == "":
                print("Reincercati. Nu ati introdus elementul.")
            elif del_elem not in lista:
                print(f"Elementul '{del_elem}' nu se afla in lista.")
            else:
                lista.remove(del_elem)
            print("Lista actualizata, este :", lista)
        elif elem == str_var_opt[3]:
            lista.clear()
            print("Ati sters lista de cumparaturi.", lista)
        elif elem == str_var_opt[4]:
            cautare = input("Introduceti elementul cautat = ").lower()
            if cautare in lista:
                print(f"Elementul '{cautare}' se afla in lista.", lista)
            else:
                print(f"Elementul '{cautare}' nu se afla in lista.", lista)
        else:
            print("Alegerea nu exista. Reincercati")



shopping_list = ["legume", "fructe"] # lista data
test = lista_cumparaturi(shopping_list) # apelare functia lista_cumparaturi


