import json
import os
from pathlib import Path


class Task:
    def __init__(self, titlu, data_limita, responsabil, categorie, task_finalizat):
        self.titlu = titlu
        self.data_limita = data_limita
        self.responsabil = responsabil
        self.categorie = categorie
        self.task_finalizat = task_finalizat

    def __str__(self):
        return f"Categoria [{self.categorie.upper()}] <-> Task: {self.titlu} <-> Responsabil: {self.responsabil} <-> Data limita: {self.data_limita} <-> Stare task: {self.task_finalizat}"

    def __repr__(self):
        return f"Task('{self.titlu}', '{self.data_limita}', '{self.responsabil}', '{self.categorie}'"


class ToDoList():
    def __init__(self):
        self.lista_categorii = []
        self.lista_taskuri = []

    def adauga_task(self):
        print("\n--- Adăugare Task Nou ---")
        titlu = input("Introduceți taskul: ").lower().strip()
        for task in self.lista_taskuri:
            if titlu == task.titlu:
                print("Acest task a fost introdus deja! Reincercati!")
                return
            else:
                continue
        data_limita = input("Introduceți data limită (ex: 22.01.2022 21:30): ")
        responsabil = input("Introduceți persoana responsabilă: ").capitalize().strip()
        while True:
            categorie = input("Introduceti categoria din care face parte taskul: ").lower().strip()
            if categorie in self.lista_categorii:
                task_nou = Task(titlu, data_limita, responsabil, categorie, task_finalizat="In desfasurare.") # aici cream obiectul Task
                self.lista_taskuri.append(task_nou)
                print("Task salvat cu succes!")
                break
            elif categorie == "e":
                break
            else:
                print(f"Categoria '{categorie}' nu exista! Categoriile valide sunt: {self.lista_categorii}")
                print("Pentru a iesi apasa 'e + ENTER'!")
                continue

    def bifeaza_task_finalizat(self, tk):
        for task in self.lista_taskuri:
            if task.titlu == tk:
                task.task_finalizat = "Finalizat"
                return
        print(f"Task-ul '{tk}' nu a fost gasit!")

    def sterge_task(self, strg_task):
        for stg_task in self.lista_taskuri:
            if stg_task.titlu == strg_task:
                self.lista_taskuri.remove(stg_task)
                print(f"Task-ul '{strg_task}' a fost sters!")
                return
        print(f"Task-ul {strg_task} nu a fost gasit!")

    def salveaza_date(self, cale_fisier, lista):
        path = Path(cale_fisier)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=2, ensure_ascii=False)
            print("Date salvate cu succes!")

    def citeste_date(self, file_name):
        path = Path(file_name)
        path.parent.mkdir(parents=True, exist_ok=True)
        # blocul try-except elimina eroarea de la prima rulare a programului, atunci cand fisierele nu au fost create inca.
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def afiseaza_meniu(self):
        print('*' * 52)
        print('*', ' ' * 18, 'To Do List', ' ' * 18, '*')
        print('*' * 52, '\n')
        print('=' * 9, 'Meniu principal', '=' * 9, '\n')
        print('1. Adauga categorie.')
        print('2. Adauga task.')
        print('3. Marcheaza task finalizat.')
        print('4. Afiseaza lista categorie.')
        print('5. Afiseaza lista task.')
        print('6. Sterge task.')
        print('7. Sortare/Filtrare task.')
        print('8. Iesire program.')
        print('-' * 30)

    def curata_ecran(self):
        # functia este utila la rularea programului din terminal!
        os.system("cls" if os.name == "nt" else "clear")


start_to_do = ToDoList()
start_to_do.curata_ecran()
start_to_do.lista_categorii = start_to_do.citeste_date("category.json")
date_taskuri = start_to_do.citeste_date("tasks.json")
# dupa citirea fisierului 'tasks.json', reconvertim dictionarul in obiecte de tip Task
start_to_do.lista_taskuri = [Task(**tk) for tk in date_taskuri]

while True:
    start_to_do.afiseaza_meniu()
    optiune = input("Alege optiunea (1/2/3/4/5/6/7/8): ")
    if optiune == "1":
        start_to_do.curata_ecran()
        while True:
            print('*' * 7, "apasa tasta 'ENTER' pentru a reveni la Meniul principal", '*' * 7, '\n')
            cat = input("Alege categoria : ").lower().strip()
            if cat == "":
                start_to_do.curata_ecran()
                break
            elif cat in start_to_do.lista_categorii:
                print(f"Categoria '{cat}' exista deja! Reincercati.")
                continue
            else:
                start_to_do.lista_categorii.append(cat)
                print(f"Categoria '{cat}' s-a adaugat cu succes!")
    elif optiune == "2":
        start_to_do.curata_ecran()
        start_to_do.adauga_task()
        start_to_do.curata_ecran()
    elif optiune == "3":
        start_to_do.curata_ecran()
        print("Lista de taskuri este urmatoarea :\n")
        for task in start_to_do.lista_taskuri:
            print(task)
        print("-" * 20)
        tsk_final = input("Marcati task-ul finalizat: ").lower().strip()
        start_to_do.bifeaza_task_finalizat(tsk_final)
        start_to_do.curata_ecran()
    elif optiune == "4":
        if len(start_to_do.lista_categorii) == 0:
            print("Nu aveti categorii in lista!\n")
            continue
        else:
            start_to_do.curata_ecran()
            print("\n")
            print("Lista de categorii este urmatoarea :\n")
            for categorie in start_to_do.lista_categorii:
                print(f"[{categorie}]".upper())
    elif optiune == "5":
        if len(start_to_do.lista_taskuri) == 0:
            print("Nu aveti taskuri in lista!\n")
            continue
        else:
            start_to_do.curata_ecran()
            print("\n")
            print("Lista de taskuri este urmatoarea :\n")
            for task in start_to_do.lista_taskuri:
                print(task)
    elif optiune == "6":
        start_to_do.curata_ecran()
        print("Lista de taskuri este urmatoarea :\n")
        for task in start_to_do.lista_taskuri:
            print(task)
        print('\n')
        sterg_tsk = input("Introduceti numele task-ului pe care doriti sa-l stergeti: ").lower().strip()
        start_to_do.sterge_task(sterg_tsk)
        start_to_do.curata_ecran()
# todo
    elif optiune == "7":
        print('\n')
        input("In progress...press 'Enter' to continue. ;-)")
        print('\n')
        start_to_do.curata_ecran()
    elif optiune == "8":
        print("\n")
        print("Ati iesit din program. O zi buna!")
        break
    else:
        print("\n")
        print("Va rog sa introduceti o valoare valida! (1/2/3/4/5/6/7/8)")
        continue

# convertim obiectul intr-un dictionar si pe urma salvam valorile in fisierul 'tasks.json'
# rezultatul este o lista de dictionare
dictionar_taskuri = [tk.__dict__ for tk in start_to_do.lista_taskuri]
start_to_do.salveaza_date("tasks.json", dictionar_taskuri)

# nu este necesara convertirea in dict deoarece lista_categorii contine doar text
# rezultatul este o lista simpla cu elementele "categorii"
start_to_do.salveaza_date("category.json", start_to_do.lista_categorii)