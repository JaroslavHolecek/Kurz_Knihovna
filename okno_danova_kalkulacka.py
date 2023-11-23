from PyQt5 import QtWidgets
from PyQt5 import QtGui

app = QtWidgets.QApplication([]) # inicializace aplikace

hlavni_okno = QtWidgets.QWidget()  # vytvoření objektu hlavního okna
hlavni_okno.setWindowTitle("Daňová kalkulačka")  # název okna


svisle_1 = QtWidgets.QVBoxLayout() # vytvoření Layout managera typu "pod sebou"

usporadani = QtWidgets.QHBoxLayout() # vytvoření Layout managera typu "vedle sebe"
hlavni_okno.setLayout(usporadani) # nastavení Layout managera našemu hlavnímu oknu

tlacitko = QtWidgets.QPushButton('Spočítej')  # vytvoření objektu tlačítko
usporadani.addWidget(tlacitko)  # vložení tlačítka do Layout managera

napis_hruby_prijem = QtWidgets.QLabel('Zadej hrubý příjem:')  # vytvoření objektu pro zobrazení textu
svisle_1.addWidget(napis_hruby_prijem)

usporadani.addLayout(svisle_1)

validator_celych_cisel = QtGui.QIntValidator() # zde si vybereme konktrétní validátor

vstup_hruby_prijem = QtWidgets.QLineEdit()
vstup_hruby_prijem.setValidator(validator_celych_cisel)
svisle_1.addWidget(vstup_hruby_prijem)

napis_naklady = QtWidgets.QLabel('Zadej náklady:')  # vytvoření objektu pro zobrazení textu
usporadani.addWidget(napis_naklady) # vložení nápisu (objektu, který zobrazuje nápis) do Layout managera

vstup_naklady = QtWidgets.QLineEdit()
vstup_naklady.setValidator(validator_celych_cisel)
usporadani.addWidget(vstup_naklady)

vstup_prijemce = QtWidgets.QLineEdit()
usporadani.addWidget(vstup_prijemce)


napis_dan = QtWidgets.QLabel('')  # vytvoření objektu pro zobrazení textu
usporadani.addWidget(napis_dan)


def spocitej_dan():
    naklady = int(vstup_naklady.text())
    hruby_prijem = int(vstup_hruby_prijem.text())
    zisk = hruby_prijem - naklady
    dan = zisk * 0.15

    prijemce = vstup_prijemce.text()

    napis_dan.setText(f"Daň k zaplacení: {dan}")
    with open("faktura.tex", "w") as soubor:
        soubor.write("""
\documentclass{article}
\\usepackage[czech]{babel}
\\usepackage[letterpaper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}
\\usepackage[colorlinks=true, allcolors=blue]{hyperref}
\\title{Faktura}
\\author{Jaroslav Holeček}
\date{\\today}

\\begin{document}
\maketitle

\section{Příjemce}

Příjemce je""" + prijemce + """ a má zaplatit """ + str(dan) + """

\end{document}
        """)

tlacitko.clicked.connect(spocitej_dan)

hlavni_okno.show() # okno bude viditelné
app.exec() # spuštění aplikace