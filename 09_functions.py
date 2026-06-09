import random
from functools import reduce
from pprint import pprint
from lib.core import even_numbers, is_even

print(random.sample(range(0,1000), 15))

random_numbers = [424, 739, 196, 456, 231, 962, 431, 617, 599, 74, 714, 565, 587, 941, 701]


# filter(), map(), reduce(), zip()

# lambda functions:

def mult_2(param1):
    return param1 * 2

print(mult_2(10))

# functie efemera (lambda)
square = lambda x: x * 2
print(square(10))

print("\n=============== Filter function: ===================")

# filtrati toate numerele multiplu de 7

rezultat = list(filter(lambda  x: x % 7 == 0, random_numbers))

print(rezultat)

rezultat2 =list(filter(is_even, random_numbers))
print(rezultat2)


# map (), reduce(), zip()

print("\n=============== Map function: ===================")

random_numbers = [424, 739, 196, 456, 231, 962, 431, 617, 599, 74, 714, 565, 587, 941, 701]
# var1
ひらが = list(map(lambda X: X // 2, random_numbers))

print(ひらが)

var2 = list(map(lambda x: x ** 3, random_numbers))
print(var2)


print("\n============= Reduce function: ==========")


var3 = reduce(lambda a, b: a +b, random_numbers, 100000)

print(var3)

var4 = reduce(lambda  a, b: a * b, random_numbers)
print(var4)

print(len(str(var4)))

random_letters = ['b', 'z', 'f', 'h', 'l', 'u', 'o']

print(chr(64))
random_letters = []

def generate_random_chars(count = 10, min_char = 97, max_char = 122):
    # count = 10
    # min_char = 97
    # max_char = 122

    # for i in range(count):
    #     random_letters.append(chr(random.randint(min_char, max_char)))
    #
    # print(random_letters)

    step1 = random.sample(range(min_char, max_char + 1), count)
    print(step1)
    step2 = list(map(lambda x: chr(x), step1))
    random_letters = step2
    return random_letters

random_letters = generate_random_chars()
print(random_letters)
random_japanese_characters = generate_random_chars( count= 20, min_char= 12400, max_char= 12500)
print(random_japanese_characters)

print("\n============== Zip Function: ===================")


names = ["John", "James", "Turk", "Maria", "Oprah"]
ages = [18, 20, 35, 50, 10]

combined_list = list(zip(names, ages)) # tuple
combined = dict(zip(names, ages)) # dict
print(combined_list)
print(combined)
names1 = list(combined.keys()) # extrage toate cheile din dict
value = list(combined.values()) # extrage toate valorile din dinct
print(names1)
print(value)

name_at_index1 = list(combined.keys())[1] # convertire dict in list si extragere cheie de la index 1
print(name_at_index1)


print("\n=============== Key Values ===================")

score = [6, 8, 4, 10, 9]

# people = [{
#     "name": "John",
#     "age": 18,
#     "score": 6
# },
#     {
#
#     }]

zipped_people = list(zip(names, ages, score))
print(zipped_people)

people = []

for elem in zipped_people:
    # elem = ('John', 18, 6) *** tuple
    people.append({
        "name": elem[0],
        "age": elem[1],
        "score": elem[2]
    })
pprint(people, sort_dicts=False)

sorted_list = sorted(people, key = lambda a: a['score'], reverse=False)
print(sorted_list)