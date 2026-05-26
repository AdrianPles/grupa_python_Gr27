# functii
# def -> keyword, face parte din sintaxa de definire a unei functii.

# definire de functie
def greet():
    print("hello")
    print("this is flume")


# apelare de functie

greet()


# add
# a, b -> parametri

def add(a, b):
    return a + b


# ctrl + x
print(add(5, 10))
# add(5, 10)
print(add(60, 90))
print(add(100, 333))


# mul

def mul(a, b):
    return a * b


var1 = mul(5, 15)
add(var1, 35)


# parametru se numeste acel "a". Argument este valoarea ce o dam acelui "a", de exmplu 5

# creati sub, care scade a - b, div care imparte a / b, si pow care ridica a ** b

def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def pow(a, b):
    return a ** b


# 6 - 4 * 10

rezultat = sub(6, mul(4, 10))
print(rezultat)

# 5 + 4 * 8 ** 2
rezultat2 = add(5, mul(4, pow(8, 2)))
print(rezultat2)


# return implicit, None

def speak(word="woof!"):
    print(word)


speak()
speak("Meow!")


def drive(car_model, max_speed=130):
    print(f"{car_model} is running at a max speed of {max_speed}")


drive("Audi")
drive("Mazda", "red")


# typed function

# a % b

def modulo(a: int, b: int) -> int:
    """
    Returns the remainder of the division between two numbers.
    :param a: the number that is divided by
    :param b: the number that does the division
    :return: remainder
    """
    return a % b


# RST / Sphinx style docs ^
print(modulo(13, True))

nr = [10, 11, 21, 5, -1, 20, 3]


def even_numbers(list1):
    # iteram prin lista. folosim modulo
    res = []
    for n in list1:
        if n % 2 == 0:
            print(f"am gasit numar par: {n}")
            res.append(n)
    return res


result = even_numbers(nr)
print(result)

nr2 = [7, 22, 4, 5, -2, 8, 10]
result2 = even_numbers(nr2)
print(result2)

# tema:

# "ERR-Value Error-ER:10"
# "INF-Program launch Info-CD:5"
# "WRN-Low memory-WR:11"

var2 = ["ERR-Value Error-ER:10", "INF-Program launch Info-CD:5", "WRN-Low memory-WR:11"]

for s in var2:
    print(s.split("-")[0])
    print(f"Mesaj: {s.split("-")[1]}")
    # print("Mesaj: ", s.split("-")[1])
    # s -> string :::: .split("-") -> list :::: [2] -> elem din lista dupa index :::: elem este string, deci s.split("-")[2] -> string :::: .split(":") -> list :::: acea_lista[1] -> al doilea element, care este numarul de cod ce ne intereseaza.
    print(s.split("-")[2].split(":")[1])

# [ERROR] -> folositi if
# Mesaj: Value Error
# Cod: 10

print("asdf", "shadow", "cat", sep="-----", end="END OF LINE\n")














