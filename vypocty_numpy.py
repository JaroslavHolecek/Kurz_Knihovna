import numpy

tabulka = numpy.zeros((4,4))
tabulka[1][2] = 6
tabulka[2] = numpy.array((1,2,3,4))
print(tabulka)
print("Max přes celou tabulku:",tabulka.max())
print("Max přes jednu dimenzi tabulku:",tabulka.max(0))
print("Sum přes jednu dimenzi tabulku:",tabulka.sum(0))
print("Pozice maxima přes jednu dimenzi tabulku:",tabulka.argmax(0))
print("Průměr přes jednu dimenzi tabulku:",tabulka.mean(0))

tabulka2 = numpy.ones((4,4))
print(tabulka2)

soucet = tabulka + tabulka2
print(soucet)
soucet[soucet > 1] *= 2
print(soucet)
filtr = soucet[soucet > 1]
print(filtr)

