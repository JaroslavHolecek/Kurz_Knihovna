cislo = 10
print(cislo)
pocitadlo = 0
while cislo > 1:
    pocitadlo += 1 # pocitadlo = pocitadlo + 1
    if cislo % 2 == 0: # zbytek po dělení 2 je nula
        cislo = cislo // 2 # // jsou dělení s výsledkem celé číslo
    else:
        cislo = (cislo * 3) + 1
    print(cislo)
# vytisknout počet kroků: pro 10 -> 6
print(f"Počet kroků je {pocitadlo}")