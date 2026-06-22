# Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
# ○ __init__ : instanțiem numărător și numitor
# ○ __str__ : afisam "numărător/numitor"
# ○ __add__ : returnam o noua fractie care reprezinta adunarea
# ○ __sub__: returnam o nouă fracție care reprezinta scădearea
# ○ inverse: returnează o nouă fracție (inversa fracției)

import math


class Fractie:
    def __init__(self, numarator, numitor):
        if numitor == 0:
            raise ValueError("Numitorul nu poate fi zero!")
        cmmdc = math.gcd(numarator, numitor)
        self.numarator = numarator // cmmdc
        self.numitor = numitor // cmmdc

    def __str__(self):
        return f"Fractia are forma {self.numarator}/{self.numitor}."

    def __add__(self, fractie_noua):
        # Formulă: a/b + c/d = (a*d + b*c) / (b*d)
        numarator_nou = (self.numarator * fractie_noua.numitor) + (self.numitor * fractie_noua.numarator)
        numitor_mou = self.numitor * fractie_noua.numitor
        return Fractie(numarator_nou, numitor_mou)

    def __sub__(self, fractie_noua):
        # Formulă: a/b - c/d = (a*d - b*c) / (b*d)
        numarator_nou = (self.numarator * fractie_noua.numitor) - (self.numitor * fractie_noua.numarator)
        numitor_mou = self.numitor * fractie_noua.numitor
        return Fractie(numarator_nou, numitor_mou)

    def __invert__(self):
        if self.numarator == 0:
            raise ValueError("Nu se poate inversa o fractie cu numaeatorul 0!")
        return Fractie(self.numitor, self.numarator)


fractie_1 = Fractie(1, 3)
fractie_2 = Fractie(4, 3)
fractie_3 = Fractie(2, 3)
print(fractie_1)

adunarea = fractie_1 + fractie_2 + fractie_3
scaderea = fractie_2 - fractie_1 - fractie_3
print(f'Adunarea fractiilor ',adunarea)
print(f"Scaderea fractiilor ",scaderea)
print(f'Inversa fractiei 1 ', fractie_1.__invert__())
print(f"Apelare clasa :", Fractie(numarator=10, numitor=5))