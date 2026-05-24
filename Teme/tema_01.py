# Creati o variabila care contine o lista de siruri de caractere:
#
# "ERR-Value Error-ER:10"
#
# "INF-Program launch Info-CD:5"
#
# "WRN-Low memory:WR:11"
#
# Si alta variabila, cu alte siruri de caractere:
#
# "INF-Program exit-CD:14"
#
# "WRN-Low disk space-WR:99"
#
# "WRN-Bandwith reached:WR:87"
#
# Treceti prin toate sirurile de caractere, extrageti valorile de la ERR, INF, WRN, si creati urmatorul
# text formatat, din sirurile de caracter date, de exemplu:
#
# [ERROR]
# Mesaj: Value Error
# Cod: 10
#
# [INFO]
# Mesaj: Program launch Info
# Cod: 5
#
# [WARNING]
# Mesaj: Low memory
# Cod: 11
#
# Faceti asta pentru amandoua variabile, care contin acele siruri de caracter.
#
#*************************************************************************************


# declaram variabilele care contin cate o lista de siruri de caractere, var_01 si var_02

var_01 = ["ERR-Value Error-ER:10", "INF-Program launch Info-CD:5", "WRN-Low memory:WR:11"]

print('''
Tema  - 1 -
-----------
Lista initiala este :''', var_01)
print('''
----------------------------------------------------------------------------------------------------------''')
# declaram patru liste goale
lista_01 = []
elem_lista_00 = []
elem_lista_01 = []
elem_lista_02 = []

# folosind functia "for", eliminam mai intai caracterul "-" din sirurile de caractere ale listei "var_01" si obtinem
# 'lista_01' avand trei subliste
for elem in var_01:
    lista_01.append(elem.split("-"))
print('''
Lista 1 obtinuta dupa eliminarea caracterului "-" :

''', lista_01)
print('''
----------------------------------------------------------------------------------------------------------
''')
# folosim functia 'for' pentru fiecare sublista (referinta la index) a lista_01 si extragem caracterul ':'

print('Listele descompuse dupa eliminarea caracterului ":" sunt urmatoarele :\n')
for elem_00 in lista_01[0]:
    elem_lista_00.append(elem_00.split(":")) # am obtinut lista elem_lista_00 cu elementele descompuse
print(elem_lista_00)

for elem_01 in lista_01[1]:
    elem_lista_01.append(elem_01.split(":")) # am obtinut lista elem_lista_01 cu elementele descompuse
print(elem_lista_01)

for elem_02 in lista_01[2]:
    elem_lista_02.append(elem_02.split(":")) # am obtinut lista elem_lista_02 cu elementele descompuse
print(elem_lista_02)

print('''
-----------------------------------------------------------------------------------------------------------
''')
# modificam primul element din fiecare lista si ii atribuim o noua valoare, ex. err = EROARE, etc

elem_lista_00[0] = ["[ERROR]"]
print('Noua lista 00 este :',elem_lista_00)
elem_lista_01[0] = ["[INFO]"]
print('Noua lista 01 este :',elem_lista_01)
elem_lista_02[0] = ["[WARNING]"]
print('Noua lista 02 este :',elem_lista_02)

print('''
                                             << REZULTAT >>
------------------------------------------------------------------------------------------------------------
\n''')

# acum putem extrage elemente din liste cu ajutorul indexurilor
# pentru printarea formatata atribuim unor variabile valori din liste

x = elem_lista_00[0][0]
y = elem_lista_00[1][0]
z = elem_lista_00[2][1]
print(f'''
{x} \nMesaj : {y} \nCod : {z}''')
print('''-----------------
''')
m = elem_lista_01[0][0]
n = elem_lista_01[1][0]
t = elem_lista_01[2][1]
print(f'''{m} \nMesaj : {n} \nCod : {t}''')
print('''-----------------
''')
a = elem_lista_02[0][0]
b = elem_lista_02[1][0]
c = elem_lista_02[1][2]
print(f'''{a} \nMesaj : {b} \nCod : {c}''')
print('''-----------------
''')

var_02 = ["INF-Program exit-CD:14", "WRN-Low disk space-WR:99", "WRN-Bandwith reached:WR:87"]
print('''
Tema  - 2 -
-----------
Lista initiala este :''', var_02)
print('''
----------------------------------------------------------------------------------------------------------''')

# declaram patru liste goale
lista_02 = []
elem_var2_lista_00 = []
elem_var2_lista_01 = []
elem_var2_lista_02 = []

for elem_var2 in var_02:
    lista_02.append(elem_var2.split("-"))
print('''
Lista 2 obtinuta dupa eliminarea caracterului "-" :

''', lista_02)
print('''
----------------------------------------------------------------------------------------------------------
''')
# folosim functia 'for' pentru fiecare sublista (referinta la index) a lista_02 si extragem caracterul ':'

print('Listele descompuse dupa eliminarea caracterului ":" sunt urmatoarele :\n')
for elem_var2_00 in lista_02[0]:
    elem_var2_lista_00.append(elem_var2_00.split(":")) # am obtinut lista elem_var2_lista_00 cu elementele descompuse
print(elem_var2_lista_00)

for elem_var2_01 in lista_02[1]:
    elem_var2_lista_01.append(elem_var2_01.split(":")) # am obtinut lista elem_var2_lista_01 cu elementele descompuse
print(elem_var2_lista_01)

for elem_var2_02 in lista_02[2]:
    elem_var2_lista_02.append(elem_var2_02.split(":")) # am obtinut lista elem_var2_lista_02 cu elementele descompuse
print(elem_var2_lista_02)

print('''
-----------------------------------------------------------------------------------------------------------
''')

# modificam primul element din fiecare lista si ii atribuim o noua valoare, ex. err = EROARE, etc

elem_var2_lista_00[0] = ["[INFO]"]
print('Noua lista 00 este :',elem_var2_lista_00)
elem_var2_lista_01[0] = ["[WARNING]"]
print('Noua lista 01 este :',elem_var2_lista_01)
elem_var2_lista_02[0] = ["[WARNING]"]
print('Noua lista 02 este :',elem_var2_lista_02)

# acum putem extrage elemente din liste cu ajutorul indexurilor
# pentru printarea formatata atribuim unor variabile valori din liste

x_var2 = elem_var2_lista_00[0][0]
y_var2 = elem_var2_lista_00[1][0]
z_var2 = elem_var2_lista_00[2][1]
print(f'''
{x_var2} \nMesaj : {y_var2} \nCod : {z_var2}''')
print('''-----------------
''')
m_var2 = elem_var2_lista_01[0][0]
n_var2 = elem_var2_lista_01[1][0]
t_var2 = elem_var2_lista_01[2][1]
print(f'''{m_var2} \nMesaj : {n_var2} \nCod : {t_var2}''')
print('''-----------------
''')
a_var2 = elem_var2_lista_02[0][0]
b_var2 = elem_var2_lista_02[1][0]
c_var2 = elem_var2_lista_02[1][2]
print(f'''{a_var2} \nMesaj : {b_var2} \nCod : {c_var2}''')
print('''-----------------
''')
print('''
------------------------------------------------------ FINISH ----------------------------------------------''')
