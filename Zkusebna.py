class Auto:
    def __init__(self):
        self.barva = "cervena"
        self.pozice = 0
        self.rychlost = 10

    def __str__(self):
        return f"p: {self.pozice} r: {self.rychlost} {self.barva}"
    def popojed(self):
        self.pozice = self.pozice + self.rychlost

trabant = Auto()
skoda = Auto()
print(skoda)
print(trabant)
trabant.popojed()
print(skoda)
print(trabant)




# for radek in range(2, 7):
#     for sloupec in range(2, 6):
#         print(f"r:{radek} s{sloupec}")
