a = 10
b = 2

try:
    vysledek = a / b + 10
    print(f"Výsledek {a}/{b} je {vysledek}")
except ZeroDivisionError as err:
    print("Nulou nejde dělit - zadej jiné číslo")
except TypeError as err:
    print("Dělit umím jen čísla")
except Exception as err:
    print("Nastala chyba:", err)


# vyrob soubor faktura.tex
import os
os.system('latex faktura.tex')

