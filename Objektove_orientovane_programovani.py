class Auto:
    def __init__(self, bar, poz, rych):
        self.barva = bar
        self.pozice = poz
        self.rychlost = rych

    def __str__(self):
        return f"p: {self.pozice} r: {self.rychlost} {self.barva}"
    def popojed(self, kolikrat):
        self.pozice = self.pozice + (self.rychlost * kolikrat)

    def srazka(self, druhe_auto):
        self.barva = "oprýskaná"
        druhe_auto.pozice += 50

trabant = Auto("modrá", 0, 10)
skoda = Auto("červená", 100, 50)
print(skoda)
print(trabant)
trabant.popojed(3)
trabant.srazka(skoda)
print(trabant)
print(skoda)






# for radek in range(2, 7):
#     for sloupec in range(2, 6):
#         print(f"r:{radek} s{sloupec}")
