import openpyxl

# seznam názvů zpracovávaných souborů (takto musí být ve stejné složce jako náš .py soubor)
vsechny_soubory = ["Spol1.xlsx", "Spol2.xlsx", "Spol3.xlsx", "Spol4.xlsx", "Spol5.xlsx"]

# načtení souboru/listu/buňky do kterého zapíšeme výsledek
nazev_vysledek = "Vysledek.xlsx"
excel_vysledek = openpyxl.load_workbook(nazev_vysledek) # otevření/načtení souboru - soubor již musí existovat
list_vysledek = excel_vysledek.active # výběr aktivního listu
bunka_vysledek = list_vysledek.cell(row=2, column=2) # pracujeme s buňkou B 2

soucet = 0
for soubor_nazev in vsechny_soubory:
    excel_soubor = openpyxl.load_workbook(soubor_nazev)  # otevření/načtení souboru
    aktivni_list = excel_soubor.active  # výběr aktivního listu
    bunka = aktivni_list.cell(row=2, column=2)  # výběr buňky
    soucet = soucet + bunka.value # scitam s předchozími hodnotami

bunka_vysledek.value = soucet # zápis nasčítané hodnoty do buňky ve výsledném souboru
excel_vysledek.save(nazev_vysledek) # uložení změn v excelu
