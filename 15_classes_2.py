from enum import Enum

# Clase, liste de obiecte ale claselor si actiuni comune ale claselor.

# CATEGORIES = ["curs", "cumparaturi", "..."]
# print(CATEGORIES[15])


class Categories(Enum):
    COURSE = "course"
    SHOPPING = "shopping"
    WORK = "work"
    PRESENTS = "presents"


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    ULTRA = 4


print(Categories.WORK.value)
print(Categories.WORK.name)
curent_category = Categories.WORK

if curent_category == Categories.WORK:
    print("I'm at work!")


class Task:
    def __init__(self, title, date, owner, category):
        self.title = title
        self.date = date
        self.owner = owner
        self.category = category
        self.completed = False

    def __str__(self):
        return f"{self.title}, {self.date}, {self.owner}, {self.category}, completed = {self.completed}"

    def __repr__(self):
        return f'Task("{self.title}", "{self.date}", "{self.owner}", {self.category})'

task1 = Task("Rezolvare tema", "23.Iunie", "John", Categories.COURSE)
print((task1))

task2 = Task("Spalat vase", "23.Iunie", "John", Categories.WORK)

task3 = Task("Buy shoes", "24.Iunie", "Olivia", Categories.SHOPPING)

# todo = [task1, task2, task3]


class Todos:
    def __init__(self):
        self.todos_list = []

    # property, this is just like a class attribute, that gets calculated whenever it's read.
    # # if a programmer writes todos1.task_count, the value gets calculated on the spot, every time this property is read.
    # @property
    # def task_count(self):
    # return len(self.todos_list)

    @property
    def task_count(self):
        return len(self.todos_list)

    # modificati metoda add_task, sa nu permita adaugarea unui task cu titlu duplicat.
    # Daca exista deja un task cu acel titlu, sa printeze "Task with this title already
    # exists!.

    def add_task(self, task):
        for t in self.todos_list:
            if t.title.lower() == task.title.lower():
                print("Task with this title already exists!")
                break
        else:
            self.todos_list.append(task)

    def remove_task(self, task_to_delete):
        for task in self.todos_list:
            if task.title == task_to_delete.title:
                self.todos_list.remove(task)

    def mark_as_completed(self, task: Task):
        task.completed = True

    def filter_by_completed(self, is_completed: bool):
        # aceasta functie sa returneze toate task-urile din todos_list,
        # care sunt completed sau nu, in functie de argumentul primit.
        lista = []
        for t in self.todos_list:
            if t.completed == is_completed:
                lista.append(t)
        return lista

    def filter_by_category(self, categ):
        results = []
        for task in self.todos_list:
            if task.category == categ:
                results.append(task)
        return results

    # scrieti o metoda in clasa Todos pentru a filtra dupa owner.
    # acea metoda va returna toate task-urile ale unui owner, ce-l primim ca parametru al
    # acelei metode.

    def filter_by_owner(self, owner):
        own = []
        for task in self.todos_list:
            if task.owner.lower() == owner.lower():
                own.append(task)
        return own

    # scrieti o metoda in clasa Todos care numara toate task-urile ale unei anumite
    # categorii, si returneaza cate task-uri sunt pentru acea categorie.
    # Daca sunt 3 taskuri in total pe categoria Category.COURSE de exemplu,
    # metoda returneaza numarul 3.

    def tasks_number(self, categ):
        nb_of_tasks = 0
        for task in self.todos_list:
            if task.category == categ:
                nb_of_tasks += 1
        return nb_of_tasks

    def __str__(self):
        return f"{self.todos_list}"


todos1 = Todos()
todos1.add_task(task1)
todos1.add_task(task2)
todos1.add_task(task3)
todos1.add_task(Task("Go to second-hand store", "25.June", "Olivia", Categories.SHOPPING))

# print(task1)
todos1.mark_as_completed(task1)
print(task1)

print(" =========== Number of tasks by category :")
print(todos1.tasks_number(Categories.SHOPPING))


print(" =========== Task filtered by completed:")
print(todos1.filter_by_completed(False))


print("\n==============================")


todos1.add_task(Task("Write a poem", "Today", "olivia", Categories.PRESENTS))

print("\n===========Task count ================")
print(len(todos1.todos_list))
print((todos1.task_count))

print("================================")

print(todos1)
print("\n")
print('-' * 15, 'Stergere task', '-' * 15)
# todos1.remove_task(task2)
# print(todos1)

task4 = Task("name", "23.June", "owner", Categories.SHOPPING)

# Categories.SHOPPING     ///       "shopping"

task5 = Task("Rezolvare aceasta Tema", "23.IUNIE", "John", Categories.COURSE)
todos1.add_task(task5)
print(task5.category)
print("\n========================")

print('\n','-' * 15, 'Tipariere lista totala', '-' * 15)
print(todos1)
task6 = Task("Rezolvare Tema", "23.IUNIE", "Oliver", Categories.COURSE)
todos1.add_task(task6)
print(todos1)


for c in Categories:
    print(c)

task7 = (Task("Buy some shoes", "28.Iunie", "George", Categories.SHOPPING))
task8 = (Task("Buy car", "31.Iunie", "Adrian", Categories.WORK))

todos1.add_task(task8)
print("\n---------------------------------")
todos1.add_task(task7)
print(todos1.todos_list)
print(todos1.task_count)

print(" =========== Task filtered by owner :")
print(todos1.filter_by_owner("adrian"))

print(" =========== Number of tasks by category :")
print(todos1.tasks_number(Categories.PRESENTS))

print(" =========== Task filtered by completed:")
print(todos1.filter_by_completed(False))