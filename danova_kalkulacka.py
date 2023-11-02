DAN = 0.15

hruby_prijem = float(input("Zadej hrubý příjem:"))
naklady = float(input("Zadej náklady:"))


zisk_pred_zdanenim = hruby_prijem - naklady
dan_k_platbe = zisk_pred_zdanenim * DAN
zisk_po_zdaneni = zisk_pred_zdanenim * (1-DAN)

with open("2023_Dan.txt", "w") as soubor:
    soubor.write(f"Příjem:{hruby_prijem}\n")
    soubor.write(f"Náklady:{naklady}\n")
    soubor.write(f"Daň k platbě:{dan_k_platbe}\n")
    soubor.write(f"Zisk po zdanění:{zisk_po_zdaneni}\n")

