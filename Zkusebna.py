pocet_sloupecku = 4
pocet_radku = 6
vysledky = []
for i in range(pocet_radku):
    vysledky.append([0]*pocet_sloupecku)


print(vysledky)
vysledky[3][2] = 55
print(vysledky)

for radek in range(2, 7):
    for sloupec in range(2, 6):
        print(f"r:{radek} s{sloupec}")
