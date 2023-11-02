with open("2023_Dan.txt", "r") as soubor:
    for radek in soubor:
        rozdeleny_radek = radek.strip().split(":")
        print(rozdeleny_radek)
        print(f"Název položky: {rozdeleny_radek[0]} s hodnotou {rozdeleny_radek[1]}")
