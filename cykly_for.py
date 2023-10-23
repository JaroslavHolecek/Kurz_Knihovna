# List
seznam = [1, 2, 3, 3.14, 2, 5, "Jarda", 2]

for prvek in seznam:
    if prvek == 2:
        continue # přeskočit všechna čísla 2
    if prvek == 3.14:
        break # ukončit při čísle 3.14
    print(prvek)
    print(type(prvek))
    print("======")

print("Konec")