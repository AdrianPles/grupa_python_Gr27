my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
# my_sliced_list = my_list[2:-5]
# print(my_sliced_list)
my2_list = list(my_list)
my2_list.sort()  # lista sortata ascendent
print(my2_list)
my3_list = list(my_list)
my3_list.reverse() # lista cu elementele inversate
print(my3_list)
my4_list = list(my2_list)
my4_list.reverse() # lista cu elementele ordonate descedent, am preluat lista my2_list cu elementele ordonate ascendent
print(my4_list)
print(my2_list[1::2]) # afisare elemente pare din lista cu pas de 2, index inceput este 1
print(my2_list[::2]) # afisare elemente impare din lista cu pas de 2, index inceput este 0
print(my2_list[2::3]) # afisare elemente din lista multiplu de 3, index de inceput este 2, pas 3
print(my_list) # lista initiala ramane neschimbata
