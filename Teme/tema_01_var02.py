# Creati o variabila care contine o lista de siruri de caractere:
# "ERR-Value Error-ER:10"
# "INF-Program launch Info-CD:5"
# "WRN-Low memory-WR:11"
#
# Si alta variabila, cu alte siruri de caractere:
# "INF-Program exit-CD:14"
# "WRN-Low disk space-WR:99"
# "WRN-Bandwith reached-WR:87"
#
# Treceti prin toate sirurile de caractere, extrageti valorile de la ERR, INF, WRN, si creati urmatorul text formatat,
# din sirurile de caracter date, de exemplu:
# Rezultatul ar trebui sa arate astfel:
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


var_1 = ["ERR-Value Error-ER:10", "INF-Program launch Info-CD:5", "WRN-Low memory-WR:11"]
var_2 = ["INF-Program exit-CD:14", "WRN-Low disk space-WR:99", "WRN-Bandwith reached-WR:87"]

def scalare_lista(lista1: list) -> list:
    '''
functia are rolul de a itera prin lista data, cu ajutorul instructiunii repetitive 'for' si
de a afla 'tag-ul' fiecarui sir, cu ajutorul instructiunii conditionale 'if/elif'.
    :param lista1: se da o lista cu 3 siruri de caractere de tipul ["***-***-**:**"]
    :return: None
    '''
    for elem in lista1:
        if elem.split("-")[0] == "ERR":
            print("[ERROR]")
        elif elem.split("-")[0] == "INF":
            print("[INFO]")
        elif elem.split("-")[0] == "WRN":
            print("[WARNING]")
        print("Mesaj :", elem.split("-")[1])
        print("Cod :", elem.split("-")[2].split(":")[1])
        print("************************************\n")
    pass

print('''
********************** VAR 1 ***************************
''')
result_1 = scalare_lista(var_1)

print('''
*********************** VAR 2 ***************************
''')
result_2 = scalare_lista(var_2)


